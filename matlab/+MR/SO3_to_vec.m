function omega = SO3_to_vec(obj, R)
% 'Differentiation' of a rotation matrix by using the matrix log to
% determine the angular velocity that reaches that orientation in unit time.
%
% Args:
%     R: 3 by 3 rotation matrix :math:`\RotationMatrix \in \SOthree`.
%
% Returns:
%     Angular velocity vector :math:`\omega` with length
%     :math:`\theta`.
%
% See Also:
%     :mat:func:`so3_to_vec`
%     :mat:func:`vec_to_SO3`

% Check if R is identity
if max(abs(R - eye(size(R, 1)))) < 1e-5
    theta = 0;
    omega_hat = NaN(3, 1);
elseif abs(trace(R) + 1) < 1e-5
    theta = pi;
    if ~abs(R(3, 3) - 1) < 1e-5
        omega_hat = 1/(sqrt(2 * (1 + R(3, 3)))) * (R(:, 3) + [0; 0; 1]);
    elseif ~abs(R(2, 2) - 1) < 1e-5
        omega_hat = 1/(sqrt(2 * (1 + R(2, 2)))) * (R(:, 2) + [0; 1; 0]);
    elseif ~abs(R(1, 1) - 1) < 1e-5
        omega_hat = 1/(sqrt(2 * (1 + R(1, 1)))) * (R(:, 1) + [1; 0; 0]);
    end
else
    theta = acos((trace(R) - 1)/2);
    omega_hat_tilde = 1/(2 * sin(theta)) * (R - R');
    omega_hat = obj.little_so3_to_vec(omega_hat_tilde);
end

omega = omega_hat .* theta;
end