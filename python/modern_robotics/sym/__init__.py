"""
Symbolic functions
------------------

This module contains symbolic implementations of most of the same functions as
:py:mod:`modern_robotics.num`, using
`sympy <https://www.sympy.org/en/index.html>`_. These implementations can be
loaded by using ``import modern_robotics.sym as mr``.

"""

import sympy as sp
from . import gen


def SO3_to_vec(R: sp.Matrix) -> sp.Matrix:
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
    if sp.eye(3).equals(R):
        # If R is equal to identity (to precision), angular velocity magnitude
        # is 0 and direction is undefined.
        theta = sp.Integer(0)
        omega = sp.Matrix([[sp.nan], [sp.nan], [sp.nan]])
    elif sp.simplify(sp.Trace(R)) == -1:
        # If trace of R is -1, angular velocity magnitude is pi, and direction
        # is either x, y, or z, depending on values of R.
        theta = sp.pi
        if not R[2, 2] == -1:
            omega = 1/(sp.sqrt(2 * (1 + R[2, 2]))) * \
                (R[:, 2] + sp.Matrix([[0], [0], [1]]))
        elif not R[1, 1] == -1:
            omega = 1/(sp.sqrt(2 * (1 + R[1, 1]))) * \
                (R[:, 1] + sp.Matrix([[0], [1], [0]]))
        elif not R[0, 0] == -1:
            omega = 1/(sp.sqrt(2 * (1 + R[0, 0]))) * \
                (R[:, 0] + sp.Matrix([[1], [0], [0]]))
    else:
        theta = sp.acos((sp.simplify(sp.Trace(R)) - 1)/2)
        omega_tilde = 1/(2 * sp.sin(theta)) * (R - R.T)
        omega = so3_to_vec(omega_tilde)

    return omega * theta


def vec_to_SO3(omega: sp.Matrix, theta: sp.Number = None) -> sp.Matrix:
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
        theta = omega.norm()  # 2-norm (Euclidean length)
        omega = omega.normalized()

    # Skew-symmetric form of omega
    omega_tilde = vec_to_so3(omega)

    # Rodrigues' formula
    return sp.eye(3) + sp.sin(theta) * omega_tilde + \
        (1 - sp.cos(theta)) * omega_tilde**2


def vec_to_so3(v: sp.Matrix) -> sp.Matrix:
    """
    Build a skew-symmetric matrix from a 3 vector.

    Args:
        v: 3 vector.

    Returns:
        3 by 3 skew-symmetric matrix form of v, :math:`\\TildeSkew{v}`.

    See Also:
        :py:func:`so3_to_vec`
    """
    return sp.Matrix([[0, -v[2, 0], v[1, 0]],
                      [v[2, 0], 0, -v[0, 0]],
                      [-v[1, 0], v[0, 0], 0]])


def so3_to_vec(v_tilde: sp.Matrix) -> sp.Matrix:
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
    return sp.Matrix([[v_tilde[2, 1]],
                      [v_tilde[0, 2]],
                      [v_tilde[1, 0]]])


def vec_to_SE3(S: sp.Matrix, theta: sp.Number) -> sp.Matrix:
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
    omega = S[:3, 0]
    v = S[3:, 0]
    if sp.zeros(3, 1).equals(omega):
        R = sp.eye(3)
        p = v * theta
    else:
        R = vec_to_SO3(omega, theta)
        omega_tilde = vec_to_so3(omega)
        p = (sp.eye(3) * theta + (1 - sp.cos(theta)) * omega_tilde
             + (theta - sp.sin(theta))
             * omega_tilde**2) * v

    return R_p_to_SE3(R, p)


def big_adjoint(T: sp.Matrix) -> sp.Matrix:
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

    return sp.Matrix.vstack(sp.Matrix.hstack(R, sp.zeros(3, 3)),
                            sp.Matrix.hstack(p_tilde * R, R))


def inv_SE3(T: sp.Matrix) -> sp.Matrix:
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

    return R_p_to_SE3(R.T, -R.T * p)


def R_p_to_SE3(R: sp.Matrix, p: sp.Matrix) -> sp.Matrix:
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
    return sp.Matrix.vstack(sp.Matrix.hstack(R, p),
                            sp.Matrix([[0, 0, 0, 1]]))
