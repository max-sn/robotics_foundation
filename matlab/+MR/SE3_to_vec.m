function V = SE3_to_vec(T)
% 'Differentiation' of a transformation matrix by using the matrix log of
% its rotation matrix to determine the screw velocity vector (twist) that
% reaches this transformation in unit time.
% 
% Args:
%     T: Homogeneous transformation matrix
% 
% Returns:
%     Velocity twist vector :math:`\Twist` with length :math:`\theta`
% 
% See Also:
%     :mat:func:`vec_to_SE3`
R = T(1:3, 1:3);
p = T(1:3, 4);

if max(abs(T - eye(4))) < 1e-5
    % If T is equal to identity (to precision), the screw axis is
    % undefined and the distance travelled along the screw axis is 0.
    omega_hat = NaN(3, 1);
    v = NaN(3, 1);
    theta = 0;
else
    if max(abs(R - eye(3))) < 1e-5
        % If the rotational part of T (the rotation matrix) is equal to
        % identity (to precision), the screw axis is purely translational,
        % i.e. the pitch is infinite.
        omega_hat = zeros(3, 1);
        theta = norm(p);
        v = p / theta;
    else
        omega = MR.SO3_to_vec(R);
        theta = norm(omega);
        omega_hat = omega / theta;
        if max(abs(p)) < 1e-5
            % If the translational part is zero, the screw axis is purely
            % angular, i.e. the pitch is zero.
            v = zeros(3, 1);
        else
            omega_tilde = MR.vec_to_little_so3(omega_hat);
            v = (1/theta * eye(3) - 1/2 * omega_tilde ...
                 + (1/theta - 1/2 / tan(theta/2)) ...
                 * omega_tilde * omega_tilde) * p;
        end
    end
end

% Screw axis
S = [omega_hat; v];

V = S * theta;
    
end

