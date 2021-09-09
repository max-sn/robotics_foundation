"""
Exponential coordinates of rigid body motion
============================================

"""

import numpy as np
from .exponential_coordinates_of_rotation import (SO3_to_vec, vec_to_so3,
                                                  vec_to_SO3)


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
