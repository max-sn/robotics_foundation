Forward kinematics example
==========================

The RRRP (three revolute joints, followed by a prismatic joint) arm, also commonly referred to as the SCARA arm, is used as an example in the video below to determine the forward kinematics, using both options for the product of exponentials (PoE) formulas shown in previous videos.

.. raw:: html

  <iframe style="width: 695px; height: 390px;" src="https://www.youtube-nocookie.com/embed/cKHsil0V6Qk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

In the video above, the instructor quickly shows an example for how to derive the forward kinematics of an RRRP robot arm, as shown in the figure below.

.. figure:: /_static/figures/session3/RRRP.png
  :width: 70%
  :align: center

  RRRP robot arm.

If we want to use the product of exponentials formula in the space frame, we need :math:`M`, and the joint screw axes expressed in the space frame :math:`\CoorSys{s}`. These were already derived in the video:

.. math::

  M =
  \begin{bmatrix}
    0 & -1 & 0 & 19 \\
    -1 & 0 & 0 & 0 \\
    0 & 0 & -1 & -3 \\
    0 & 0 & 0 & 1 \\
  \end{bmatrix}

.. math::

  \begin{align*}
    \Screw_1 &=
    \begin{bmatrix} 0 & 0 & 1 & 0 & 0 & 0 \end{bmatrix} \Transposed, &
    \Screw_{\omega,1} &=
    \begin{bmatrix} 0 & 0 & 1 \end{bmatrix}\Transposed, &
    \Screw_{v,1} &=
    \begin{bmatrix} 0 & 0 & 0 \end{bmatrix}\Transposed \\
    \Screw_2 &=
    \begin{bmatrix} 0 & 0 & 1 & 0 & -10 & 0 \end{bmatrix} \Transposed, &
    \Screw_{\omega,2} &=
    \begin{bmatrix} 0 & 0 & 1 \end{bmatrix}\Transposed, &
    \Screw_{v,2} &=
    \begin{bmatrix} 0 & -10 & 0 \end{bmatrix}\Transposed \\
    \Screw_3 &=
    \begin{bmatrix} 0 & 0 & 1 & 0 & -19 & 0 \end{bmatrix} \Transposed, & \Screw_{\omega,3} &=
    \begin{bmatrix} 0 & 0 & 1 \end{bmatrix}\Transposed, &
    \Screw_{v,3} &=
    \begin{bmatrix} 0 & -19 & 0 \end{bmatrix}\Transposed \\
    \Screw_4 &=
    \begin{bmatrix} 0 & 0 & 0 & 0 & 0 & 1 \end{bmatrix} \Transposed, &
    \Screw_{\omega,4} &=
    \begin{bmatrix} 0 & 0 & 0 \end{bmatrix}\Transposed, &
    \Screw_{v,4} &=
    \begin{bmatrix} 0 & 0 & 1 \end{bmatrix}\Transposed \\
  \end{align*}

Note that the notation of the screw axes is only transposed to make it more readable. They are still treated as column arrays.

Now to apply the product of exponentials formula, we need the scary-looking formula from the lesson about exponential coordinates of rigid-body motion, but we will go through it step-by-step.

.. math::

  \exp(\TildeSkew{\Screw}\theta) =
  \begin{cases}
    \begin{bmatrix}
      \exp(\TildeSkew{\Screw}_{\omega}\theta) & (I\theta + \TildeSkew{\Screw}_{\omega}(1 - \cos\theta) + \TildeSkew{\Screw}_{\omega}^2(\theta -\sin\theta)) \Screw_{v} \\ 0 & 1
    \end{bmatrix}, &
    \Norm{\Screw_{\omega}} = 1 \\
    \begin{bmatrix}
      I & \Screw_v \theta \\ 0 & 1
    \end{bmatrix}, &
    \Screw_{\omega} = 0,\; \Norm{\Screw_v} = 1
  \end{cases}

This equation must be found for all joints, and for every joint :math:`i`, the screw axis :math:`\Screw` will be substituted with the joint's screw axis :math:`\Screw_i`, and :math:`\theta` will be substituted with the joint's generalized coordinate: :math:`\GeneralizedCoordinate_i`. The full product of exponentials formula in the space frame for an :math:`n`-joint manipulator then becomes:

.. math::

  \FromTo{b}{s}{\HomogeneousTransformationMatrix}(\Configuration) = \exp(\TildeSkew{\Screw}_1 \GeneralizedCoordinate_1)\exp(\TildeSkew{\Screw}_2 \GeneralizedCoordinate_2) \cdots \exp(\TildeSkew{\Screw}_n \GeneralizedCoordinate_n)M

