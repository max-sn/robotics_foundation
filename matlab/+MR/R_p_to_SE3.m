function T = R_p_to_SE3(R, p)
% Constructs a homogeneous transformation matrix from a rotation matrix and
% displacement vector.
% 
% Args:
%     R: 3 by 3 rotation matrix :math:`\RotationMatrix\in\SOthree`
%     p: 3 by 1 displacement vector
% 
% Returns:
%     4 by 4 homogeneous transformation matrix
%     :math:`\HomogeneousTransformationMatrix \in \SEthree`

T = [R, p; 0, 0, 0, 1];
end