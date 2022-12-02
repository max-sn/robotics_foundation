function Tinv = inv_SE3(T)
% Inverts the transformation matrix T.
% 
% .. math::
% 
%     \HomogeneousTransformationMatrix =
%     \begin{bmatrix}
%     \RotationMatrix & p \\
%     0 & 1
%     \end{bmatrix}\in\SEthree
%     \quad\Rightarrow\quad
%     \HomogeneousTransformationMatrix^{-1} =
%     \begin{bmatrix}
%     \RotationMatrix\Transposed & -\RotationMatrix\Transposed p \\
%     0 & 1
%     \end{bmatrix}\in\SEthree
% 
% Args:
%     T: 4 by 4 homogeneous transformation matrix
%        :math:`\HomogeneousTransformationMatrix \in \SEthree`
% 
% Returns:
%     4 by 4 inverse of the homogeneous transformation matrix
%     :math:`\HomogeneousTransformationMatrix^{-1} \in \SEthree`

R = T(1:3,1:3);
p = T(1:3,4);
Tinv = [R', -R'*p; 0, 0, 0, 1];
end