We start with :math:`\Screw_1`. We can see that :math:`\Norm{\Screw_{\omega,1}}=1`, and additionally that :math:`\Screw_{v,1}=0`. The exponential therefore is given by the first case in the equation above. The top left element of the matrix on the right is the exponential coordinate representation of rotation. From the lesson on exponential coordinates of rotation we know that:

.. math::

  \exp(\TildeSkew{\UnitLength{\omega}}\theta) = I_3 + \TildeSkew{\UnitLength{\omega}}\sin\theta + \TildeSkew{\UnitLength{\omega}}^2\left(1-\cos\theta\right)

In this equation we can substitute the unit angular velocity :math:`\TildeSkew{\UnitLength{\omega}}` by the angular velocity part of the joint screw axis (:math:`\Screw_\omega`), and the travelled 'distance' or 'angle' :math:`\theta` with the generalized coordinate of the joint: :math:`\GeneralizedCoordinate_i`.

.. math::

  \exp(\TildeSkew{\Screw}_{\omega,i} \GeneralizedCoordinate_i) = I_3 + \TildeSkew{\Screw}_{\omega,i}\sin \GeneralizedCoordinate_i + \TildeSkew{\Screw}_{\omega,i}^2\left(1-\cos \GeneralizedCoordinate_i\right)

Substituting gives:

.. math::

  \begin{align*}
    \exp(\TildeSkew{\Screw}_{\omega,1} \GeneralizedCoordinate_1) &=
    \begin{bmatrix}
      1 & 0 & 0 \\
      0 & 1 & 0 \\
      0 & 0 & 1
    \end{bmatrix} +
    \begin{bmatrix}
      0 & -1 & 0 \\
      1 & 0 & 0 \\
      0 & 0 & 0
    \end{bmatrix}
    \sin\GeneralizedCoordinate_1 +
    \begin{bmatrix} -1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 0 \end{bmatrix}
    (1 - \cos\GeneralizedCoordinate_1) \\
    &=
    \begin{bmatrix}
      \cos\GeneralizedCoordinate_1 & -\sin\GeneralizedCoordinate_1 & 0 \\
      \sin\GeneralizedCoordinate_1 & \cos\GeneralizedCoordinate_1 & 0 \\
      0 & 0 & 1
    \end{bmatrix}
  \end{align*}

Then on to the top-right element of the exponential coordinates representation of rigid-body motion. Again we substitute the proper matrix and vector for :math:`\Screw_v` and :math:`\TildeSkew{\Screw}_{\omega}`, and the generalized coordinate for :math:`\theta`. We can immediately see that :math:`\Screw_v=0`, effectively setting the entire term to zero.

For the first joint, the exponential representation therefore is:

.. math::

  \exp(\TildeSkew{\Screw}_1 \GeneralizedCoordinate_1) =
  \begin{bmatrix}
    \cos\GeneralizedCoordinate_1 & -\sin\GeneralizedCoordinate_1 & 0 & 0 \\
    \sin\GeneralizedCoordinate_1 & \cos\GeneralizedCoordinate_1 & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 1
  \end{bmatrix}

The second joint has the same angular velocity part of the joint screw axis, therefore the top-left part of the exponential representation will also be the same. The linear velocity part, however, is non-zero. Therefore we need to calculate the top-right part, let's call it :math:`B`. We can substitute the proper values for :math:`\Screw_v`, :math:`\TildeSkew{\Screw}_{\omega}`, and :math:`\theta` again:

.. math::

  \begin{align*}
    B &= \left( I\GeneralizedCoordinate_2 + \TildeSkew{\Screw}_{\omega,2}(1 - \cos\GeneralizedCoordinate_2) + \TildeSkew{\Screw}_{\omega,2}^2 (\GeneralizedCoordinate_2 - \sin\GeneralizedCoordinate_2) \right)\Screw_{v,2} \\
    &= \left(
      \begin{bmatrix}
        \GeneralizedCoordinate_2 & 0 & 0 \\
        0 & \GeneralizedCoordinate_2 & 0 \\
        0 & 0 & \GeneralizedCoordinate_2 \\
      \end{bmatrix} +
      \begin{bmatrix}
        0 & -1+\cos\GeneralizedCoordinate_2 & 0 \\
        1 - \cos\GeneralizedCoordinate_2 & 0 & 0 \\
        0 & 0 & 0 \\
      \end{bmatrix} +
      \begin{bmatrix}
        -\GeneralizedCoordinate_2 + \sin\GeneralizedCoordinate_2 & 0 & 0 \\
        0 & -\GeneralizedCoordinate_2 + \sin\GeneralizedCoordinate_2 & 0 \\
        0 & 0 & 0 \\
      \end{bmatrix}
    \right)
    \begin{bmatrix}
      0 \\ -10 \\ 0
    \end{bmatrix} \\
    &=
    \begin{bmatrix}
      \sin\GeneralizedCoordinate_2 & \cos\GeneralizedCoordinate_2 - 1 & 0 \\
      1 - \cos\GeneralizedCoordinate_2 & \sin\GeneralizedCoordinate_2 & 0 \\
      0 & 0 & \GeneralizedCoordinate_2
    \end{bmatrix}
    \begin{bmatrix}
      0 \\ -10 \\ 0
    \end{bmatrix} \\
    &=
    \begin{bmatrix}
      10 - 10\cos\GeneralizedCoordinate_2 \\
      -10\sin\GeneralizedCoordinate_2 \\
      0
    \end{bmatrix}
  \end{align*}

