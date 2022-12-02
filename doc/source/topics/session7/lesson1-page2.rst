Junctions
=========

From the examples we have seen so far, we were only able to construct chain-like structures from the one- and two-bond components that we treated. To form arbitrary structures, we need another kind of component, with the potential to form more than two bonds. It turns out that it is convenient to define two of these components, and we call them 0- and 1-junctions respectively. We can introduce this junctions again by means of examples.


1-junction
----------

Let's have a look at a series LRC circuit, powered by a voltage source.

.. figure:: /_static/figures/session7/uLRC_circuit_example/uLRC_circuit_example-001.svg

  Voltage source powered LRC electrical circuit.

As before, the arrows besides the components indicate the direction in which we define the current and voltage (flow and effort) to be positive. By convention these are directed towards the ground. From Kirchhoff's laws we can determine the following equations:

.. math::

    \begin{gather*}
      0 = -u + u_L + u_R + u_C \\
      i = i_L = i_R = i_C
    \end{gather*}

.. raw:: html

  <div class="recap">Kirchhoff's laws
    <ol>
      <li>The current entering any junction is equal to the current leaving that junction;</li>
      <li>The sum of all voltages around a loop is equal to zero.</li>
    </ol>
  </div>

We can combine these in block diagram form as follows. We call this structure a *1-junction*.

.. figure:: /_static/figures/session7/uLRC_circuit_example/uLRC_circuit_example-002.svg

  Block diagram representation of a 1-junction structure, without causality assigned, so it is still unclear in which direction the signals are directed.

We use a sum block for the voltages, and because it has only one output, we have a maximum of one effort-out causality for this 1-junction structure. The other bonds have flow-out causality, as seen from the 1-junction.

In this example, the voltage source has fixed effort-out causality, which is seen as effort-in by the 1-junction. The capacitor has a preferred effort-out causality, again seen as effort-in by the 1-junction. The inductor has a preferred flow-out causality, so this could be the single effort-out for the 1-junction. The final bond we have to consider is the bond between 1-junction and the resistor. Since the resistor has no preferred causality, we can choose for it to have effort-in as seen by the 1-junction, therefore allowing the inductor to have its preferred effort-out causality. This gives us all the directions for the block diagram.

.. figure:: /_static/figures/session7/uLRC_circuit_example/uLRC_circuit_example-003.svg

  1-junction structure with included directions for a series LRC circuit.

We can rewrite the voltage equation from above in terms of the inductor voltage :math:`u_L`:

.. math::

  u_L = u - u_R - u_C

This gives us the signs with which the efforts should be added by the sum block. These are the direct result of how we defined the directions in the circuit above. Finally we can complete the block diagram by adding the missing components.

.. figure:: /_static/figures/session7/uLRC_circuit_example/uLRC_circuit_example-004.svg

  Dynamic equations of a series LRC circuit, expressed in block diagram representation.

Simulating this model with unit parameters (:math:`u=C=L=R=1`) gives the following response for the inductor voltage and current:

.. figure:: /_static/figures/session6/responses/responses-003.svg

  Response graph of a constant voltage powered series LRC circuit.

In short, the 1-junction structure can be used to join components that share the same flow. In electrical circuits that are components in series, in mechanical systems that are components that share the same velocity (or act on the same velocity difference, e.g. a spring acts on a velocity difference).


0-junction
----------

To comply to the theme of duality, there should be another junction structure for components that share the same *effort*. Such a junction is called a 0-junction. Let's take a parallel LRC circuit powered by a current source for example now.

.. figure:: /_static/figures/session7/iLRC_circuit_example/iLRC_circuit_example-001.svg

  Iconic diagram of a current source powered parallel LRC circuit.

Again applying Kirchhoff's laws, we get the following equations:

.. math::

  \begin{gather*}
    0 = i - i_L + i_C + i_R \\
    u = u_L = u_C = u_R
  \end{gather*}

Similar to the 1-junction structure, we can use a sum block, but now for the current (flow) equation, and a signal splitter for the voltage (effort) equation. This gives the following structure:

.. figure:: /_static/figures/session7/iLRC_circuit_example/iLRC_circuit_example-002.svg

  Block diagram representation of a 0-junction structure, without causality assigned.

Again we have sum block that has only one output, so this junction structure can have only one bonded component that has a flow-in (or effort-out) causality. The flow source has fixed flow-out causality, the inductor has preferred flow-out causality, and the capacitor has preferred flow-in causality, and again the resistor has no preferred causality. Therefore we can choose the capacitor as the single flow-in causality component connected to the 0-junction. This gives us the directions in which the signals are flowing in the junction structure:

.. figure:: /_static/figures/session7/iLRC_circuit_example/iLRC_circuit_example-003.svg

  Block diagram representation of a 0-junction structure, without causality assigned.

Finally we can add the blocks that represent the component behaviour, note that the resistor now is in flow-out causality so we use the :math:`\frac{1}{R}` block. Also we rewrite the current equation from above in terms of :math:`i_C` to get the signs with which :math:`i`, :math:`i_L`, and :math:`i_R` are added to the sum block.

.. math::

  i_C = i - i_L - i_R

This gives the following complete block diagram:

.. figure:: /_static/figures/session7/iLRC_circuit_example/iLRC_circuit_example-004.svg

  Dynamic equations of a parallel LRC circuit, expressed in block diagram representation.

Simulating this model with unit parameters (:math:`i=C=L=R=1`) gives the following response for the inductor voltage and current:

.. figure:: /_static/figures/session6/responses/responses-004.svg

  Response graph of a constant current powered parallel LRC circuit.

In short, the 0-junction structure can be used to join component that share the same effort. In electrical circuits that are components in parallel, in mechanical systems that are components that share the same force, but these are in general hard to find.