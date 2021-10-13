"""
.. rubric:: ``modern_robotics.num.gen``

This submodule contains convenient functions to generate transformation
matrices.

"""

import numpy as np
import modern_robotics.num as mr


def TRx(theta: float) -> np.array:
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

            >>> import numpy as np
            >>> import modern_robotics.num as mr
            >>> mr.gen.TRx(np.pi/3)
            array([[ 1.       ,  0.       ,  0.       ,  0.       ],
                   [ 0.       ,  0.5      , -0.8660254,  0.       ],
                   [ 0.       ,  0.8660254,  0.5      ,  0.       ],
                   [ 0.       ,  0.       ,  0.       ,  1.       ]])

    See Also:
        :py:func:`TRy`
        :py:func:`TRz`
    """
    return mr.vec_to_SE3(np.array([[1, 0, 0, 0, 0, 0]]).T, theta)


def TRy(theta: float) -> np.array:
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

            >>> import numpy as np
            >>> import modern_robotics.num as mr
            >>> mr.gen.TRy(np.pi/3)
            array([[ 0.5      ,  0.       ,  0.8660254,  0.       ],
                   [ 0.       ,  1.       ,  0.       ,  0.       ],
                   [-0.8660254,  0.       ,  0.5      ,  0.       ],
                   [ 0.       ,  0.       ,  0.       ,  1.       ]])

    See Also:
        :py:func:`TRx`
        :py:func:`TRz`
    """
    return mr.vec_to_SE3(np.array([[0, 1, 0, 0, 0, 0]]).T, theta)


def TRz(theta: float) -> np.array:
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

            >>> import numpy as np
            >>> import modern_robotics.num as mr
            >>> mr.gen.TRz(np.pi/3) 
            array([[ 0.5      , -0.8660254,  0.       ,  0.       ],
                   [ 0.8660254,  0.5      ,  0.       ,  0.       ],
                   [ 0.       ,  0.       ,  1.       ,  0.       ],
                   [ 0.       ,  0.       ,  0.       ,  1.       ]])

    See Also:
        :py:func:`TRx`
        :py:func:`TRy`
    """
    return mr.vec_to_SE3(np.array([[0, 0, 1, 0, 0, 0]]).T, theta)


def Tt(t: np.array = None, x: float = 0., y: float = 0., z: float = 0.) \
        -> np.array:
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

            >>> import numpy as np
            >>> import modern_robotics.num as mr
            >>> mr.gen.Tt(np.array([[1], [2], [3]]))
            array([[1., 0., 0., 1.],
                   [0., 1., 0., 2.],
                   [0., 0., 1., 3.],
                   [0., 0., 0., 1.]])

        .. code-block:: python

            >>> import numpy as np
            >>> import modern_robotics.num as mr
            >>> mr.gen.Tt(y=2, z=6)
            array([[1., 0., 0., 0.],
                   [0., 1., 0., 2.],
                   [0., 0., 1., 6.],
                   [0., 0., 0., 1.]])
        """

    if t is None:
        t = np.array([[x], [y], [z]])

    return mr.R_p_to_SE3(np.eye(3), t)
