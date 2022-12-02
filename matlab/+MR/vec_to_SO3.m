function R = vec_to_SO3(omega, theta)
% 'Integration' of an angular velocity to determine the orientation
% (expressed as rotation matrix) that this angular velocity reaches in unit
% time.
%
% Uses Rodrigues' formula to solve the matrix exponential of the vector's
% skew-symmetric matrix form.
%
% .. math::
%
%     \RotationMatrix =
%     \exp(\TildeSkew{\UnitLength{\omega}}\theta) =
%     I + \TildeSkew{\UnitLength{\omega}}\sin\theta +
%     \TildeSkew{\UnitLength{\omega}}^2(1-\cos\theta) \in \SOthree
%
% Args:
%     omega: 3 vector angular velocity. Can be unit length, in that case
%            theta should also be provided.
%     theta: If omitted, the Euclidean norm of omega is assumed to be theta.
%
% Returns:
%     3 by 3 rotation matrix :math:`\RotationMatrix \in \SOthree`.
%
% See Also:
%     :mat:func:`vec_to_so3`
%     :mat:func:`SO3_to_vec`

if ~exist('theta', 'var')
    theta = norm(omega);
    if theta < 1e-5
        R = eye(3);
        return
    end
    omega_hat = omega ./ theta;
else
    omega_hat = omega;
end
omega_hat_tilde = MR.vec_to_little_so3(omega_hat);
R = eye(3) + sin(theta) * omega_hat_tilde + (1 - cos(theta)) * omega_hat_tilde^2;
end
