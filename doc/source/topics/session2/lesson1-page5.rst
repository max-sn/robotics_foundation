Homogeneous transformation matrices
===================================

.. raw:: html

  <iframe style="width: 695px; height: 390px;" src="https://www.youtube-nocookie.com/embed/vlb3P7arbkU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Properties of homogeneous transformation matrices are very similar to those of rotation matrices.

* Inverse:  we can find the inverse quickly and neatly by using the transpose property of the rotation matrices.

  .. math::

    \HomogeneousTransformationMatrix^{-1} =
    \begin{bmatrix}
      \RotationMatrix & p \\
      0 & 1
    \end{bmatrix}^{-1}
    =
    \begin{bmatrix}
      \RotationMatrix\Transposed & -\RotationMatrix\Transposed p \\
      0 & 1
    \end{bmatrix} \in \SEthree

  This can be done quickly with :py:func:`~modern_robotics.num.inv_SE3` (Python) or :mat:func:`~+MR.inv_SE3` (MATLAB), which are numerically stable for all homogeneous transformation matrices. Using MATLAB's or numpy's ``inv`` functions is (in theory) slower, and might in some circumstances lead to unexpected results.

* Closure: the product of any two transformation matrices will be another transformation matrix.

  .. math::

    \HomogeneousTransformationMatrix_1 \HomogeneousTransformationMatrix_2 \in \SEthree

* Associative: the order of multiplication for multiple transformation matrices is arbitrary, as long as the direction (left- or right multiplication) is the same.

  .. math::

    (\HomogeneousTransformationMatrix_1 \HomogeneousTransformationMatrix_2)
    \HomogeneousTransformationMatrix_3 = \HomogeneousTransformationMatrix_1
    (\HomogeneousTransformationMatrix_2 \HomogeneousTransformationMatrix_3)

* Not commutative: same as for rotation matrices, the direction of multiplication (left- or right multiplication) is generally not arbitrary.

  .. math::

    \HomogeneousTransformationMatrix_1 \HomogeneousTransformationMatrix_2 \neq \HomogeneousTransformationMatrix_2 \HomogeneousTransformationMatrix_1

Homogeneous transformation matrices can be used to change the frame of reference of a vector. For example, a point :math:`p` expressed in :math:`\CoorSys{b}` can be expressed in frame :math:`\CoorSys{s}` using the transformation matrix :math:`\FromTo{b}{s}{\HomogeneousTransformationMatrix}`. Due to the difference in shape, we have to use the so-called homogeneous form of the point :math:`p`, which is denoted with :math:`\HomogeneousCoordinate{p}` and can be constructed simply by adding a :math:`1` at the bottom:

.. math::

  \HomogeneousCoordinate{p} =
  \begin{bmatrix}
    p \\ 1
  \end{bmatrix}

In the video the instructor mentions that the frame of reference for the translation vector and rotation axis (:math:`p` and :math:`\UnitLength{\omega}`) are dependent on whether the transformation matrix is left- or right multiplied to the initial transformation :math:`\FromTo{b}{s}{\HomogeneousTransformationMatrix}`. It is more intuitive to think of it the other way around. We already have a translation vector and rotation axis, and depending on the frame they are expressed in, we determine whether to left- or right multiply the initial transformation with our transformation matrix.

* :math:`\To{b}{p}` and :math:`\To{b}{\UnitLength{\omega}}` expressed in :math:`\CoorSys{b}` :math:`\rightarrow` body frame transformation :math:`\rightarrow` right multiplication :math:`\FromTo{b}{s}{\HomogeneousTransformationMatrix}\HomogeneousTransformationMatrix(p, \UnitLength{\omega})`

  Example with :math:`\UnitLength{\omega}=[0,0,1]\Transposed` and :math:`p=[0,2,0]\Transposed`, expressed in :math:`\CoorSys{b}`:

  .. raw:: html

    <figure>
      <object type="image/svg+xml" data="/web/Rserobo000/Public_Html/figures/session2/left_multiply/master.svg">
      </object>
    </figure>

* :math:`\To{s}{p}` and :math:`\To{s}{\UnitLength{\omega}}` expressed in :math:`\CoorSys{s}` :math:`\rightarrow` space frame transformation :math:`\rightarrow` left multiplication :math:`\HomogeneousTransformationMatrix(p, \UnitLength{\omega})\FromTo{b}{s}{\HomogeneousTransformationMatrix}`

  Example with :math:`\UnitLength{\omega}=[0,0,1]\Transposed` and :math:`p=[0,2,0]\Transposed`, expressed in :math:`\CoorSys{s}`):

  .. raw:: html

    <figure>
      <object type="image/svg+xml" data="/web/Rserobo000/Public_Html/figures/session2/right_multiply/master.svg">
      </object>
    </figure>

Note that whether you have to left or right multiply, you still construct the transformation matrix from :math:`p` and :math:`\UnitLength{\omega}` as follows:

.. math::

  \HomogeneousTransformationMatrix(p, \UnitLength{\omega}) =
  \begin{bmatrix}
    I_3 & p \\
    0_{1\times 3} & 1
  \end{bmatrix}
  \begin{bmatrix}
    \exp(\theta\TildeSkew{\UnitLength{\omega}}) & 0_{3\times 1} \\
    0_{1\times 3} & 1
  \end{bmatrix}

Where :math:`I_3` is the 3 by 3 identity matrix. That is why, in the animations, it seems as if the translation is applied first when right-multiplying, while for left-multiplying it seems as if the rotation is applied first.