Transducers
===========

We have seen ideal components that treat power and energy in a certain way in their own power domains, which had a single *power bond* to other components. In the components we have seen so far, we sometimes treated flow and effort as in- and output signals because there was only one bond to take into account. In this session we will see how to handle components that can have multiple bonds.

It becomes really interesting if we have a look at components that transform power *between* domains, components that have two bonds. We call these components *transducers*. Take for example an electric DC motor, which transforms electrical power into rotational mechanical power, or a rack and pinion system that transforms rotational mechanical power into translational mechanical power. Of course, these non-ideal components have some other dynamic behaviour. An electric DC motor has some internal resistance and internal inductance. A lubricated rack and pinion system has some viscous friction, the pinion has some inertia, and the rack has some mass, possibly there is even some hysteresis present (we will not treat hysteresis in this course, but you can read more on it `here <https://en.wikipedia.org/wiki/Hysteresis>`_).

.. figure:: https://upload.wikimedia.org/wikipedia/commons/6/68/Rack_and_pinion_animation.gif
  :width: 200px

  Rack and pinion animation. `Source <https://upload.wikimedia.org/wikipedia/commons/6/68/Rack_and_pinion_animation.gif>`__.

.. figure:: https://upload.wikimedia.org/wikipedia/commons/8/89/Electric_motor.gif
  :width: 200px

  Electric DC motor animation. `Source <https://upload.wikimedia.org/wikipedia/commons/8/89/Electric_motor.gif>`__.

For the sake of modelling, we can extract the non-ideal dynamics from the component to make it an ideal transducer. These ideal transducers have a single parameter that describes the relation between input power variables (flow and effort) and output power variables, and they come in two flavours which are best explained with the examples from above.


Transformers
------------

Let's start with the rack and pinion, assuming that the pinion is driving the movement. The input power therefore is rotational mechanical, and the output power is linear mechanical. The parameter that describes the relation between input- and output power is the radius of the pinion, typically denoted :math:`r`. We know that both input- and output power should be equal, because the system does not add or store energy. The input power consists of a torque :math:`\tau` and an angular velocity :math:`\omega`. The output power consists of a force :math:`f` and a linear velocity :math:`v`. If the pinion has a radius of :math:`r=0.2\Unit{m}` and moves at :math:`\omega=3\Unit{rad \cdot s^{-1}}`, we know that the rack will move with:

.. math::

  v=r \omega=0.6\Unit{m \cdot s^{-1}}

This, together with the fact that power should remain equal we can determine the relation between torque and force:

.. math::

  P_l = P_r \Rightarrow f v = \omega \tau

Substitute :math:`v=r\omega`:

.. math::

  \begin{align*}
    f r \omega &= \omega \tau \\
    f r &= \tau \\
    f &= \frac{1}{r} \tau
  \end{align*}

So the ideal rack and pinion will have the following equations for transforming power:

.. math::

  \begin{align*}
    v &= r \omega \\
    f &= \frac{1}{r} \tau
  \end{align*}

Where :math:`r` is the reference radius of the pinion. Note that there is no storage of energy, only a scaling between the power variables of the two bonds. This kind of transducer is called *transformer*, and examples are:

* Lever: translational mechanical :math:`\rightarrow` rotational mechanical, transformation ratio is the length of the lever.
* Gearbox: rotational mechanical :math:`\rightarrow` rotational mechanical, transformation ratio is the ratio between the teeth of the gears.
* Pair of hydraulic cylinders: hydraulic :math:`\rightarrow` hydraulic, transformation ratio is the ratio between the area of the cylinders that is actuated by the fluid.
* Transformator: (AC) electrical :math:`\rightarrow` (AC) electrical, transformation ratio is the ratio between the number of windings of both sides.

Because the ideal transformer has two bonds, both of those bonds have a causality setting. Moreover, because a component cannot impose both an effort and a flow on a single bond, the two bonds of the transformer should have opposite causality. The dynamic equations therefore generalize to:

.. math::

  \begin{align*}
    e_1 &= n e_2 \\
    f_2 &= n f_1 \\
  \end{align*}

Or:

.. math::

  \begin{align*}
    e_2 &= \frac{1}{n} e_1 \\
    f_1 &= \frac{1}{n} f_2 \\
  \end{align*}

Where :math:`e_i` and :math:`f_i` are the effort and flow of bond :math:`i`, and :math:`n` is the transformation ratio. In the figures below you can find the block diagram representations of these two options.


