Bond graphs
===========

The block diagram notation that we have seen this far is intuitive once the diagram is complete, and it is fairly simple to implement in most simulation software. For modelling, it unfortunately also has quite a few downsides. Firstly, it is very verbose, every operation is separately described with a different block, even though we often (always) use the same combinations of blocks. Secondly, the combination of blocks to use changes when the causality of the component changes. Finally, the idea of power flows between components can be made more explicit if every component has a single symbol. Fortunately, for the way of modelling we used so far, such a compact representation can be found in the form of *bond graphs* (`See Wikipedia <https://en.wikipedia.org/wiki/Bond_graph>`_, but please don't get lost on all the possible systems, rather skip to `Components <https://en.wikipedia.org/wiki/Bond_graph#Components>`_.).


One-port components
-------------------

.. list-table::
  :header-rows: 1

  * - Component
    - Bond graph element
  * - Inertance
    - :math:`\mathbf{I}`
  * - Compliance
    - :math:`\mathbf{C}`
  * - Resistance
    - :math:`\mathbf{R}`
  * - Effort source
    - :math:`\mathbf{Se}`
  * - Flow source
    - :math:`\mathbf{Sf}`


Two-port components
-------------------

.. list-table::
  :header-rows: 1
  
  * - Component
    - Bond graph element
  * - Transformer
    - :math:`\mathbf{TF}`
  * - Gyrator
    - :math:`\mathbf{GY}`


Multi-port components
---------------------

.. list-table::
  :header-rows: 1

  * - Component
    - Bond graph element
  * - 1-junction
    - :math:`\mathbf{1}`
  * - 0-junction
    - :math:`\mathbf{0}`


Power bond
----------

The power bonds, after which bond graphs are named, are single lines between components. These lines now have a double function, the first is to indicate *positive* power direction. This is done by a half-arrow indicating the positive direction:

.. figure:: /_static/figures/session7/bonds/bonds-001.svg

  Bond with positive power in right direction. Note that the half-arrow should always be directed downwards.

By convention, the positive direction is directed towards the :math:`\mathbf{I}`-, :math:`\mathbf{C}`-, and :math:`\mathbf{R}`-elements, and directed away from the :math:`\mathbf{Se}` and :math:`\mathbf{Sf}` elements. Bonds between junctions have positive direction towards the zero reference, e.g. the fixed world for mechanical systems and ground for electrical systems.

The second function is to indicate the direction of effort and flow in the bond. This is done by a small dash at either the front or end of the arrow, called the causal stroke.

.. figure:: /_static/figures/session7/bonds/bonds-004.svg

  Bond with effort going to the right (and flow to the left).

.. figure:: /_static/figures/session7/bonds/bonds-005.svg

  Bond with effort going to the left (and flow to the right).

Note that the causal stroke only indicates the direction of causality, not the direction of positive flow or effort. If a bond is in effort-out causality, the flow goes in the negative power direction, so it should be negated.

If the causality of a bond is different from the preferred causality of the component attached to it, by convention we choose to give the causal stroke an orange colour.

.. figure:: /_static/figures/session7/bonds/bonds-006.svg

  Bond with effort going right, causes the C-element to be in nonpreferred effort-in causality.

When needed, you can label the flow and effort that goes through a bond. By convention the effort is always denoted *above* the bond, and the flow is always denoted *below* the bond.

.. figure:: /_static/figures/session7/bonds/bonds-007.svg

  Effort and flow on a bond labelled.


Systematic approach
-------------------

To derive a bond graph from a mechanical system, take the following steps:

#. Place a 1-junction for every distinct velocity. Typically these can be found at masses and references such as the fixed world.
#. For every spring and damper, place a velocity difference 1-junction, and attach it to a 0-junction that is placed between the two 1-junctions representing the velocities where it acts.
#. Attach components to their respective 1-junctions.
#. Draw bonds. By convention power direction should be directed towards the fixed world, except for the bonds connecting I-, C-, and R-components.

To derive a bond graph from an electrical system, take the following steps:

#. Place a 0-junction for every distinct voltage. Typically these can be found at nodes in the circuit.
#. For every component, place a 1-junction between the 0-junctions representing the nodes where it is placed between.
#. Attach components to their respective 1-junctions.
#. Draw bonds. By convention power direction should be directed towards ground, except for the bonds connecting I-, C-, and R-components.

Next you can simplify the bond graph as follows:

#. Remove junctions with a zero reference, e.g. 0-junctions that represent nodes where an electrical ground is attached, or 1-junctions that represent velocities of the fixed world.
#. Remove other junctions with less than three bonds. If they have two bonds, connect those components directly, *if they have the same direction*. If they have opposite direction, keep the junction.
#. Combine similar junctions that are connected in series, e.g. two 0- or two 1-junctions.
#. Optionally 'pull' components through transformers and gyrators.

Finally you can assign causality.

#. Draw fixed causalities from sources.
#. Draw preferred causalities from storage elements.
#. Complete causalities from junctions.
#. Draw causalities from resistance elements.

If at any step there is a conflict in assigning causality, e.g. when a 1-junction has more than one bond with effort directed outwards, change one of the preferred causalities of storage elements to a nonpreferred causality.


Examples
========


RC circuit
----------

We look again at one of the examples from the previous lesson on dynamic behaviour, the RC circuit:

.. figure:: /_static/figures/session7/RC_circuit_example/RC_circuit_example-001.svg

  Simple RC electrical circuit.

Now let's create a bond graph. The first step is to draw 0-junctions for all nodes with distinct voltages. In this case there are only two distinct voltages:

.. figure:: /_static/figures/session7/RC_circuit_example/RC_circuit_example-002.svg

Create their respective 0-junctions.

.. figure:: /_static/figures/session7/RC_circuit_example/RC_circuit_example-003.svg

We have two components, so we create their respective 1-junctions and connect them. Positive power direction is directed towards the C- and R-components.

.. figure:: /_static/figures/session7/RC_circuit_example/RC_circuit_example-005.svg

Next we draw the bonds, with positive direction directed towards the grounded 0-junction.

.. figure:: /_static/figures/session7/RC_circuit_example/RC_circuit_example-006.svg

Then we can remove the grounded 0-junction.

.. figure:: /_static/figures/session7/RC_circuit_example/RC_circuit_example-007.svg

Next we can remove the two 1-junctions, because they have only two bonds and those have the same direction. We cannot remove the 0-junction, because its bonds have opposite direction.

.. figure:: /_static/figures/session7/RC_circuit_example/RC_circuit_example-008.svg

We can assign causality starting with the C-component, because there are no sources.

.. figure:: /_static/figures/session7/RC_circuit_example/RC_circuit_example-009.svg

We complete the causality of the 0-junction, it already has a single effort-in from the C-component, so the R-component gets an effort-out (seen from the junction). We can label the flows and efforts on the bonds for clarity.

.. figure:: /_static/figures/session7/RC_circuit_example/RC_circuit_example-010.svg

Finally if we want to simulate the system in software that does not directly support bond graphs, we can convert the bond graph to block diagrams using the combinations we saw before:

.. figure:: /_static/figures/session7/RC_circuit_example/RC_circuit_example-011.svg


Mass-spring system
------------------

Another often encountered dynamic system is a mass-spring system.

.. figure:: /_static/figures/session7/mass_spring_damper/mass_spring_damper-001.svg

  Mass-spring system. A mass is connected to the fixed world by means of an ideal spring. Gravity is acting on the mass and is displayed as force source. Velocities and forces are defined to be positive in the same direction as the gravity.

For mechanical diagrams, we first look at distinct velocities. In this case, there are two and they are already labelled in the figure above. For these velocities we create 1-junctions.

.. figure:: /_static/figures/session7/mass_spring_damper/mass_spring_damper-002.svg

The spring acts on the velocity difference between :math:`v_1` and :math:`v_0`. For this, we can use a 0-junction between the two 1-junctions, connected to another 1-junction which will represent the velocity difference.

.. figure:: /_static/figures/session7/mass_spring_damper/mass_spring_damper-003.svg

Next we can connect the components to their respective 1-junctions. The inertia and the force source both act on :math:`v_1`, and the spring on its specific velocity difference.

.. figure:: /_static/figures/session7/mass_spring_damper/mass_spring_damper-004.svg

Then we connect the junctions, keeping positive direction towards the fixed world representing 1-junction (:math:`v_0`), and then remove that 1-junction.

.. figure:: /_static/figures/session7/mass_spring_damper/mass_spring_damper-006.svg

Now we have the C-component connected to :math:`v_1`, but via a 0-junction and a 1-junction. Both these junctions have two bonds but both also have their bonds in opposite direction. Both will impose a negation on the power direction, and therefore cancel each other out. Therefore we can remove them both and directly connect the C-component to :math:`v_1`.

.. figure:: /_static/figures/session7/mass_spring_damper/mass_spring_damper-007.svg

Then we can assign causality, first by starting with the force source. This has fixed effort-out causality. We continue with the preferred causalities of the mass and spring. They don't create any conflicts with the causality of the 1-junction so we're done.

.. figure:: /_static/figures/session7/mass_spring_damper/mass_spring_damper-008.svg

Again for simulating in software that does not support simulating bond graphs directly, we have to convert this to a block diagram.

.. figure:: /_static/figures/session7/mass_spring_damper/mass_spring_damper-009.svg


Cable drum
----------

Consider the following mechanical system, driven by an ideal torque force.

.. figure:: /_static/figures/session7/cable_drum_example/cable_drum_example-001.svg

  Iconic diagram representation of a torque source driving a pulley system that pulls on a mass.

We will go slightly faster in this example. There are four distinct velocities, namely: :math:`\omega_0` at the fixed world, :math:`\omega_1` between the torque source and the transmission, :math:`\omega_2` between the transmission and the cable drum, and finally :math:`v_3` at the mass. We can attach the torque source at :math:`\omega_1`, and the mass at :math:`v_3`. For both the transmission and the cable drum we can use transformers.

.. figure:: /_static/figures/session7/cable_drum_example/cable_drum_example-004.svg

Next we draw the directions of the power bonds, again towards the fixed world. Note that for transformers this also defines what to use as transformation ratio. In the iconic diagram, the transmission will scale the velocity to its left with a factor :math:`i`, but because the direction is reversed in the bond graph, the factor will invert to :math:`\frac{1}{i}`. Similar for the cable drum. An easy way to check whether the ratio should be inverted is to check with the iconic diagram whether the right (or left) velocity would respond as expected for a given left (or right) velocity, using the equations of the transformer.

.. figure:: /_static/figures/session7/cable_drum_example/cable_drum_example-005.svg

Next we can remove the zero reference velocity (:math:`\omega_0`), and other junctions that have two bonds with the same direction.

.. figure:: /_static/figures/session7/cable_drum_example/cable_drum_example-007.svg

Coincidentally, we now have two transformers connected in series. These can be combined to a single transformer by multiplying their ratios.

.. figure:: /_static/figures/session7/cable_drum_example/cable_drum_example-008.svg

If the velocities are important outputs of the simulation, the model is now sufficiently simplified. If not, we can invert the transformer to change the direction of its bonds once more. To do that, we must invert its ratio. Then we can remove both remaining 1-junctions. Assigning causality gives us:

.. figure:: /_static/figures/session7/cable_drum_example/cable_drum_example-010.svg

In block diagram that is:

.. figure:: /_static/figures/session7/cable_drum_example/cable_drum_example-011.svg
