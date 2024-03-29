"""
.. rubric:: ``modern_robotics.num``

This module contains numerical implementations, using
`numpy <https://numpy.org/>`_. These implementations are the default when using
``import modern_robotics``. They can be loaded specifically by using
``import modern_robotics.num as mr``.

"""

import numpy as np
from . import gen


def SO3_to_vec(R: np.array) -> np.array:
    """
    'Differentiation' of a rotation matrix by using the matrix log to
    determine the angular velocity that reaches that orientation in unit time.

    Args:
        R: 3 by 3 rotation matrix :math:`\\RotationMatrix \\in \\SOthree`.

    Returns:
        Angular velocity vector :math:`\\omega` with length
        :math:`\\theta`.

    See Also:
        :py:func:`so3_to_vec`
        :py:func:`vec_to_SO3`
    """
    if np.allclose(R, np.eye(3)):
        # If R is equal to identity (to precision), angular velocity magnitude
        # is 0 and direction is undefined.
        theta = 0
        omega = np.full((3, 1), np.nan)
    elif np.allclose(R.trace(), -1):
        # If trace of R is -1, angular velocity magnitude is pi, and direction
        # is either x, y, or z, depending on values of R.
        theta = np.pi
        if not np.allclose(R[2, 2], -1):
            omega = 1/(np.sqrt(2 * (1 + R[2, 2]))) * \
                (R[:, 2:3] + np.array([[0], [0], [1]]))
        elif not np.allclose(R[1, 1], -1):
            omega = 1/(np.sqrt(2 * (1 + R[1, 1]))) * \
                (R[:, 1:2] + np.array([[0], [1], [0]]))
        elif not np.allclose(R[0, 0], -1):
            omega = 1/(np.sqrt(2 * (1 + R[0, 0]))) * \
                (R[:, 0:1] + np.array([[1], [0], [0]]))
    else:
        theta = np.arccos(1/2 * (R.trace() - 1))
        omega_tilde = 1/(2 * np.sin(theta)) * (R - R.T)
        omega = so3_to_vec(omega_tilde)

    return omega * theta


def vec_to_SO3(omega: np.array, theta: float = None) -> np.array:
    """
    'Integration' of an angular velocity to determine the orientation
    (expressed as rotation matrix) that this angular velocity reaches in unit
    time.

    Uses Rodrigues' formula to solve the matrix exponential of the vector's
    skew-symmetric matrix form.

    .. math::

        \\RotationMatrix =
        \\exp(\\TildeSkew{\\UnitLength{\\omega}}\\theta) =
        I + \\TildeSkew{\\UnitLength{\\omega}}\\sin\\theta +
        \\TildeSkew{\\UnitLength{\\omega}}^2(1-\\cos\\theta) \\in \\SOthree

    Args:
        omega: 3 vector angular velocity. Can be unit length, in that case
               theta should also be provided.
        theta: If omitted, the Euclidean norm of omega is assumed to be theta.

    Returns:
        3 by 3 rotation matrix :math:`\\RotationMatrix \\in \\SOthree`.

    See Also:
        :py:func:`vec_to_so3`
        :py:func:`SO3_to_vec`
    """
    if theta is None:
        # If no theta, take length of omega and make omega unit length.
        theta = np.linalg.norm(omega)
        omega = omega / theta

    # Skew-symmetric form of omega
    omega_tilde = vec_to_so3(omega)

    # Rodrigues' formula
    return np.eye(3) + np.sin(theta) * omega_tilde + \
        (1 - np.cos(theta)) * np.linalg.matrix_power(omega_tilde, 2)


def vec_to_so3(v: np.array) -> np.array:
    """
    Build a skew-symmetric matrix from a 3 vector.

    Args:
        v: 3 vector.

    Returns:
        3 by 3 skew-symmetric matrix form of v, :math:`\\TildeSkew{v}`.

    See Also:
        :py:func:`so3_to_vec`
    """
    return np.array([[0, -v.item(2), v.item(1)],
                     [v.item(2), 0, -v.item(0)],
                     [-v.item(1), v.item(0), 0]])


