function T = Tt(varargin)

p = inputParser;
addOptional(p, 't', NaN);
addParameter(p, 'x', 0);
addParameter(p, 'y', 0);
addParameter(p, 'z', 0);

parse(p, varargin{:});
a = p.Results;

if isnan(a.t)
    a.t = [a.x; a.y; a.z];
end
T = [eye(3), a.t; 0, 0, 0, 1];
end