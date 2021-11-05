Product of exponentials formula in the body frame
=================================================

.. raw:: html

  <iframe style="width: 695px; height: 390px;" src="https://www.youtube-nocookie.com/embed/27jUrkFdyks" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Similarly to the PoE formula in the space frame, we can find the same transformation as on the previous page (:math:`\FromTo{b}{s}{T}(\Configuration)`) when we express the joint unit twists in the end-effector frame :math:`\CoorSys{b}`. To do this, you can follow these steps:

1. First we find again the zero configuration transformation of the end-effector frame :math:`\CoorSys{b}`: :math:`M`, which is :math:`\FromTo{b}{s}{T}(0)`.
#. Now instead of expressing the joint unit twists in the space frame, we express them in the end-effector frame :math:`\CoorSys{b}`. So we find :math:`\BodyScrew_1,\ldots,\BodyScrew_n` for all :math:`n` joints.
#. Finally, for a given :math:`\Configuration`, we evaluate the PoE formula in the end-effector frame:

   .. math::

      \FromTo{b}{s}{T}(\Configuration)=
      M
      \exp({\tilde{\BodyScrew}_1\theta_1})
      \exp({\tilde{\BodyScrew}_2\theta_2})
      \cdots
      \exp({\tilde{\BodyScrew}_n\theta_n})

   Where the matrix exponentials are now multiplied on the <em>right</em> of :math:`M`, because the screw axes, and therefore the transformations resulting from the matrix exponentials, are expressed in the body frame :math:`\CoorSys{b}`, in this case the end-effector frame.