def so3_to_vec(v_tilde: np.array) -> np.array:
    """
    Reconstruct a 3 vector from its skew-symmetric matrix form. No check is
    performed to see if v_tilde is really skew-symmetric.

    Args:
        v_tilde: 3 by 3 skew-symmetric matrix form of v,
                 :math:`\\TildeSkew{v}`.

    Returns:
        3 vector.

    See Also:
        :py:func:`vec_to_so3`
    """
    return np.array([[v_tilde.item(2, 1)],
                     [v_tilde.item(0, 2)],
                     [v_tilde.item(1, 0)]])


def SE3_to_vec(T: np.array) -> np.array:
    """
    'Differentiation' of a transformation matrix by using the matrix log of its
    rotation matrix to determine the screw velocity vector (twist) that reaches
    this transformation in unit time.

    Args:
        T: Homogeneous transformation matrix

    Returns:
        Velocity twist vector :math:`\\Twist` with length
        :math:`\\theta`

    See Also:
        :py:func:`vec_to_SE3`
    """
    R = T[0:3, 0:3]
    p = T[0:3, 3:4]

    if np.allclose(T, np.eye(4)):
        # If T is equal to identity (to precision), the screw axis is
        # undefined and the distance travelled along the screw axis is 0.
        omega_hat = np.full((3, 1), np.nan)
        v = np.full((3, 1), np.nan)
        theta = 0
    else:
        if np.allclose(R, np.eye(3)):
            # If the rotational part of T (the rotation matrix) is equal to
            # identity (to precision), the screw axis is purely translational,
            # i.e. the pitch is infinite.
            omega_hat = np.zeros((3, 1))
            theta = np.linalg.norm(p)
            v = p / theta
        else:
            omega = SO3_to_vec(R)
            theta = np.linalg.norm(omega)
            omega_hat = omega / theta
            if np.allclose(p, np.zeros((3, 1))):
                # If the translational part is zero, the screw axis is purely
                # angular, i.e. the pitch is zero.
                v = np.zeros((3, 1))
            else:
                omega_tilde = vec_to_so3(omega_hat)
                v = (1/theta * np.eye(3) - 1/2 * omega_tilde
                     + (1/theta - 1/2 / np.tan(theta/2))
                     * np.linalg.matrix_power(omega_tilde, 2)).dot(p)

    # Screw axis
    S = np.vstack((omega_hat, v))

    return S * theta


def vec_to_SE3(S: np.array, theta: float) -> np.array:
    """
    'Integration' of a velocity twist to determine the configuration (expressed
    as transformation matrix) that this velocity twist reaches in unit time.

    Args:
        S: 6 vector velocity twist
        theta: Distance travelled along the velocity twist screw axis

    Returns:
        4 by 4 homogeneous transformation matrix
        :math:`\\HomogeneousTransformationMatrix \\in \\SEthree`

    See Also:
        :py:func:`SE3_to_vec`
    """
    omega = S[:3]
    v = S[3:]
    if np.allclose(omega, np.zeros((3, 1))):
        R = np.eye(3)
        p = v * theta
    else:
        R = vec_to_SO3(omega, theta)
        omega_tilde = vec_to_so3(omega)
        p = (np.eye(3) * theta + (1 - np.cos(theta)) * omega_tilde
             + (theta - np.sin(theta))
             * np.linalg.matrix_power(omega_tilde, 2)).dot(v)

    return R_p_to_SE3(R, p)


