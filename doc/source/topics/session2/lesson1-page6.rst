Twists (part 1 of 2)
====================

Twists, and their dual: wrenches, are six dimensional generalizations of the velocity and force that we already know. Their definition is based on screw theory, which says that any rigid body velocity can be described an instantaneous velocity along a screw axis.

.. raw:: html

  <iframe style="width: 695px; height: 390px;" src="https://www.youtube-nocookie.com/embed/mvGZtO_ruj0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

The video goes fairly quickly and only briefly mentions that the linear velocity part of a twist is actually the linear velocity of a point that is rigidly attached to the rigid body, so it moves with the rigid body, but is placed at the origin of the reference frame used to express the twist. This particular point is often a source of confusion, since the linear velocity is not expressed as linear velocity of for example the center of mass of the rigid body, which would be the intuitive choice. This intuitive choice has the downside that it is not a geometrical entity and therefore is dependent on the choice of reference. The linear velocity part embedded in the twist, however, *is* a geometrical entity and therefore is independent of choice of reference frame.

.. warning::

  Note that that does not mean that the coordinates used to *express* the twist are not dependent of the choice of reference.


Twists (part 2 of 2)
====================

.. raw:: html

  <iframe style="width: 695px; height: 390px;" src="https://www.youtube-nocookie.com/embed/VTv0qmLNvjg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

To change the frame of reference for a twist, which is :math:`6 \times 1`, we need a :math:`6 \times 6` matrix. The adjoint representation of the transformation matrix (often referred to as the 'big adjoint', we will see later what the 'little adjoint' is) can be used for that:

.. math::

  \HomogeneousTransformationMatrix =
  \begin{bmatrix}
    \RotationMatrix & p \\
    0 & 1
  \end{bmatrix},\quad
  \Adjoint{\HomogeneousTransformationMatrix} :=
  \begin{bmatrix}
    \RotationMatrix & 0 \\
    \TildeSkew{p}\RotationMatrix & \RotationMatrix
  \end{bmatrix} \in \mathbb{R}^{6\times6}

Where we use the skew-symmetric matrix notation of :math:`p` in the lower left entry.

Given this adjoint representation, we can transform a twist:

.. math::

  \To{a}{\Twist} = \Adjoint{\FromTo{b}{a}{\HomogeneousTransformationMatrix}} \To{b}{\Twist}

Similar to the angular velocity, we want to have a matrix form for the twist such that we can use it for the matrix exponential. Again where the bracket notation is used in the video, we use the tilde notation to prevent ambiguity with the matrix brackets. Recall that for angular velocity we had:

.. math::

  \begin{align*}
    \To{b}{\TildeSkew{\omega}} &= \RotationMatrix^{-1}\dot{\RotationMatrix}\in \sothree \\
    \To{S}{\TildeSkew{\omega}} &= \dot{\RotationMatrix}\RotationMatrix^{-1}\in \sothree
  \end{align*}

With these equations we can find that:

.. math::

  \begin{align*}
    \To{b}{\TildeSkew{\Twist}} &= \HomogeneousTransformationMatrix^{-1} \dot{\HomogeneousTransformationMatrix} =
    \begin{bmatrix}
      \To{b}{\TildeSkew{\omega}} & \To{b}{v} \\
      0 & 0
    \end{bmatrix} \in \sethree \\
    \To{s}{\TildeSkew{\Twist}} &= \dot{\HomogeneousTransformationMatrix} \HomogeneousTransformationMatrix^{-1} =
    \begin{bmatrix}
      \To{s}{\TildeSkew{\omega}} & \To{s}{v} \\
      0 & 0
    \end{bmatrix} \in \sethree
  \end{align*}