function v = little_so3_to_vec(v_tilde)
% Reconstruct a 3 vector from its skew-symmetric matrix form. No check is
% performed to see if v_tilde is really skew-symmetric.
% 
% Args:
%     v_tilde: 3 by 3 skew-symmetric matrix form of v,
%              :math:`\TildeSkew{v}`.
% 
% Returns:
%     3 vector.
% 
% See Also:
%     :mat:func:`vec_to_so3`

v = [v_tilde(3, 2);
     v_tilde(1, 3);
     v_tilde(2, 1)];
end