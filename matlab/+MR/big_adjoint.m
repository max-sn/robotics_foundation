function AdT = big_adjoint(T)
% Constructs the 'big adjoint' form of the transformation matrix T.
% 
% .. math::
% 
%     \HomogeneousTransformationMatrix =
%     \begin{bmatrix}
%     \RotationMatrix & p \\
%     0 & 1
%     \end{bmatrix}
%     \quad\Rightarrow\quad
%     \Adjoint{\HomogeneousTransformationMatrix} =
%     \begin{bmatrix}
%     \RotationMatrix & 0 \\
%     \TildeSkew{p}\RotationMatrix & \RotationMatrix
%     \end{bmatrix}
% 
% Args:
%     T: 4 by 4 homogeneous transformation matrix
%        :math:`\HomogeneousTransformationMatrix \in \SEthree`
% 
% Returns:
%     6 by 6 'big adjoint' form of the transformation matrix T
%
% Example:
%     .. code-block:: matlab
%
%        >> T = [eye(3), [1; 2; 3]; 0, 0, 0, 1];
%        >> MR.big_adjoint(T)
%        
%        ans =
%        
%             1     0     0     0     0     0
%             0     1     0     0     0     0
%             0     0     1     0     0     0
%             0    -3     2     1     0     0
%             3     0    -1     0     1     0
%            -2     1     0     0     0     1

R = T(1:3,1:3);
p = T(1:3,4);
p_tilde = MR.vec_to_little_so3(p);

AdT = [R, zeros(3); p_tilde*R, R];
end