.. figure:: /_static/figures/session6/block_diagrams_ideal_components/block_diagrams_ideal_components-005.svg

  Block diagram representation of the dynamic behaviour of an ideal transformer where bond :math:`1` has effort-out causality and bond :math:`2` has flow-out causality.

.. figure:: /_static/figures/session6/block_diagrams_ideal_components/block_diagrams_ideal_components-006.svg

  Block diagram representation of the dynamic behaviour of an ideal transformer where bond :math:`1` has flow-out causality and bond :math:`2` has effort-out causality.


Example
~~~~~~~

Let's look at a mechanical system that is driven by an ideal torque source. The mechanical power is transformed by a transmission, and used to rotate a cable drum whose cable is pulling on a mass.

.. figure:: /_static/figures/session7/cable_drum_example/cable_drum_example-001.svg

  Iconic diagram representation of a torque source driving a pulley system that pulls on a mass.

First we have to look for causality. Since we have a fixed effort-out causality of the torque source, and a preferred flow-out causality of the mass. The causality of the source can be propagated through the two transformers, the transmission and the cable drum. There it imposes an effort-in causality on the mass, which is its preferred causality so that's fine.

We consider the following parameters:

.. math::

  \begin{align*}
    \tau &= 1 \Unit{N \cdot m}, &
    m &= 1 \Unit{kg}, &
    i &= 0.1 \Unit{-}, &
    r &= 2 \Unit{m}
  \end{align*}

Note that the transmission is a transformer that does not change the domain of the power, it only redistributes the energy between torque and angular velocity, therefore its parameter (:math:`i`) is unitles. The cable drum however transforms the rotational mechanical power to translational mechanical power. For this example we assume that the mass is sliding over a frictionless surface, perpendicular to the direction of gravity (so we can ignore gravity).

This results in the following block diagram, where :math:`n_1 =i`, :math:`n_2=r`, :math:`I=m`, and :math:`e_s=\tau`.

.. figure:: /_static/figures/session7/cable_drum_example/cable_drum_example-002.svg

  Block diagram representation of a torque source driving a pulley system that pulls on a mass.

Now since we know that :math:`\frac{1}{n}\Int{x}=\Int{\frac{1}{n}x}` if :math:`n` is constant, if we apply that to our block diagram, we can 'pull' both the top :math:`\frac{1}{n}`'s through the integrator, and combine them with the bottom :math:`\frac{1}{n}`'s and the :math:`\frac{1}{I}` block to get a single :math:`\frac{1}{n_1^2 n_2^2 I}` block, as seen in the figure below.

.. figure:: /_static/figures/session7/cable_drum_example/cable_drum_example-003.svg

  Alternative simplified block diagram representation of a torque source driving a pulley system that pulls on a mass.

If we look at the units of that particular block:

.. math::

  \begin{align*}
    \frac{1}{n_1^2\Unit{-} n_2^2\Unit{m^2} I\Unit{kg}} =
    \frac{1}{(n_1^2 n_2^2 I) \Unit{kg \cdot m^2}} =
    \frac{1}{I^* \Unit{kg \cdot m^2}}
  \end{align*}

Apparently the new block now represents an inertia :math:`I^*= n_1^2 n_2^2 m \Unit{kg \cdot m^2 }`. So from the perspective of the torque source, the mass and transformers can be combined to a single inertia.


Gyrators
--------

Now let's look at the electric DC motor. We only look at the relation between electrical power and rotational mechanical power, for sake of an ideal component ignoring other dynamics such as inductance of the coils, resistance, axis inertia, etc. because these can be added later and represented by the components we have seen in the previous lesson.

The following equations describe these relations:

.. math::

  \begin{align*}
    \tau \Unit{N \cdot m} &= k_t \Unit{N \cdot m \cdot A^{-1}} i \Unit{A} \\
    u \Unit{V} &= k_e \Unit{V \cdot s \cdot rad^{-1}} \omega \Unit{rad \cdot s^{-1}}
  \end{align*}

Where :math:`k_t` is the electric motor's torque constant, and :math:`k_e` is the electric motor's back EMF constant (both not to be mistaken with the motor constant, commonly denoted with :math:`k_m`). These constants are typically found in the component's datasheet. Note the units of both constants, since :math:`\Unit{N \cdot m} = \Unit{J}`, and :math:`\Unit{A} = \Unit{C \cdot s^{-1}}`, then :math:`\Unit{N \cdot m \cdot A^{-1}}=\Unit{J \cdot s \cdot {C}^{-1}}=\Unit{V \cdot s}`, therefore the units of both constants are the same, and because of power continuity, their values are too.

