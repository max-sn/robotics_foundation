Notation
========

The notation used in the course Robotics Foundation and in this documentation is very specific. This section should shed some light on the used notation and the reasoning behind it.

Symbols
-------

The following symbols are used often.

.. list-table::
  :header-rows: 1
  :widths: 10 90
  :width: 100%

  * - Symbol
    - Description
  * - :math:`\CoorSys{\PHrule}`
    - Used to refer to a certain coordinate system.
  * - :math:`\Twist`
    - Twist, generalized velocity consisting of angular part and linear part.
  * - :math:`\Wrench`
    - Wrench, generalized force consisting of moment and linear force part.
  * - :math:`\UnitLength{\PHrule}`
    - Hat notation, indicates that the vector is of unit length. See also `Hat notation`_.
  * - :math:`\TildeSkew{\PHrule}`
    - Tilde notation, see `Tilde notation`_.
  * - :math:`\FromTo{\PHrule}{\PHrule}{\PHrule}`
    - Sub- and superscripts, see `Sub- and superscripts`_
  * - :math:`\wedge`
    - Cross product operator.
  * - :math:`\RotationMatrix`
    - Rotation matrix, :math:`\RotationMatrix \in \SOthree`.
  * - :math:`\HomogeneousTransformationMatrix`
    - Homogeneous transformation matrix, :math:`\HomogeneousTransformationMatrix \in \SEthree`.
  * - :math:`\Adjoint{\PHrule}`
    - Big adjoint of the transformation matrix :math:`\PHrule`. See `Big- and little adjoint`_.
  * - :math:`\LittleAdjoint{\PHrule}`
    - Little adjoint of the velocity twist :math:`\PHrule`. See `Big- and little adjoint`_.
  * - :math:`\PHrule\Transposed`
    - Transposed of matrix :math:`\PHrule`, obtained by flipping along the diagonal.
  * - :math:`\trace\PHrule`
    - Trace of matrix :math:`\PHrule`, obtained by summing the diagonal elements.
  * - :math:`\PHrule\PseudoInverse`
    - Pseudoinverse of the matrix :math:`\PHrule`. The matrix can be singular, or non-square.


Sub- and superscripts
---------------------

The entities used in this documentation can be roughly divided into two categories: transformations and others. For transformations we use the following notation:

.. math::

  \FromTo{\PH{y}}{\PH{x}}{\PH{A}}

In this, :math:`\PH{y}` indicates the target frame of reference, and :math:`\PH{x}` indicates the source frame of reference. The operator :math:`\PH{A}` indicates the type of transformation, and in this documentation we use rotation matrices :math:`\RotationMatrix`, and homogeneous transformation matrices :math:`\HomogeneousTransformationMatrix`. If the transformation in question is used to express a *configuration*, e.g. a rotation matrix used as orientation, :math:`\PH{x}` indicates the frame of in consideration, and :math:`\PH{y}` indicates the frame of reference. In other words, :math:`\FromTo{s}{b}{\RotationMatrix}` denotes the *orientation* of :math:`\CoorSys{s}` with respect to :math:`\CoorSys{b}`, i.e. expressed in :math:`\CoorSys{b}`.

For entities that fall in the 'other' category, such as twists, wrenches, positions, (angular) velocities, et cetera, we use the following notation:

.. math::

  \FromTo{\PH{b}}{\PH{a}}{\PH{V}}

Here :math:`\PH{a}` is always the frame of reference, i.e. the coordinate system in which the entity is expressed, regardless of the actual expression (skew-symmetric, tilde notation, row- or column array, etc.). On the other side, :math:`\PH{b}` does not denote a source frame, but can be used to distinguish the entity :math:`\PH{V}`. For example, if we require a certain wrench to get a rigid body moving, and it is expressed in the body frame, we could denote it as :math:`\FromTo{m}{b}{\Wrench}`. Similarly if that rigid-body is subjected to an external wrench, also expressed in the body frame, we can denote that as :math:`\FromTo{e}{b}{\Wrench}`. In this case we can still distinguish between the two.

For velocities, angular, linear, as well as twists, we could even introduce a third sub-/superscript:

.. math::

  \FromTo{\color{red}i}{\color{blue}k}{\Twist}^{\color{green}j}

In human language this would mean, the velocity twist of some frame :math:`\color{red}i`, relative to some frame :math:`\color{green}j`, expressed in some frame :math:`\color{blue}k`. In this documentation we will not use this notation, but for completeness it is included here.

