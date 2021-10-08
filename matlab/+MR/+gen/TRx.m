function T = TRx(theta)
% Creates a transformation matrix with a single rotation around the
% :math:`x`-axis.
%
% Args:
%     theta: Angle to rotate with around :math:`x`, in radians.
% 
% Returns:
%     Homogeneous transformation matrix with :math:`x`-rotation and zero
%     translation.
%
% Example:
%     .. code-block:: matlab
%       
%       >> MR.gen.TRx(pi/6)
%
%       ans =
%
%           1.0000         0         0         0
%                0    0.8660   -0.5000         0
%                0    0.5000    0.8660         0
%                0         0         0    1.0000
%
% See Also:
%     :mat:func:`TRy`
%     :mat:func:`TRz`

T = MR.vec_to_SE3([1;0;0;0;0;0], theta);

end

