Exponential coordinates of rigid-body motion
============================================

.. role:: raw-html(raw)
  :format: html

.. raw:: html

  <iframe style="width: 695px; height: 390px;" src="https://www.youtube-nocookie.com/embed/1jYMvm1U2D0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


.. list-table::
  :header-rows: 1
  :widths: 50 50
  :width: 80%

  * - Rotations
    - Rigid-body motions
  * - rotation axis: :math:`\UnitLength{\omega}`

      * :math:`\Norm{\UnitLength{\omega}}=1`
    - screw axis: :math:`\Screw = (\Screw_{\omega}, \Screw_{v})`

      a. :math:`\Norm{\Screw_{\omega}}=1`, or
      b. :math:`\Screw_{\omega}=0, \Norm{\Screw_{v}}=1`
  * - exponential coordinates: :math:`\UnitLength{\omega}\theta \in \mathbb{R}^3`
    - exponential coordinates: :math:`\Screw\theta \in \mathbb{R}^6`
  * - matrix representation: :math:`\TildeSkew{\UnitLength{\omega}}\theta \in \sothree`
    - matrix representation: :math:`\TildeSkew{\Screw}\theta \in \sethree`
  * - * exp: :math:`\sothree \rightarrow \SOthree`
      * log: :math:`\SOthree \rightarrow \sothree`
    - * exp: :math:`\sethree \rightarrow \SEthree`
      * log: :math:`\SEthree \rightarrow \sethree`

So the exponential for rigid-body motions will map a screw motion in :math:`\sethree` to a tansformation matrix in :math:`\SEthree`. So when we know the screw axis :math:`\Screw`, and we know the 'distance' travelled along the screw axis :math:`\theta`, we can determine the transformation matrix that will apply this motion by calculating the matrix exponential.

Similar to the angular velocity exponential, which we saw earlier, the rigid-body motion exponential also has a closed form solution. Since we have two options for the screw axis (either the angular velocity part is unit length, or it is zero and the linear velocity part is unit length), we also have two closed form solutions.

* In the case that :math:`\Screw_{\omega} = 0` and :math:`\Norm{\Screw_{v}} = 1`:

  .. math::

    \exp(\TildeSkew{\Screw}\theta) =
    \begin{bmatrix}
      I & \Screw_{v}\theta \\
      0 & 1
    \end{bmatrix}

  This means that there is no angular velocity, and therefore no resulting rotation. The displacement is simply the linear velocity times the distance travelled along the linear part of the screw axis.
* In the case that :math:`\Norm{\Screw_{\omega}} = 1`:

  .. math::

    \exp(\TildeSkew{\Screw}\theta) =
    \begin{bmatrix}
      \exp(\TildeSkew{\Screw}_{\omega}\theta) &
        (I\theta + \TildeSkew{\Screw}_{\omega}(1 - \cos\theta) +
          \TildeSkew{\Screw}_{\omega}^2(\theta -\sin\theta)) \Screw_{v} \\
      0 & 1
    \end{bmatrix}

  In which we can recognize the rotation matrix on the top left, which is mapped by the angular velocity exponential.

In the following chapter we will learn that robot joint axes can be expressed as screw axes and therefore we can easily compute the transformation due to a certain robot joint.


Code
----

Similar to the exponential coordinates of rotation, working out these equations is not complex, but it is cumbersome and prone to errors. We would prefer to have these calculations done by software.

For this lesson, the :doc:`/index` repository also has a function to aid with the calculations. The :py:func:`~modern_robotics.num.vec_to_SE3` function (MATLAB: :mat:func:`~+MR.vec_to_SE3`) is particularly interesting. It uses the matrix exponential to 'integrate' over a velocity twist to find a transformation matrix. The same module also has the :py:func:`~modern_robotics.num.SE3_to_vec` function (MATLAB: :mat:func:`~+MR.SE3_to_vec`) that 'differentiates' a transformation matrix to find a velocity twist, using the matrix log. In the same module, you can also find convenience functions, e.g. to invert a transformation matrix (Python: :py:func:`~modern_robotics.num.inv_SE3`, MATLAB: :mat:func:`~+MR.inv_SE3`), and to construct the 'big adjoint' (Python: :py:func:`~modern_robotics.num.big_adjoint`, MATLAB: :mat:func:`~+MR.big_adjoint`).