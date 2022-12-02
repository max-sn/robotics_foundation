function adV = little_adjoint(V)
% Constructs the 'little adjoint' form of the velocity twist V.
% 
% .. math::
% 
%     \Twist =
%     \begin{bmatrix}
%     \omega \\ v
%     \end{bmatrix}
%     \quad\Rightarrow\quad
%     \LittleAdjoint{\Twist} =
%     \begin{bmatrix}
%     \TildeSkew{\omega} & 0 \\
%     \TildeSkew{v} & \TildeSkew{\omega}
%     \end{bmatrix}
%
% Args:
%     V: 6 by 1 velocity twist
%
% Returns:
%     6 by 6 'little adjoint' form of the twist V
%
% Example:
%     .. code-block:: matlab
%
%         >> V = [1; 2; 3; 4; 5; 6];
%         >> MR.little_adjoint(V)
%
%         ans =
%
%              0    -3     2     0     0     0
%              3     0    -1     0     0     0
%             -2     1     0     0     0     0
%              0    -6     5     0    -3     2
%              6     0    -4     3     0    -1
%             -5     4     0    -2     1     0

w = V(1:3);
v = V(4:6);

adV = [MR.vec_to_little_so3(w), zeros(3);
       MR.vec_to_little_so3(v), MR.vec_to_little_so3(w)];
end

