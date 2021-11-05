.. role:: quote-lecturer
  :class: quote-lecturer

.. role:: quote-student
  :class: quote-student

Generic behaviour
=================

In the previous lesson we saw some examples of cross-domain power exchanges. In this lesson we will see that the behaviour of ideal components in those domains is very comparable and can even be generalized with generic components.

Ideal in this context means that their dynamic behaviour is described with a single parameter (which can still be multi-dimensional but we will look at one-dimensional first), e.g. an ideal spring only has compliance, but no mass or damping. An ideal damper only has damping, no mass or compliance, etc. Similar for ideal electrical components, an ideal capacitor has no resistance or inductance, and an ideal inductor has no resistance or capacitance. In most cases, non-ideal components can be composed of several ideal components.

Generalized inertance
---------------------

The first behaviour type we will have a look at is the behaviour of inheritances, or I-elements.

Let's have a look at the behaviour of an ideal mass for example. From Newton's second law we know that when a force :math:`f` is applied to the mass :math:`\Mass`, it will result in an acceleration :math:`a` following :math:`f=\Mass a`, or :math:`a=\frac{f}{\Mass}`. Knowing that acceleration is the rate of change of velocity in time, we can rewrite this to:

.. math::

  f \Unit{N} = \Mass \Unit{kg} \cdot \Diff{v} \Unit{m \cdot s^{-2}}

In the rotational mechanical domain, this translates one-to-one to:

.. math::

  \tau \Unit{N \cdot m} = I \Unit{kg \cdot m^2} \cdot \Diff{\omega} \Unit{rad \cdot s^{-2}}

Where :math:`\tau` is the applied torque, :math:`I` is an ideal inertia component, and :math:`\omega` is the angular velocity.

Looking at the electrical domain, we find a similar behaviour in the ideal coil, also known as the inductor. In this case, we substitute force by voltage, velocity by current, and the mass by the inductor's self inductance :math:`L` expressed in Henry.

.. math::

  u\Unit{V} = L\Unit{H} \cdot \Diff{i}\Unit{A \cdot s^{-1}}

And also in the hydraulic domain, the dynamics of hydraulic inertance have the same form. An example of hydraulic inertance is a long pipe with fluid that resists against a change in flow because the fluid has its own inertia. This time we substitute force by pressure, velocity by volumetric flow rate, and the mass by the fluid's hydraulic inertance:

.. math::

  p\Unit{Pa} = I \Unit{Pa \cdot m^{-3} \cdot s^2} \cdot \Diff{Q} \Unit{m^3 \cdot s^{-2}}

