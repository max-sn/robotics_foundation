Angular velocity
================

.. raw:: html

  <iframe style="width: 695px; height: 390px;" src="https://www.youtube-nocookie.com/embed/zJJldJYMxVU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Even though we use a 9 variable rotation matrix to represent the 3D orientation, the angular velocity can be expressed by a 3D vector due to the topology of its space, which is 'flat'.

The bracket notation mentioned in the video above is also known as the skew-symmetric matrix notation of a three dimensional vector. In this course we will use the following notation with a tilde (:math:`\TildeSkew{}`) accent to prevent ambiguity with the brackets that we already use for matrices.

.. math::

  \begin{gather*}
    x \wedge y = \TildeSkew{x}y \\ \\
    x =
    \begin{bmatrix}
      x_1 \\ x_2 \\ x_3
    \end{bmatrix}
    \in\mathbb{R}^3,\quad
    \TildeSkew{x} :=
    \begin{bmatrix}
      0 & -x_3 & x_2 \\
      x_3 & 0 & -x_1 \\
      -x_2 & x_1 & 0
    \end{bmatrix} \in \sothree,\quad
    \TildeSkew{x} = - \TildeSkew{x}\Transposed
  \end{gather*}

With this notation defined, we can use it to more easily calculate the cross-product of three dimensional vectors.

For any combination of 3D rotations, it is always possible to describe it as a single rotation about a unit vector with a certain angle. The same applies to rotational velocity, or angular velocity, which can be described by a unit vector and a certain angular velocity. When a frame :math:`\CoorSys{b}` rotates around such a unit vector :math:`\UnitLength{\omega}` with angular velocity :math:`\dot{\theta}`, its axes (:math:`\UnitLength{x}_b`, :math:`\UnitLength{y}_b`, :math:`\UnitLength{z}_b`) have a resulting linear velocity. This linear velocity can be found with the cross product of the axis, and :math:`\dot{\theta}\UnitLength{\omega}=\omega`, e.g.:

.. math::

  \dot{\UnitLength{x}}_b = \omega \wedge \UnitLength{x}_b

At this point it does not yet matter in which coordinate frame we have expressed these vectors, provided that they are expressed in the same reference frame. The figure below shows how to draw this linear velocity of the x-axis, :math:`\dot{\UnitLength{x}}_b`.

.. figure:: /_static/figures/session2/angular_velocity_vector/angular_velocity_vector.svg

  How to construct the linear velocity of the x-axis of :math:`\CoorSys{b}`. Note that we are only interested in rotation between :math:`\CoorSys{s}` and :math:`\CoorSys{b}`, so you can assume that there is no translation between them. In the figure they are not drawn in the same location for clarity.

Using the tilde notation that we introduced above, we can write the change rate of :math:`\UnitLength{x}_b` as follows, and similarly for the other two axes:

.. math::

  \begin{align*}
    \dot{\UnitLength{x}}_b &= \TildeSkew{\omega}\UnitLength{x}_b \\
    \dot{\UnitLength{y}}_b &= \TildeSkew{\omega}\UnitLength{y}_b \\
    \dot{\UnitLength{z}}_b &= \TildeSkew{\omega}\UnitLength{z}_b
  \end{align*}

If we want to use coordinates to express these equations, we have to pick a coordinate frame in which to express the (unit) vectors. As always, any frame can be chosen, but it seems convenient to either use the (fixed) space frame :math:`\CoorSys{s}`, or the rotating body frame :math:`\CoorSys{b}`. Let us try the space frame first. If we only consider rotation, the orientation of :math:`\CoorSys{b}` with respect to :math:`\CoorSys{s}` can be described with :math:`\FromTo{b}{s}{\RotationMatrix}(t)`. Note the time dependency indicating that it changes with time. We know that the rotation matrix is composed of the axes of frame :math:`\CoorSys{b}`, expressed in :math:`\CoorSys{s}`:

.. math::

  \FromTo{b}{s}{\RotationMatrix} =
  \begin{bmatrix}
    \FromTo{b}{s}{\UnitLength{x}} &
    \FromTo{b}{s}{\UnitLength{y}} &
    \FromTo{b}{s}{\UnitLength{z}}
  \end{bmatrix}

If we take the time derivative on both sides of this equation, and we substitute the equations from above, we get:

.. math::

  \begin{align*}
    \FromTo{b}{s}{\dot{\RotationMatrix}} &=
    \begin{bmatrix}
      \FromTo{b}{s}{\dot{\UnitLength{x}}} &
      \FromTo{b}{s}{\dot{\UnitLength{y}}} &
      \FromTo{b}{s}{\dot{\UnitLength{z}}}
    \end{bmatrix} \\
    &=
    \begin{bmatrix}
      \To{s}{\TildeSkew{\omega}}\FromTo{b}{s}{\UnitLength{x}} &
      \To{s}{\TildeSkew{\omega}}\FromTo{b}{s}{\UnitLength{y}} &
      \To{s}{\TildeSkew{\omega}}\FromTo{b}{s}{\UnitLength{z}}
    \end{bmatrix} \\
    &=
    \To{s}{\TildeSkew{\omega}}
    \begin{bmatrix}
      \FromTo{b}{s}{\UnitLength{x}} &
      \FromTo{b}{s}{\UnitLength{y}} &
      \FromTo{b}{s}{\UnitLength{z}}
    \end{bmatrix}\\
    &=
    \To{s}{\TildeSkew{\omega}}
    \FromTo{b}{s}{\RotationMatrix}
  \end{align*}

So the change of orientation :math:`\FromTo{b}{s}{\dot{\RotationMatrix}}` is not simply the time derivative of the angular velocity :math:`\To{s}{\omega}`, it is also a function of the orientation :math:`\FromTo{b}{s}{\RotationMatrix}` itself, therefore it is a differential equation.

If we multiply both sides of the last equation with :math:`\FromTo{b}{s}{\RotationMatrix}\Transposed`, we get:

.. math::

  \FromTo{b}{s}{\dot{\RotationMatrix}}
  \FromTo{b}{s}{\RotationMatrix}\Transposed
  =
  \To{s}{\TildeSkew{\omega}}
  \underbrace{
  \FromTo{b}{s}{\RotationMatrix}
  \FromTo{b}{s}{\RotationMatrix}\Transposed
  }_{I_3}
  =
  \To{s}{\TildeSkew{\omega}}

We can find a similar expression for the angular velocity but now expressed in the body frame :math:`\CoorSys{b}`:

.. math::

  \FromTo{b}{s}{\RotationMatrix}\Transposed
  \FromTo{b}{s}{\dot{\RotationMatrix}}
  =
  \To{b}{\TildeSkew{\omega}}
