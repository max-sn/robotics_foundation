function T = TRz(theta)
% Creates a transformation matrix with a single rotation around the
% :math:`z`-axis.
%
% Args:
%     theta: Angle to rotate with around :math:`z`, in radians.
% 
% Returns:
%     Homogeneous transformation matrix with :math:`z`-rotation and zero
%     translation.
%
% Example:
%     .. code-block:: matlab
%       
%       >> MR.gen.TRx(pi/6)
%
%       ans =
%
%           0.8660   -0.5000         0         0
%           0.5000    0.8660         0         0
%                0         0    1.0000         0
%                0         0         0    1.0000
%
% See Also:
%     :mat:func:`TRx`
%     :mat:func:`TRy`

T = MR.vec_to_SE3([0;0;1;0;0;0], theta);

end

