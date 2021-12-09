Rotation matrices (part 1 of 2)
===============================

Before looking at the complete configuration of a rigid body, first we will study the orientation separately.

Recap: Note that for any frame :math:`\CoorSys{a}`, the unit vectors of the :math:`x`, :math:`y`, and :math:`z` axes expressed in that same frame :math:`\CoorSys{a}` (:math:`\FromTo{a}{a}{\UnitLength{x}}, \FromTo{a}{a}{\UnitLength{y}}, \FromTo{a}{a}{\UnitLength{z}}`) are as follows:

.. math::

  \FromTo{a}{a}{\UnitLength{x}} =
  \begin{bmatrix}
  1 \\ 0 \\ 0
  \end{bmatrix}, \quad
  \FromTo{a}{a}{\UnitLength{y}} =
  \begin{bmatrix}
  0 \\ 1 \\ 0
  \end{bmatrix}, \quad
  \FromTo{a}{a}{\UnitLength{z}} =
  \begin{bmatrix}
  0 \\ 0 \\ 1
  \end{bmatrix}

When expressed in another frame, however, these coordinate vectors could be different. This is used to find the orientation between two frames in the following video.

.. raw:: html

  <iframe style="width: 695px; height: 390px;" src="https://www.youtube-nocookie.com/embed/OZucG1DY_sY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Properties of a rotation matrix:

* Inverse: the inverse of a rotation matrix is equal to its transposed, and is also a rotation matrix.

  .. math::

    \RotationMatrix^{-1} = \RotationMatrix\Transposed \in \SOthree

* Closure: the product of any two rotation matrices is again a rotation matrix.

  .. math::

    \RotationMatrix_1 \RotationMatrix_2 \in \SOthree

* Associative: the order of multiplication for multiple rotation matrices is arbitrary, as long as the direction (left- or right multiplication) is the same.

  .. math::

    (\RotationMatrix_1 \RotationMatrix_2) \RotationMatrix_3 =
    \RotationMatrix_1 (\RotationMatrix_2 \RotationMatrix_3)

* Not commutative: in general the direction of multiplication of rotation matrices is not arbitrary.

  .. math::

    \RotationMatrix_1 \RotationMatrix_2 \neq \RotationMatrix_2 \RotationMatrix_1

* And, multiplying an arbitrary three dimensional vector with any rotation matrix will not change its length.

  .. math::

    x\in\mathbb{R}^3,\quad \Norm{\RotationMatrix x} = \Norm{x}


Rotation matrices (part 2 of 2)
===============================

.. raw:: html

  <iframe style="width: 695px; height: 390px;" src="https://www.youtube-nocookie.com/embed/6KIPusOv5fA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