Notice how all these equations have the same shape, where the resultant force, torque, voltage, or pressure depends on the time derivative of the velocity, angular velocity, current, or volumetric flow, multiplied by some ideal component parameter. The former variable can be generalized with *effort* :math:`e`, and the latter with *flow* :math:`f` (don't mistake the flow with translational mechanical force). The component parameter will then be a generalized inertia parameter :math:`I`, giving:

.. math::

  e = I \Diff{f}

For simulation purposes, we like to write such equations in their integral form (and assuming a constant component parameter). For example in the translational mechanical domain:

.. math::

  v\Unit{m \cdot s^{-1}} = \frac{p \Unit{kg \cdot m \cdot s^{-1}}}{\Mass \Unit{kg}}, \quad p = p_0 + \Int{f}

A few things can be noticed from this form of the same equation. Firstly, we no longer look at the force (effort) directly, but at its integral, in the translational mechanical domain that is the momentum :math:`p`. By applying a force to the mass, more momentum is added. So we can see the mass as some kind of storage for momentum. Secondly, by using the integral form, we can take into account the momentum that the mass already had, the initial momentum :math:`p_0`, before we started looking at it. Finally, the velocity of the mass (flow) is clearly a result from applying a force (effort). We call this the *causality* of this component. For a generalized inertia, we prefer *flow-out* causality (or *effort-in* causality, which is the same).

The generalized version of this equation looks like this:

.. math::

  f = \frac{p}{I}, \quad p = p_0 + \Int{e}

Where :math:`p` represents the :math:`p`-type storage variable, also called generalized momentum, :math:`f` again is the flow, :math:`e` is the effort, and :math:`I` is the generalized inertance parameter. We can describe this behaviour using a block diagram as shown below.

.. figure:: /_static/figures/session6/block_diagrams_ideal_components/block_diagrams_ideal_components-001.svg
  
  Block diagram representation of the dynamic behaviour of a generalized inertia.

We often use iconic symbols to depict domain-specific systems. The following icons or symbols can be used to depict inertances in their specific domain.

.. figure:: /_static/figures/session6/iconic_diagram_symbols/inertances-001.svg

  Translational mechanical domain: mass. :math:`\Mass` indicates the value of the mass.

.. figure:: /_static/figures/session6/iconic_diagram_symbols/inertances-002.svg

  Rotational mechanical domain: inertia. :math:`I` indicates the value of the inertia.

.. figure:: /_static/figures/session6/iconic_diagram_symbols/inertances-003.svg

  Electrical domain: inductor. :math:`L` indicates the value of the inductance.

.. figure:: /_static/figures/session6/iconic_diagram_symbols/inertances-004.svg

  Hydraulic domain: hydraulic inertance. :math:`I` indicates the value of the inertance.

Generalized compliance
----------------------

Another behaviour type that is analogous between these domains is the behaviour of compliance, or C-elements. Compliance components are the *dual* of inertia components.

In the translational mechanical domain, compliance can be found in ideal springs. According to Hook's law, the force :math:`f` exerted by a compressed (or expanded) spring from its natural state, is given by the displacement :math:`x` multiplied by the stiffness (or spring constant) of the spring, generally denoted with :math:`k`, so Hook's law is: :math:`f = kx`. If we instead use the *compliance* of the spring, which is the inverse of stiffness, we can rewrite this as:

.. math::

  f \Unit{N} = \frac{x\Unit{m}}{C\Unit{m \cdot N^{-1}}}, \quad x = x_0 + \Int{v}

This again translates straightforwardly to the rotational mechanical domain:

.. math::

  \tau \Unit{N \cdot m} = \frac{\theta \Unit{rad}}{C \Unit{rad \cdot N^{-1} \cdot m^{-1}}}, \quad \theta = \theta_0 + \Int{\omega}

In the electrical domain the compliance is found in the ideal capacitor component. The voltage that a charged capacitor can exert is given by its capacitance and the charge:

.. math::

  u\Unit{V} = \frac{q\Unit{C}}{C \Unit{F}}, \quad q = q_0 + \Int{i}

In the hydraulic domain, compliance can be found in fluid tanks, e.g. imagine an empty tank with a certain volume. If fluid is pumped in through the bottom by applying pressure to it, the tank itself will be able to apply pressure onto the bottom that is proportional with the volume that is inside. The 'compliance' of this tank is a function of gravity, the fluid's density, and the area of the tank's bottom: :math:`C=A/\rho\Gravity`. The pressure then is given by:

.. math::

  p\Unit{Pa} = \frac{V\Unit{m^3}}{C \Unit{m^3 \cdot Pa^{-1}}}, \quad V = V_0 + \Int{Q}

Other sources of compliance in hydraulic systems can be caused by compressible gas that is trapped in the system (that's why you don't want air in the hydraulic brake system of your car), or flexible tanks or piping.

Again these equations have the same shape, but notice that with respect to the inertia equations, the role of effort and flow variables has flipped. Also, the storage variable is no longer the integral of the effort, but now the integral of the flow variable. This also means that for simulation purposes, we prefer the causality of generalized compliance components to be *effort-out*, contrary to the generalized inertias (which are preferred *flow-out*). The generalized version of this behaviour is described with:

.. math::

  e = \frac{q}{C},\quad q = q_0 + \Int{f}

Where :math:`q` represents the :math:`q`-type storage variable, or generalized displacement. The compliance elements therefore are :math:`q`-type storage elements and store :math:`q`-type storage variables.

.. figure:: /_static/figures/session6/block_diagrams_ideal_components/block_diagrams_ideal_components-002.svg

  Block diagram representation of the dynamic behaviour of a generalized compliance.

The following icons or symbols can be used to depict compliances in their specific domain.

.. figure:: /_static/figures/session6/iconic_diagram_symbols/compliances-001.svg

  Translational mechanical domain: spring. :math:`C` indicates the compliance value of the spring (the inverse of its stiffness).

.. figure:: /_static/figures/session6/iconic_diagram_symbols/compliances-002.svg

  Rotational mechanical domain: rotational spring. :math:`C` indicates the compliance value of the rotational spring (the inverse of its stiffness).

.. figure:: /_static/figures/session6/iconic_diagram_symbols/compliances-003.svg

  Electrical domain: capacitor. :math:`C` indicates the capacitance value of the capacitor.

.. figure:: /_static/figures/session6/iconic_diagram_symbols/compliances-004.svg

  Hydraulic domain: open-topped reservoir. :math:`C` indicates the compliance value of the reservoir (depending on its geometry, the density of the fluid, and gravity).

Note how there is only one so-called *terminal* for the reservoir, in contrast to the spring and capacitor components that have two. That is because due to the nature of how reservoirs are constructed, we always assume a zero-flow and zero-pressure at the other 'terminal', namely the top of the reservoir. This is identical to e.g. attaching one side of a spring to the fixed world, or one side of the capacitor to ground.


Generalized resistance
----------------------

The final generalized behaviour that we learn about in this lesson is generalized resistance. In contrary to the previous two elements, we will introduce this element from the electrical domain. Ohm's law tells us that for a given ideal resistor with a certain resistance :math:`R \Unit{\Omega}`, the voltage drop :math:`u` over this resistor, and the current :math:`i` flowing through it are related as follows:

.. math::

  u \Unit{V} = i \Unit{A} \cdot R \Unit{\Omega}

Due to the linear shape of this equation, it is easy to rewrite it to:

.. math::

  i \Unit{A} = \frac{u \Unit{V}}{R \Unit{\Omega}}

A similar relation can be found in both the mechanical domains:

.. math::
  
    \begin{align*}
    f \Unit{N} &= v \Unit{m \cdot s^{-1}} \cdot D \Unit{N \cdot m^{-1} \cdot s} \\
    \tau \Unit{N \cdot m} &= \omega \Unit{rad \cdot s^{-1}} \cdot D \Unit{N \cdot m \cdot rad^{-1} \cdot s}
    \end{align*}

Where both :math:`D` parameters are viscous damping parameters, and are responsible for velocity dependent resistance. In general, viscous damping is not the only damping that has a significant influence on mechanical dynamics and for accurate simulation, more complex friction models are typically needed. These are outside the scope of this course however.

In the hydraulic domain, a similar relation can also be found, where pressure is lost by the difference in velocity of the fluid flow and the pipe or tube containing the flow.

.. math::

  p \Unit{P} = V \Unit{m^{3} \cdot s^{-1}} \cdot D \Unit{P \cdot s \cdot m^{-3}}

Similar to the mechanical domain however, this is not always the dominant friction behaviour in hydraulic systems. Again the complexer friction models are outside the scope of this course.

The generalized resistance behaviour can be described with:

.. math::

  e = fR

or

.. math::

  f = \frac{e}{R}

For this behaviour, there is no preferred form for simulation. In a block diagram, this is described with either of the following, depending on whether other components impose a flow-in or effort-in direction:

.. figure:: /_static/figures/session6/block_diagrams_ideal_components/block_diagrams_ideal_components-003.svg

  Block diagram representation of the dynamic behaviour of a generalized resistance in effort-out causality.
  
.. figure:: /_static/figures/session6/block_diagrams_ideal_components/block_diagrams_ideal_components-004.svg

  Block diagram representation of the dynamic behaviour of a generalized resistance in flow-out causality.

In contrast to the generalized inertia and generalized compliance, generalized resistance components do not store energy. In this course, we treat resistance components as if they dissipate energy.
:quote-student:`Did you not just tell us that energy does not get dissipated?`
:quote-lecturer:`True, later in this course there could be some time left to look at what resistance components actually do, but that is of no concern to us now.`

The following icons or symbols can be used to depict resistances in their specific domain.

.. figure:: /_static/figures/session6/iconic_diagram_symbols/resistances-001.svg

  Translational mechanical domain: (viscous) damper. :math:`D` indicates the resistance value of the damper.

.. figure:: /_static/figures/session6/iconic_diagram_symbols/resistances-002.svg

  Rotational mechanical domain: (viscous) rotational damper. :math:`D` indicates the resistance value of the damper.

.. figure:: /_static/figures/session6/iconic_diagram_symbols/resistances-003.svg

  Electrical domain: resistor. :math:`R` indicates the resistance value of the resistor.

.. figure:: /_static/figures/session6/iconic_diagram_symbols/resistances-004.svg

  Hydraulic domain: hydraulic friction. :math:`R` indicates the resistance value of the friction.

Example
-------

Let's have a look at a simple electrical circuit. Before closing the switch, we only know that the capacitor has a capacitance :math:`C=1\Unit{F}`, an initial charge :math:`q_0=1\Unit{C}`, and the resistor has a resistance :math:`R=1\Unit{\Omega}`. Both components have their respective voltage with respect to the global zero reference: the earth. The arrows beside the components indicate the positive current direction.

.. figure:: /_static/figures/session6/RC_circuit_example/RC_circuit_example-001.svg

  Simple RC electrical circuit.

From our direction definitions, and the structure of the circuit we can see that the voltages of both components are equal: :math:`u_C = u_R`. The current running through both components is in opposite direction, but of equal magnitude: :math:`i_C=-i_R`.

When we close the switch, the dynamics of the circuit will behave in a certain way, and we can use the block diagrams shown above to determine what their behaviour will look like. First we look at the capacitor, we prefer its dynamic equation to be in integral form, because it has an initial charge :math:`q_0`. The causality of this capacitor will therefore be *effort-out*. This means that it will impose a voltage on the resistor, which in turn will determine how much current will be drawn. This means that the resistor will have a *flow-out* causality. Fortunately we can use the resistor in both causality options. We can draw both block diagrams and connect their efforts and flows as follows (note the sum symbol to change the sign of :math:`i_R`):

.. figure:: /_static/figures/session6/RC_circuit_example/RC_circuit_example-002.svg

  Simple RC electrical circuit, now in block-diagram form.

Now we can use any kind of simulation software capable of simulating block diagrams to simulate the system behaviour, e.g. 20-sim or Matlab/Simulink. If we look at the response of the capacitor's voltage and current :math:`u_C` and :math:`i_c`, given that we close the switch at time :math:`t=0`, we will get the following behaviour:

.. figure:: /_static/figures/session6/responses/responses-001.svg

  RC circuit response of the capacitor voltage and current.


Overview
--------

The table below gives an overview of variables introduced in this lesson.


.. table:: Domain variables for the domains.

  .. list-table::
    :header-rows: 1

    * - Domain
      - Generalized
      - Translational mechanical
      - Rotational mechanical
      - Electromagnetic
      - Hydraulic
    * - :math:`p`-type storage variable
      - feneralized momentum :math:`p`
      - momentum :math:`p`
      - angular momentum :math:`b`
      - magnetic flux linkage :math:`\lambda`
      - hydraulic momentum :math:`\Gamma`
    * - :math:`q`-type storage variable
      - generalized displacement :math:`q`
      - displacement :math:`x`
      - angular displacement (angle) :math:`\theta`
      - charge :math:`q`
      - volume :math:`V`
    * - effort
      - effort :math:`e`
      - force :math:`f`
      - torque :math:`\tau`
      - voltage :math:`u`
      - pressure :math:`p`
    * - flow
      - flow :math:`f`
      - velocity :math:`v`
      - angular velocity :math:`\omega`
      - current :math:`i`
      - volumetric flow :math:`Q`
    * - power
      - :math:`P=ef`
      - :math:`P=fv`
      - :math:`P=\tau\omega`
      - :math:`P=u i`
      - :math:`P=pQ`