In general the placing of these scripts is to ensure that multiplications are applied in the right order. If, for example, we would have the configuration of :math:`\CoorSys{b}` with respect to :math:`\CoorSys{a}`, and the configuration of :math:`\CoorSys{c}` with respect to :math:`\CoorSys{b}`, we could find the configuration of :math:`\CoorSys{c}` with respect to :math:`\CoorSys{a}` as follows:

.. math::
  
  \FromTo{\color{green}c}{\color{blue}a}{\HomogeneousTransformationMatrix} =
  \FromTo{\color{red}b}{\color{blue}a}{\HomogeneousTransformationMatrix}
  \FromTo{\color{green}c}{\color{red}b}{\HomogeneousTransformationMatrix}

Notice how the matching scripts (in red) are side-by-side, and drop out in the outcome.


Tilde notation
--------------

The tilde notation is used differently in two cases, for three vectors and for twists.

For three vectors such as point locations, (angular) velocities, etc. it is used as follows:

.. math ::
  
  v =
  \begin{bmatrix}
    {\color{red} v_1} \\ {\color{green} v_2} \\ {\color{blue} v_3}
  \end{bmatrix}
  \Rightarrow
  \TildeSkew{v} =
  \begin{bmatrix}
    0 & -{\color{blue} v_3} & {\color{green} v_2} \\
    {\color{blue} v_3} & 0 & -{\color{red} v_1} \\
    -{\color{green} v_2} & {\color{red} v_1} & 0
  \end{bmatrix}

Where the result is in the :math:`\sothree` space.

This is also called the 'skew-symmetric matrix notation' of a three vector. This can be used to easily calculate the cross product of two three vectors:

.. math::

  v \wedge w =
  \TildeSkew{v}w =
  \begin{bmatrix}
    v_2 w_3 - v_3 w_2 \\
    v_3 w_1 - v_1 w_3 \\
    v_1 w_2 - v_2 w_1
  \end{bmatrix}

For twists, the tilde notation is used as follows:

.. math ::

  \Twist =
  \begin{bmatrix}
    \omega \\ v
  \end{bmatrix}
  \Rightarrow
  \TildeSkew{\Twist} =
  \begin{bmatrix}
    \TildeSkew{\omega} & v \\
    0 & 0
  \end{bmatrix}

Where the result is the 4 by 4 times matrix that is in the :math:`\sethree` space.


Hat notation
------------

The hat accent indicates that vectors are of unit length, meaning that their Euclidean norm is equal to 1. For a three vector that would mean:

.. math::
  
  \UnitLength{v} \Rightarrow \sqrt{v_1^2 + v_2^2 + v_3^2} = 1

Note that the definition of a unit twist :math:`\UnitLength{\Twist}` is slightly different. A unit twist can be 'unit length' in two cases:

1. The angular velocity part of the twist is unit length. In that case the linear velocity part does not have to be unit length.

   .. math::

     \UnitLength{\Twist} =
     \begin{bmatrix}
     \UnitLength{\omega} \\ v
     \end{bmatrix}

2. In the second case the angular velocity part of the twist is zero, in that case the linear velocity part is unit length:
   
   .. math::

     \UnitLength{\Twist} =
     \begin{bmatrix}
     0 \\ \UnitLength{v}
     \end{bmatrix}


Big- and little adjoint
-----------------------

Adjoint, or adjunction, is a term regularly used in mathematics to denote another form of a certain entity. In this set of documentation, we have the adjoint form of a homogeneous transformation matrix, referred to as the big adjoint, and denoted with :math:`\Adjoint{}`, and the adjoint form of a velocity twist vector, referred to as the little- or small adjoint, denoted with :math:`\LittleAdjoint{}`.

A general homogeneous transformation matrix is constructed from a rotation matrix :math:`\RotationMatrix` and translation vector :math:`p` as follows:

.. math::

  \HomogeneousTransformationMatrix =
  \begin{bmatrix}
  \RotationMatrix & p \\
  0 & 1 \\
  \end{bmatrix}

The big adjoint form of that rotation matrix is then constructed as follows:

.. math::

  \Adjoint{\HomogeneousTransformationMatrix} =
  \begin{bmatrix}
  \RotationMatrix & 0 \\
  \TildeSkew{p}\RotationMatrix & \RotationMatrix
  \end{bmatrix}

A general velocity twist is constructed from angular velocity and linear velocity as follows:

.. math::
  
  \Twist =
  \begin{bmatrix}
  \omega \\ V
  \end{bmatrix}

The little adjoint form of that velocity twist is then constructed as follows:

.. math::

  \LittleAdjoint{\Twist} =
  \begin{bmatrix}
  \TildeSkew{\omega} & 0 \\
  \TildeSkew{v} & \TildeSkew{\omega} 
  \end{bmatrix}
