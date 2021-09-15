function v_tilde = vec_to_little_so3(v)
% Build a skew-symmetric matrix from a 3 vector.
% 
% Args:
%     v: 3 vector.
% 
% Returns:
%     3 by 3 skew-symmetric matrix form of v, :math:`\TildeSkew{v}`.
% 
% See Also:
%     :mat:func:`so3_to_vec`

v_tilde = [0, -v(3), v(2);
           v(3), 0, -v(1);
           -v(2), v(1), 0];
end