Note how, in contrary to the transformer, the equations now relate the *effort* of one bond (:math:`\tau`, :math:`u`), to the *flow* (:math:`\omega`, :math:`i`) of the other bond. We generalize these components as *gyrators*. Examples are:

* electric DC motor: electrical :math:`\rightarrow` rotational mechanical, gyration ratio is the motor's torque constant, which is equal to the back EMF constant.
* centrifugal pump: rotational mechanical :math:`\rightarrow` hydraulic, gyration ratio is related to the pump's maximum head.

Similar to the transformer, the gyrator has two bonds, which both have a causality setting. Contrary to the transform, these causalities for both bonds are the same, because the relations are between flow and effort, and not between effort and effort, and flow and flow. This is also due to the fact that a component cannot impose both effort and flow on a single bond. The dynamic equations of a gyrator therefore are:

.. math::

  \begin{align*}
    e_1 &= r f_2 \\
    e_2 &= r f_1
  \end{align*}

Or:

.. math::

  \begin{align*}
    f_1 &= \frac{1}{r} e_2 \\
    f_2 &= \frac{1}{r} e_1
  \end{align*}


Where again :math:`e_i` and :math:`f_i` are the effort and flow of bond :math:`i`, and :math:`r` is the gyrator ratio. In the figures below you can find the block diagram representations of these two options.

.. figure:: /_static/figures/session6/block_diagrams_ideal_components/block_diagrams_ideal_components-007.svg

  Block diagram representation of the dynamic behaviour of an ideal gyrator where both bonds have effort-out causality.

.. figure:: /_static/figures/session6/block_diagrams_ideal_components/block_diagrams_ideal_components-008.svg

  Block diagram representation of the dynamic behaviour of an ideal gyrator where both bonds have flow-out causality.


Example
~~~~~~~

By means of an example, let's attach an ideal inertia component to a electric DC motor, which in turn is connected to a current source, as shown in the figure below.

.. figure:: /_static/figures/session7/dc_motor_example/dc_motor_example-001.svg

  Iconic diagram of an ideal inertia connected to a DC motor, in turn powered by a current source.

The current source can be modelled as flow source, the DC motor as a two-bond gyrator, and the inertia as a generalized inertia component. Because the flow source has a fixed flow-out causality, both bonds of the gyrator will have effort-out (flow-in) causality. The result is that the inertia also has flow-out causality, which fortunately is its preferred causality.

.. figure:: /_static/figures/session7/dc_motor_example/dc_motor_example-002.svg

  Block diagram representation of the iconic diagram shown in the figure above.

With the above block diagram, we can simulate the behaviour of the system. We assume the following parameter values (note that :math:`f_s` is dependent on time :math:`t`):

.. math::

  \begin{align*}
    I &= 2 \Unit{kg \cdot m^2}, &
    p_0 &= 0 \Unit{N \cdot m \cdot s}, &
    r &= 2 \Unit{N \cdot m \cdot A^{-1}}, &
    f_s(t) &=
    \begin{cases}
      \phantom{-}1 \Unit{A}, & 1 < t \leq 4 \\
      -1 \Unit{A}, & 4 < t \\
      \phantom{-}0 \Unit{A}, & \text{otherwise}
    \end{cases}
  \end{align*}

This will result in the following response:

.. figure:: /_static/figures/session6/responses/responses-002.svg

  Response of an ideal inertia, actuated by a DC motor, powered by an ideal current source.

Now since we know that :math:`r\Int{x}=\Int{rx}` if :math:`r` is constant, if we apply that to our block diagram, we can 'pull' the bottom :math:`r` through the integrator, and combine it with the top :math:`r` and the :math:`\frac{1}{I}` blocks to get a single :math:`\frac{r^2}{I}` block, as seen in the figure below.

.. figure:: /_static/figures/session7/dc_motor_example/dc_motor_example-004.svg

  Alternative block diagram representation of the block diagram shown in the figure above.

.. figure:: /_static/figures/session7/dc_motor_example/dc_motor_example-005.svg

  Block diagram representation of an ideal capacitor connected to an ideal current source.

This looks identical to a capacitor with :math:`C=\frac{I}{r^2}` connected to an ideal current source. It seems that if we look at the inertia *through* the gyrator, we observe the behaviour of the inertia's dual, a capacitance.
