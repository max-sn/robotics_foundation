function T = vec_to_SE3(S, theta)
% 'Integration' of a velocity twist to determine the configuration
% (expressed as transformation matrix) that this velocity twist reaches in
% unit time.
% 
% Args:
%     S: 6 vector velocity twist
%     theta: Distance travelled along the velocity twist screw axis
% 
% Returns:
%     4 by 4 homogeneous transformation matrix
%     :math:`\HomogeneousTransformationMatrix \in \SEthree`
% 
% See Also:
%     :mat:func:`SE3_to_vec`

omega = S(1:3);
v = S(4:end);

if all(abs(omega) < 1e-5)
    R = eye(3);
    p = v * theta;
else
    R = MR.vec_to_SO3(omega, theta);
    omega_tilde = MR.vec_to_little_so3(omega);
    p = (eye(3) * theta + (1 - cos(theta)) * omega_tilde ...
         + (theta - sin(theta)) ...
         * omega_tilde * omega_tilde) * v;
end

T = MR.R_p_to_SE3(R, p);

end