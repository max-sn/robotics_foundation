Sources
=======

Besides the storage and dissipation components that we saw on the previous page, we also have components that insert power into the system, so-called *sources*. These components can either provide an effort, or a flow, therefore they can be divided in effort sources and flow sources. The ideal effort source also acts as a flow sink, and conversely the ideal flow source acts as an effort sink. Their behaviour is best explained with their block diagrams.

Effort source
-------------

The ideal effort source's behaviour is defined by a single parameter, :math:`e_s`, which defines the amount of effort is applied on its bond. All flow is terminated by the effort source, indicated by the *terminator*-block shown in the figure below.

.. figure:: /_static/figures/session6/block_diagrams_ideal_components/block_diagrams_ideal_components-009.svg

  Block diagram representation of an ideal effort source with fixed effort-out causality.

Domain examples of effort sources are:

* Gravity, although it is an acceleration, it can be modelled as an ideal source of force.
* Voltage sources, both AC and DC voltage sources can be modelled as ideal sources of voltage. Often an additional (internal) resistance is modelled to limit the current (flow). For AC sources, :math:`e_s` is not constant.

The effort source will always impose an effort on its bond, meaning that has a fixed effort-out causality that cannot be changed. E.g., if we attach an effort source to a generalized capacitance, the capacitance will have to take the non-preferred differential form of flow-out causality.

Iconic symbols used to depict effort sources are:

.. figure:: /_static/figures/session6/iconic_diagram_symbols/effort_sources-001.svg

  Translational mechanical domain: force source. :math:`F` indicates the applied force.

.. figure:: /_static/figures/session6/iconic_diagram_symbols/effort_sources-002.svg

  Rotational mechanical domain: torque source. :math:`\tau` indicates the applied torque.

.. figure:: /_static/figures/session6/iconic_diagram_symbols/effort_sources-003.svg

  Electrical domain: voltage source. :math:`u` indicates the applied voltage.

.. figure:: /_static/figures/session6/iconic_diagram_symbols/effort_sources-004.svg

  Hydraulic domain: pressure source, a centrifugal pump. :math:`P` indicates the applied pressure.

Flow source
-----------

Similar to the effort source, the flow source is also characterised by a single parameter: :math:`f_s`, which defines the amount of flow through its bond. All effort is terminated by the flow source.

.. figure:: /_static/figures/session6/block_diagrams_ideal_components/block_diagrams_ideal_components-010.svg

  Block diagram representation of an ideal flow source with fixed flow-out causality.

Domain examples of flow sources are:

* Current sources, both AC and DC current sources can be modelled as ideal source of flow.
* A huge flywheel, if the dynamics of other parts of your system are insignificant for the angular velocity of the flywheel, you can model (approximate) it as an ideal source of flow. We will see more of these approximations later in the course.

The ideal flow source always imposes a flow on its bond, therefore it is fixed in flow-out causality. If for example you would connect an generalized inertia directly to a flow source, the inertia would have to assume the non-preferred differential form of effort-out causality.

Iconic symbols used to depict flow sources are:

.. figure:: /_static/figures/session6/iconic_diagram_symbols/flow_sources-001.svg

  Translational mechanical domain: velocity source. :math:`v` indicates the supplied velocity.

.. figure:: /_static/figures/session6/iconic_diagram_symbols/flow_sources-002.svg

  Rotational mechanical domain: angular velocity source. :math:`\tau` indicates the supplied angular velocity.

.. figure:: /_static/figures/session6/iconic_diagram_symbols/flow_sources-003.svg

  Electrical domain: current source. :math:`u` indicates the supplied current.

.. figure:: /_static/figures/session6/iconic_diagram_symbols/flow_sources-004.svg

  Hydraulic domain: flow source, a displacement pump. :math:`f` indicates the supplied volume flow.

Causality
---------

With ideal sources, we have another set of components to worry about when assigning causality. Since these have *fixed* causality, they overrule the *preferred* causality from the storage elements (inertances and capacitances). To assign causality in a system we use the following order:

1. Sources (fixed causality)
2. Storage elements (preferred causality)
3. Resistances (arbitrary causality)

In some unfortunate systems, it might prove necessary to have storage elements in non-preferred causality. This is undesirable for several reasons:

* Differentiating 'amplifies' noise such as numerical inaccuracies, while integrating 'filters' noise out.
* Components in differential form cannot have an initial value, which limits the models usefulness.
* Components in differential form cannot be simulated with discontinues inputs like pulse functions or step functions.

Example
-------

Now that we have introduced ideal sources, let's have a look at an example. Consider the following circuit.

.. figure:: /_static/figures/session6/effort_source_example/effort_source_example-001.svg

  Ideal voltage source in series with an inductor.

As previously, we take the ground as a zero voltage reference, and the arrows indicate the direction of positive current. By convention, all components have positive current towards the ground, except for sources.

In dynamic behaviour, this is the same system as the following mechanical system.

.. figure:: /_static/figures/session6/effort_source_example/effort_source_example-002.svg

  Force acting on mass w.r.t the fixed world.

Here the symbol on the left indicates the fixed world which is the zero velocity reference, the symbol in the center indicates an ideal force source, and the symbol on the right indicates an ideal mass.

In both systems shown above, an ideal effort source is directly connected to an generalized inertia. Both have dynamic behaviour that can be described with the following block diagram:

.. figure:: /_static/figures/session6/effort_source_example/effort_source_example-003.svg

  Ideal effort source acting on generalized inertia.

If we take the flow of the inertia to be the output of the system, and the effort provided by the effort source the input, we can write the dynamic equation as follows:

.. math::

  f = \frac{p}{I}, \quad p=p_0 + \Int{e}

Where :math:`f=y(t)` is the output, and :math:`e=u(t)` is the input.
