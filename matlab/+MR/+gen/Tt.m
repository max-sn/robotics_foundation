function T = Tt(varargin)
% Creates a transformation matrix with only a translational part.
%
%
% Args:
%     t: Translation three vector. Should be a column vector. Optional, if
%        omitted use one of the following to create ``t``. 
%     x: :math:`x`-coordinate of the translation. Optional and only used if
%        ``t`` is not provided.
%     y: :math:`y`-coordinate of the translation. Optional and only used if
%        ``t`` is not provided.
%     z: :math:`z`-coordinate of the translation. Optional and only used if
%        ``t`` is not provided.
%
% Returns:
%     Homogeneous transformation matrix without rotation, only translation.
%
% Examples:
%     .. code-block:: matlab
%
%       >> MR.gen.Tt([1;2;3])
%      
%       ans =
%
%            1     0     0     1
%            0     1     0     2
%            0     0     1     3
%            0     0     0     1
%
%     .. code-block:: matlab
%
%       >> MR.gen.Tt('y', 2, 'z', 6)
%
%       ans =
%
%            1     0     0     0
%            0     1     0     2
%            0     0     1     6
%            0     0     0     1



% Parse input arguments
p = inputParser;
addOptional(p, 't', NaN);
addParameter(p, 'x', 0);
addParameter(p, 'y', 0);
addParameter(p, 'z', 0);
parse(p, varargin{:});
a = p.Results;

% If t is not given as argument, use x, y, z and their default values.
if isnan(a.t)
    a.t = [a.x; a.y; a.z];
end

% Construct T
T = [eye(3), a.t; 0, 0, 0, 1];

end