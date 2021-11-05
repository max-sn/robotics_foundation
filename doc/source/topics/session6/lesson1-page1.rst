Domain dynamics introduction
============================

Until this point we have treated the kinematics and dynamics of robotic arms by treating them as chains of rigid bodies linked by actuators that can magically deliver joint forces and torques to get them moving. In reality, these actuators are often powered by electricity, pneumatics, or hydraulics. For accurate modelling and simulation of these kinds of systems, we have to take a step back and change our perspective to include other physical domains in which dynamics are present.

To ensure that we can relate different domains, we need a common denominator, a 'language' that is understood in all domains. We can find one in *energy*, expressed in Joule. By the law of conservation of energy, energy does not dissipate and is exchanged between domains. For the purpose of modelling, it is often more interesting to look at the *rate of energy exchange*, better known as power, expressed in Watt. Let's look at an example.

An anonymous man is riding a bicycle and at a certain point in time, his foot is moving with a certain translational velocity :math:`v` downwards, while he exerts a certain force :math:`f` on the pedal. The power he is applying to the bicycle's pedal is then the product :math:`P=fv`. This power is used to rotate the first of the bicycle's gears and depending on the length of the arm of the pedal this power will result in an angular velocity :math:`\omega` and torque :math:`\tau` of the front gear, where :math:`P=\omega\tau=fv`. This power is again transformed to the translational mechanical domain by the gear that actuates the chain. At the rear wheel of the bicycle the translational mechanical power is once again transformed to rotational mechanical power by rotating the rear gear and with it, the rear wheel. Finally the wheel uses it's friction with the road to transform the power to translational mechanical power that will push the bicycle forward.

.. figure:: /_static/figures/session6/bicycle_example/bicycle_example.svg

  Force and velocity of a bicycle pedal and the arm lengths that transform the power several times from rotational mechanical domain to translational mechanical domain and vice versa.

In the example above, energy stays in the mechanical domain, but transfers between rotational and translational energy. Energy can also be transferred from other domains, e.g.:

* An hydraulic jack: translational mechanical :math:`\rightarrow` rotational mechanical :math:`\rightarrow` translational mechanical :math:`\rightarrow` hydraulic :math:`\rightarrow` translational mechanical

  .. figure:: /_static/figures/session6/hydraulic-jack.jpg
    :width: 400px

    Hydraulic jack.

* A submersible pump: electrical :math:`\rightarrow` rotational mechanical :math:`\rightarrow` hydraulic (fluid)

  .. figure:: /_static/figures/session6/submersible-pump.jpg
    :width: 400px

    Submersible pump.

* A windturbine: pneumatic (wind) :math:`\rightarrow` rotational mechanical :math:`\rightarrow` electrical

  .. figure:: /_static/figures/session6/windturbines.jpg
    :width: 400px

    Windturbines.

Software
--------

For the remainder of this course, it is required to use a simulation software package. A few options are listed below:

.. list-table::
  :header-rows: 1
  :stub-columns: 1

  * - Software
    - Windows
    - Linux
    - GUI
    - License at future employer
    - Support from teacher
  * - `Matlab/Simulink <https://nl.mathworks.com/products.html>`_
    - :math:`\checkmark`
    - :math:`\checkmark`
    - :math:`\checkmark`
    - Possibly
    - Mediocre
  * - `20-sim <https://www.20sim.com/>`_
    - :math:`\checkmark`
    - :math:`\times`
    - :math:`\checkmark`
    - Probably not
    - Better
  * - `Scilab/Xcos <https://www.scilab.org/software/xcos>`_
    - :math:`\checkmark`
    - :math:`\checkmark`
    - :math:`\checkmark`
    - Open-source and free!
    - None yet
  * - `SimuPy <https://simupy.readthedocs.io/en/latest/index.html>`_
    - :math:`\checkmark`
    - :math:`\checkmark`
    - :math:`\times`
    - Open-source and free!
    - None yet
  * - `Python Control Systems Library <https://python-control.readthedocs.io/en/0.9.0/>`_
    - :math:`\checkmark`
    - :math:`\checkmark`
    - :math:`\times`
    - Open-source and free!
    - None yet

Personally, I like to use free and open-source tools, but I haven't had the time yet to work with one of those options. Both Matlab/Simulink and 20-sim can be used at Saxion, but could be of limited use in your later careers.
