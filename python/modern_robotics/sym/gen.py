"""
``modern_robotics.sym.gen``
===========================

This submodule contains convenient functions to generate transformation
matrices.

"""

import sympy as sp
import modern_robotics.sym as mr


def TRx(theta: float) -> sp.Matrix:
    """
    Creates a transformation matrix with a single rotation around the
    :math:`x`-axis.

    Args:
        theta: Angle to rotate with around :math:`x`, in radians.

    Returns:
        Homogeneous transformation matrix with :math:`x`-rotation and zero
        translation.

    Example:
        .. code-block:: python

            >>> import sympy as sp
            >>> import modern_robotics.sym as mr
            >>> mr.gen.TRx(sp.pi/3)
            Matrix([
            [1,         0,          0, 0],
            [0,       1/2, -sqrt(3)/2, 0],
            [0, sqrt(3)/2,        1/2, 0],
            [0,         0,          0, 1]])

    See Also:
        :py:func:`TRy`
        :py:func:`TRz`
    """
    return mr.vec_to_SE3(sp.Matrix([1, 0, 0, 0, 0, 0]), theta)


def TRy(theta: float) -> sp.Matrix:
    """
    Creates a transformation matrix with a single rotation around the
    :math:`y`-axis.

    Args:
        theta: Angle to rotate with around :math:`y`, in radians.

    Returns:
        Homogeneous transformation matrix with :math:`y`-rotation and zero
        translation.

    Example:
        .. code-block:: python

            >>> import sympy as sp
            >>> import modern_robotics.sym as mr
            >>> mr.gen.TRy(sp.pi/3)
            Matrix([
            [       1/2, 0, sqrt(3)/2, 0],
            [         0, 1,         0, 0],
            [-sqrt(3)/2, 0,       1/2, 0],
            [         0, 0,         0, 1]])

    See Also:
        :py:func:`TRx`
        :py:func:`TRz`
    """
    return mr.vec_to_SE3(sp.Matrix([0, 1, 0, 0, 0, 0]), theta)


def TRz(theta: float) -> sp.Matrix:
    """
    Creates a transformation matrix with a single rotation around the
    :math:`z`-axis.

    Args:
        theta: Angle to rotate with around :math:`z`, in radians.

    Returns:
        Homogeneous transformation matrix with :math:`z`-rotation and zero
        translation.

    Example:
        .. code-block:: python

            >>> import sympy as sp
            >>> import modern_robotics.sym as mr
            >>> mr.gen.TRz(sp.pi/3)
            Matrix([
            [      1/2, -sqrt(3)/2, 0, 0],
            [sqrt(3)/2,        1/2, 0, 0],
            [        0,          0, 1, 0],
            [        0,          0, 0, 1]])

    See Also:
        :py:func:`TRx`
        :py:func:`TRy`
    """
    return mr.vec_to_SE3(sp.Matrix([0, 0, 1, 0, 0, 0]), theta)


def Tt(t: sp.Matrix = None, x: float = 0, y: float = 0, z: float = 0) \
        -> sp.Matrix:
    """
    Creates a transformation matrix with only a translational part.

    Args:
        t: Translation three vector. Should be a column vector. Optional, if
           omitted use one of the following to create ``t``.
        x: :math:`x`-coordinate of the translation. Optional and only used if
           ``t`` is not provided.
        y: :math:`y`-coordinate of the translation. Optional and only used if
           ``t`` is not provided.
        z: :math:`z`-coordinate of the translation. Optional and only used if
           ``t`` is not provided.

    Returns:
        Homogeneous transformation matrix without rotation, only translation.

    Examples:
        .. code-block:: python

            >>> import sympy as sp
            >>> import modern_robotics.sym as mr
            >>> mr.gen.Tt(sp.Matrix([1, 2, 3]))
            Matrix([
            [1, 0, 0, 1],
            [0, 1, 0, 2],
            [0, 0, 1, 3],
            [0, 0, 0, 1]])

        .. code-block:: python

            >>> import modern_robotics.sym as mr
            >>> mr.gen.Tt(y=2, z=6)
            Matrix([
            [1, 0, 0, 0],
            [0, 1, 0, 2],
            [0, 0, 1, 6],
            [0, 0, 0, 1]])
        """

    if t is None:
        t = sp.Matrix([[x], [y], [z]])

    return mr.R_p_to_SE3(sp.eye(3), t)
