Introduction to rigid-body motions
==================================

.. raw:: html

  <iframe style="width: 695px; height: 390px;" src="https://www.youtube-nocookie.com/embed/29LhXWjn7Pc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

As already mentioned in the lesson on configuration space, orientation is not described with a 'flat' space. Therefore, the velocity of orientation is not the time derivative of orientation.

As the instructor already mentions, all frames in this course will be right-handed. That means that we can use the cross-product :math:`\UnitLength{z} = \UnitLength{x} \wedge \UnitLength{y}` to determine the direction of the third (:math:`z`-) axis. You can use the right-hand rule as given in the video, and shown below in the figure for reference.

.. figure:: /_static/figures/session2/right_hand_rule_coordinate_frame/right_hand_rule_coordinate_frame.svg

  Right hand rule for determining axis directions.

Positive rotation direction can also be determined by means of a right hand rule, see the figure below for reference.

.. figure:: /_static/figures/session2/right_hand_rule_orientation/right_hand_rule_orientation.svg

  Right hand rule for determining positive rotation direction.

To describe the configuration of a rigid body, you can fix a coordinate frame to the rigid body in a convenient location (often this should be the center of mass, with the axes aligned with the principal axes of the body and we will see later why that is convenient), and fix a reference coordinate frame in a convenient location in space. The relative pose between those frames will define the configuration.