def big_adjoint(T: np.array) -> np.array:
    """
    Constructs the 'big adjoint' form of the transformation matrix T.

    .. math::

        \\HomogeneousTransformationMatrix =
        \\begin{bmatrix}
        \\RotationMatrix & p \\\\
        0 & 1
        \\end{bmatrix}
        \\quad\\Rightarrow\\quad
        \\Adjoint{\\HomogeneousTransformationMatrix} =
        \\begin{bmatrix}
        \\RotationMatrix & 0 \\\\
        \\TildeSkew{p}\\RotationMatrix & \\RotationMatrix
        \\end{bmatrix}

    Args:
        T: 4 by 4 homogeneous transformation matrix
           :math:`\\HomogeneousTransformationMatrix \\in \\SEthree`

    Returns:
        6 by 6 'big adjoint' form of the transformation matrix T
    """
    R = T[0:3, 0:3]
    p_tilde = vec_to_so3(T[0:3, 3:4])

    return np.vstack((np.hstack((R, np.zeros((3, 3)))),
                      np.hstack((p_tilde.dot(R), R))))


def little_adjoint(V: np.array) -> np.array:
    """
    Constructs the 'little adjoint' form of the velocity twist V.

    .. math::

        \\Twist =
        \\begin{bmatrix}
        \\omega \\\\ v
        \\end{bmatrix}
        \\quad\\Rightarrow\\quad
        \\LittleAdjoint{\\Twist} =
        \\begin{bmatrix}
        \\TildeSkew{\\omega} & 0 \\\\
        \\TildeSkew{v} & \\TildeSkew{\\omega}
        \\end{bmatrix}

    Args:
        V: 6 by 1 velocity twist

    Returns:
        6 by 6 'little adjoint' form of the twist V
    """
    w = V[:3]
    v = V[3:]

    return np.vstack((np.hstack((vec_to_so3(w), np.zeros((3, 3)))),
                      np.hstack((vec_to_so3(v), vec_to_so3(w)))))


def inv_SE3(T: np.array) -> np.array:
    """
    Inverts the transformation matrix T.

    .. math::

        \\HomogeneousTransformationMatrix =
        \\begin{bmatrix}
        \\RotationMatrix & p \\\\
        0 & 1
        \\end{bmatrix}\\in\\SEthree
        \\quad\\Rightarrow\\quad
        \\HomogeneousTransformationMatrix^{-1} =
        \\begin{bmatrix}
        \\RotationMatrix\\Transposed & -\\RotationMatrix\\Transposed p \\\\
        0 & 1
        \\end{bmatrix}\\in\\SEthree

    Args:
        T: 4 by 4 homogeneous transformation matrix
           :math:`\\HomogeneousTransformationMatrix \\in \\SEthree`

    Returns:
        4 by 4 inverse of the homogeneous transformation matrix
        :math:`\\HomogeneousTransformationMatrix^{-1} \\in \\SEthree`
    """
    R = T[0:3, 0:3]
    p = T[0:3, 3:4]

    return R_p_to_SE3(R.T, np.dot(-R.T, p))


def R_p_to_SE3(R: np.array, p: np.array) -> np.array:
    """
    Constructs a homogeneous transformation matrix from a rotation matrix and
    displacement vector.

    Args:
        R: 3 by 3 rotation matrix :math:`\\RotationMatrix\\in\\SOthree`
        p: 3 by 1 displacement vector

    Returns:
        4 by 4 homogeneous transformation matrix
        :math:`\\HomogeneousTransformationMatrix \\in \\SEthree`
    """
    return np.vstack((np.hstack((R, p)),
                      np.array([0, 0, 0, 1])))


def manipulability(J: np.array) -> np.array:
    """
    Calculates the direction and magnitude of the principal axes of the
    manipulability ellipsoid, and the ratio between largest and smallest
    eigenvalue of :math:`\\Jacobian\\Jacobian\\Transposed`.

    Args:
        J: Jacobian matrix

    Returns:
        Tuple with 2D array containing the principal axes of the manipulability
        ellipsoid, and the condition number.
    """
    A = J @ J.T

    if np.allclose(np.linalg.det(A), 0):
        raise np.linalg.LinAlgError('Singular matrix')

    w, v = np.linalg.eigh(A)

    cond = np.max(w) / np.min(w)

    H = np.hstack(tuple(np.sqrt(w[i]) * v[:, i:i+1] for i in range(len(w))))

    return H, cond