For the second joint, the exponential representation therefore is:

.. math::

  \exp(\TildeSkew{\Screw}_2 \GeneralizedCoordinate_2) =
  \begin{bmatrix}
    \cos\GeneralizedCoordinate_2 & -\sin\GeneralizedCoordinate_2 & 0 & 10 - 10\cos\GeneralizedCoordinate_2 \\
    \sin\GeneralizedCoordinate_2 & \cos\GeneralizedCoordinate_2 & 0 & -10\sin\GeneralizedCoordinate_2\\
    0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 1
  \end{bmatrix}

Similarly we can determine the third joint:

.. math::

  \exp(\TildeSkew{\Screw}_3 \GeneralizedCoordinate_3) =
  \begin{bmatrix}
    \cos\GeneralizedCoordinate_3 & -\sin\GeneralizedCoordinate_3 & 0 & 19 - 19\cos\GeneralizedCoordinate_3 \\
    \sin\GeneralizedCoordinate_3 & \cos\GeneralizedCoordinate_3 & 0 & -19\sin\GeneralizedCoordinate_3\\
    0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 1
  \end{bmatrix}

The final joint is slightly different. We can use the less complex case, because for the last joint :math:`\Screw_{\omega,4}=0` because it is a prismatic joint. It is clear to see that the transformation of joint 4 is:

.. math::

  \exp(\TildeSkew{\Screw}_4 \GeneralizedCoordinate_4) =
  \begin{bmatrix}
    1 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 \\
    0 & 0 & 1 & \GeneralizedCoordinate_4 \\
    0 & 0 & 0 & 1 \\
  \end{bmatrix}

Finally to find the forward kinematics, expressed in the :math:`\CoorSys{s}` frame, we concatenate the found link transformations and :math:`M`:

.. math::

  \begin{align*}
    \FromTo{b}{s}{\HomogeneousTransformationMatrix}(\Configuration) &=
    \exp(\TildeSkew{\Screw}_1 \GeneralizedCoordinate_1) \exp(\TildeSkew{\Screw}_2 \GeneralizedCoordinate_2) \exp(\TildeSkew{\Screw}_3 \GeneralizedCoordinate_3) \exp(\TildeSkew{\Screw}_4 \GeneralizedCoordinate_4) M \\
    &=
    \begin{bmatrix}
      \ShortCos{123} & -\ShortSin{123} & 0 & 10\ShortCos{1} - 9\ShortCos{12} - 19\ShortCos{123} \\
      \ShortSin{123} & \ShortCos{123} & 0 & 10\ShortSin{1} - 9\ShortSin{12} - 19\ShortSin{123} \\
      0 & 0 & 0 & 1
    \end{bmatrix}
    \begin{bmatrix}
      0 & -1 & 0 & 19 \\
      -1 & 0 & 0 & 0 \\
      0 & 0 & -1 & -3 \\
      0 & 0 & 0 & 1
    \end{bmatrix} \\
    &=
    \begin{bmatrix}
      \ShortSin{123} & -\ShortCos{123} & 0 & 9\ShortCos{12} + 10\ShortCos{1} \\
      -\ShortCos{123} & -\ShortSin{123} & 0 & 9\ShortSin{12} + 10\ShortSin{1} \\
      0 & 0 & -1 & \GeneralizedCoordinate_4 - 3 \\
      0 & 0 & 0 & 1 \\
    \end{bmatrix}
  \end{align*}

Where we use the common shorthands :math:`\ShortSin{123}=\sin(\GeneralizedCoordinate_1 + \GeneralizedCoordinate_2 + \GeneralizedCoordinate_3)` and :math:`\ShortCos{123}=\cos(\GeneralizedCoordinate_1 + \GeneralizedCoordinate_2 + \GeneralizedCoordinate_3)`.
