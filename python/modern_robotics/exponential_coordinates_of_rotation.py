import numpy as np


def SO3_to_vec(R: np.array, unit_vec: bool = False) -> np.array:
    """
    'Differentiation' of a rotation matrix by using the matrix log to
    determine the angular velocity that reaches that orientation in unit time.

    Args:
        R (np.array): Rotation matrix
        unit_vec (bool): Whether or not to return the angular velocity as unit
                         vector, with its magnitude in a tuple.

    Returns:
        Either returns a single np.array :math:`\\omega` with length
        :math:`\\theta`, or a tuple with (:math:`\\hat{\\omega}`,
        :math:`\\theta`).
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

    if unit_vec:
        return omega, theta
    else:
        return omega * theta


def vec_to_SO3(omega: np.array, theta: float = None) -> np.array:
    """
    'Integration' of an angular velocity to determine the orientation
    (expressed as rotation matrix) that this angular velocity reaches in unit
    time.

    Uses Rodrigues' formula to solve the matrix exponential of the vector's
    skew-symmetric matrix form.

    Args:
        omega (np.array): 3 vector angular velocity. Can be unit length, in
                          that case theta should also be provided.
        theta (float):    Optional. If omitted, the Euclidean length of omega
                          is assumed to be theta.

    Returns:
        np.array: Rotation matrix R.
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
        v (np.array): 3 vector.

    Returns:
        np.array: 3 by 3 skew-symmetric matrix form of v.
    """
    return np.array([[0, -v.item(2), v.item(1)],
                     [v.item(2), 0, -v.item(0)],
                     [-v.item(1), v.item(0), 0]])


def so3_to_vec(v_tilde: np.array) -> np.array:
    """
    Reconstruct a 3 vector from its skew-symmetric matrix form. No check is
    performed to see if v_tilde is really skew-symmetric.

    Args:
        v_tilde (np.array): skew-symmetric matrix.

    Returns:
        np.array: 3 vector.
    """
    return np.array([[v_tilde.item(2, 1)],
                     [v_tilde.item(0, 2)],
                     [v_tilde.item(1, 0)]])
