Product of exponentials formula in the space frame
==================================================

.. raw:: html

  <iframe style="width: 695px; height: 390px;" src="https://www.youtube-nocookie.com/embed/hE_Duih_7JE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

The following steps can be taken to determine the forward kinematics (:math:`\FromTo{b}{s}{\HomogeneousTransformationMatrix}(\Configuration)`) based on the joint's unit twists (screw axes) expressed in the space frame :math:`\CoorSys{s}`.

1. We start with the transformation :math:`\FromTo{b}{s}{\HomogeneousTransformationMatrix}(\Configuration)` for :math:`\Configuration=0`. This transformation, :math:`\FromTo{b}{s}{\HomogeneousTransformationMatrix}(0)=M`, is the pose of frame :math:`\CoorSys{b}` expressed in frame :math:`\CoorSys{s}` when the robot is at its zero configuration.
#. Then we find the screw axes :math:`\Screw_1,\ldots,\Screw_n` for all of the :math:`n` joints, expressed in the space frame :math:`\CoorSys{s}`, also in the robot's zero configuration (:math:`\Configuration=0`).
#. Finally when we have a configuration :math:`\Configuration` for which we want to determine the forward kinematics :math:`\FromTo{b}{s}{\HomogeneousTransformationMatrix}(\Configuration)`, we construct the product of exponentials (PoE) formula in the space frame, and evaluate it for the given configuration :math:`\Configuration`:

   .. math::

      \FromTo{b}{s}{\HomogeneousTransformationMatrix}=
      \exp({\tilde{\mathcal{S}}_1\GeneralizedCoordinate_1})
      \exp({\tilde{\mathcal{S}}_2\GeneralizedCoordinate_2})
      \cdots
      \exp({\tilde{\mathcal{S}}_n\GeneralizedCoordinate_n})
      M

