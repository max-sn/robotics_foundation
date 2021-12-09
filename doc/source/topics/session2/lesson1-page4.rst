.. role:: raw-html(raw)
  :format: html

Exponential coordinates of rotation
===================================

Exponential coordinates of rotation present an alternative to using a rotation matrix to express an orientation. We don't use them for that purpose however, but they can be used to keep track of a certain orientation by integrating the angular velocity. The following video gives the basics needed for that.

.. raw:: html

  <iframe style="width: 695px; height: 390px;" src="https://www.youtube-nocookie.com/embed/v_KBHaG0mas" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

The next video explains that when we know the axis of rotation (:math:`\UnitLength{\omega}`), and we know the vector that we want to track (:math:`p`), we can find an expression for :math:`p(t)` by solving the differential equation from the previous video, and using the skew-symmetric form of :math:`\TildeSkew{\UnitLength{\omega}}\theta` (note the *two* accents on :math:`\omega`) we find a closed form for the matrix exponential.

.. raw:: html

  <iframe style="width: 695px; height: 390px;" src="https://www.youtube-nocookie.com/embed/WHn9xJl43nY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Rodrigues' formula is the closed form solution of the series expansion of the matrix exponential, when the matrix in question is a three by three skew-symmetric matrix. We can use this formula to map an exponential coordinate representation of rotation (:math:`\UnitLength{\omega}\theta`), to a rotation matrix (:math:`\RotationMatrix`).

.. math::

  \RotationMatrix =
  \exp(\TildeSkew{\UnitLength{\omega}}\theta) =
  I + \TildeSkew{\UnitLength{\omega}}\sin\theta +
  \TildeSkew{\UnitLength{\omega}}^2(1-\cos\theta) \in \SOthree


Example
-------

Let's do a simple example. We start with as body frame :math:`\CoorSys{b}` and a space frame :math:`\CoorSys{s}` which initially are aligned. We rotate the body frame around the :math:`z`-axis of the space frame :math:`\CoorSys{s}` for :math:`\pi/3` radians. We would like to know the rotation matrix that expresses the new orientation of the body frame with respect to the space frame: :math:`\FromTo{b}{s}{\RotationMatrix}`.

* We know that the rotation axis is the :math:`z`-axis of the space frame. So:

  .. math::

    \UnitLength{\omega} =
    \begin{bmatrix}
      0 \\ 0 \\ 1
    \end{bmatrix}, \quad
    \TildeSkew{\UnitLength{\omega}} =
    \begin{bmatrix}
      0 & -1 & 0 \\
      1 & 0 & 0 \\
      0 & 0 & 0
    \end{bmatrix}, \quad
    \TildeSkew{\UnitLength{\omega}}^2 =
    \begin{bmatrix}
      -1 & 0 & 0 \\
      0 & -1 & 0 \\
      0 & 0 & 0
    \end{bmatrix}

* We also know :math:`\theta=\pi/3`. So:

  .. math::

    \TildeSkew{\UnitLength{\omega}} \sin \theta =
    \begin{bmatrix}
      0 & -\frac{\sqrt{3}}{2} & 0 \\
      \frac{\sqrt{3}}{2} & 0 & 0 \\
      0 & 0 & 0
    \end{bmatrix}, \quad
    \TildeSkew{\UnitLength{\omega}}^2 (1-\cos\theta) =
    \begin{bmatrix}
      -\frac{1}{2} & 0 & 0 \\
      0 & -\frac{1}{2} & 0 \\
      0 & 0 & 0
    \end{bmatrix}

* Then we can substitute these values in Rodrigues' formula, giving us the rotation matrix directly:

  .. math::

    \begin{align*}
      \FromTo{s}{b}{\RotationMatrix} &=
      \begin{bmatrix}
        1 & 0 & 0 \\
        0 & 1 & 0 \\
        0 & 0 & 1
      \end{bmatrix} +
      \begin{bmatrix}
        0 & -\frac{\sqrt{3}}{2} & 0 \\
        \frac{\sqrt{3}}{2} & 0 & 0 \\
        0 & 0 & 0
      \end{bmatrix} +
      \begin{bmatrix}
        -\frac{1}{2} & 0 & 0 \\
        0 & -\frac{1}{2} & 0 \\
        0 & 0 & 0
      \end{bmatrix}\\
      &=
      \begin{bmatrix}
        \frac{1}{2} & -\frac{\sqrt{3}}{2} & 0 \\
        \frac{\sqrt{3}}{2} & \frac{1}{2} & 0 \\
        0 & 0 & 1
      \end{bmatrix}
    \end{align*}


Code
----

Of course working this out with a 'simple' vector as above is not that hard, but it is cumbersome and prone to errors. Besides, in real applications we will not work with perfect :math:`[0,0,1]\Transposed` angular velocity, nor with perfect :math:`\pi/3` angles. When these numbers become less pretty, it is easier to use a software function to do the cumbersome part.

This course is accompanied by a `GitHub <https://github.com/max-sn/robotics_foundation/tree/develop>`__ repository with Python- and MATLAB functions that can be used to aid with these cumbersome calculations (be sure to look at the 'develop' branch which has the latest changes). Documentation can be found on `Read the Docs <https://robotics-foundation.readthedocs.io/>`__, and for this lesson, the :py:func:`~modern_robotics.num.vec_to_SO3` function (MATLAB: :mat:func:`~+MR.vec_to_SO3`) is particularly interesting. It uses Rodrigues' formula to 'integrate' over an angular velocity to find a rotation matrix. The same module also has the :py:func:`~modern_robotics.num.SO3_to_vec` function (MATLAB: :mat:func:`~+MR.SO3_to_vec`) that 'differentiates' a rotation matrix to find an angular velocity, using the matrix log. We will see later why this is useful.