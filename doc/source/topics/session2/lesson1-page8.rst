
Wrenches
========

.. role:: raw-html(raw)
  :format: html

.. raw:: html

  <iframe style="width: 695px; height: 390px;" src="https://www.youtube-nocookie.com/embed/0wsYPJPGtKE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Since wrenches are the dual of twists, we consider them to be co-vectors instead of vectors. This means that where the video above uses a *column* array for a wrench, we construct a wrench as follows in a *row* array:

.. math::

  \To{b}{\Wrench}=
  \begin{bmatrix}
    \To{b}{m} & \To{b}{f}
  \end{bmatrix}

Where both :math:`\To{b}{m}` and :math:`\To{b}{f}` are :math:`1\times 3` row arrays, such that :math:`\To{b}{\Wrench}\in\mathbb{R}^{1\times6}`.

As dual of twists, wrenches present a mapping from the twist space to the scalar power. Therefore, we can use the adjoint representation of the transformation matrix again to change reference frames for wrenches. Keep in mind that the scalar power should be independent of the chosen reference frames, so for any reference frame the product of twist and wrench should give the same scalar number.

.. math::

  \begin{align*}
    &\To{s}{\Wrench} \To{s}{\Twist} &&= \To{b}{\Wrench} \To{b}{\Twist} &= P \\
    &\begin{bmatrix}
      \To{s}{m} & \To{s}{f}
    \end{bmatrix}
    \begin{bmatrix}
      \To{s}{\omega} \\ \To{s}{v}
    \end{bmatrix} &&=
    \begin{bmatrix}
      \To{b}{m} & \To{b}{f}
    \end{bmatrix}
    \begin{bmatrix}
      \To{b}{\omega} \\ \To{b}{v}
    \end{bmatrix} &= P
  \end{align*}

We use the following equation to change reference frame for a twist:

.. math::

  \To{s}{\Twist} = \Adjoint{\FromTo{b}{s}{\HomogeneousTransformationMatrix}} \To{b}{\Twist}

Substituting this in the power equation above, gives us:

.. math::

  \To{b}{\Wrench}\To{b}{\Twist} = \To{s}{\Wrench}\Adjoint{\FromTo{b}{s}{\HomogeneousTransformationMatrix}} \To{b}{\Twist}

We cannot simply divide by :math:`\To{b}{\Twist}` on both sides of the equation, but we know that this equation must hold for any twist in any reference frame. Therefore we can write this as:

.. math::

  \To{b}{\Wrench} = \To{s}{\Wrench}\Adjoint{\FromTo{b}{s}{\HomogeneousTransformationMatrix}}

Transposing both sides of the equation gives us the following, which is similar to the form used in the video. In this form however, the matching sub- and superscript that we are used to from transforming coordinates, transformation matrices, and twists, no longer holds. That is why we prefer the previous form.

.. math::

  \left(\To{b}{\Wrench}\right)\Transposed =
  \Adjoint{\FromTo{b}{s}{\HomogeneousTransformationMatrix}}\Transposed
  \left(\To{s}{\Wrench}\right)\Transposed


Example
-------

Let's have a look at the following example. A wrench is used to tighten a bolt by applying a linear force at the end. We define a coordinate frame :math:`\CoorSys{e}` at the end of the wrench, which is aligned with the wrench itself, which in turn is rotated with :math:`\pi/6\Unit{rad}` with respect to the world frame.

.. figure:: /_static/figures/session2/wrench/wrench.svg

  Applying linear force on a wrench creates a moment.

We use the coordinate frame :math:`\CoorSys{e}` to express the force :math:`f` as a wrench. The linear part can be expressed as:

.. math::

  \To{e}{\Wrench}_f = 10
  \begin{bmatrix}
    \cos(-\frac{4\pi}{6}) & \sin(-\frac{4\pi}{6}) & 0
  \end{bmatrix} =
  \begin{bmatrix}
    -5 & -5\sqrt{3} & 0
  \end{bmatrix}

The angular part of the wrench is zero, because the force passes through the origin of the coordinate frame in which we are expressing it.

.. math::

  \To{e}{\Wrench}_m =
  \begin{bmatrix}
    0 & 0 & 0
  \end{bmatrix}

The total wrench therefore is:

.. math::

  \To{e}{\Wrench} =
  \begin{bmatrix}
    0 & 0 & 0 & -5 & -5\sqrt{3} & 0
  \end{bmatrix}

Now if we want to find how that force is experienced by the bolt, we have to transform this wrench to the space frame :math:`\CoorSys{s}`. For that we need the transformation :math:`\FromTo{s}{e}{\HomogeneousTransformationMatrix}`. Notice the difference with transforming velocity twists, where we would use :math:`\FromTo{e}{s}{\HomogeneousTransformationMatrix}` to transform from :math:`\CoorSys{e}` to :math:`\CoorSys{s}`.

To find :math:`\FromTo{s}{e}{\HomogeneousTransformationMatrix}`, it is easiest to first find :math:`\FromTo{e}{s}{\HomogeneousTransformationMatrix}`, and then invert it. To get from the :math:`\CoorSys{s}` frame to the :math:`\CoorSys{e}` frame, we first rotate by :math:`\pi/6\Unit{rad}` around :math:`\UnitLength{z}`, and then move along the rotated :math:`\UnitLength{x}`-axis for :math:`0.2\Unit{m}`. Both transformations are expressed in the space frame, so should be applied as right-multiplication:

.. math::

  \begin{align*}
    \FromTo{e}{s}{\HomogeneousTransformationMatrix} &=
    \begin{bmatrix}
      \frac{1}{2}\sqrt{3} & -\frac{1}{2} & 0 & 0 \\
      \frac{1}{2} & \frac{1}{2}\sqrt{3} & 0 & 0 \\
      0 & 0 & 1 & 0 \\
      0 & 0 & 0 & 1
    \end{bmatrix}
    \begin{bmatrix}
      1 & 0 & 0 & \frac{1}{5} \\
      0 & 1 & 0 & 0 \\
      0 & 0 & 1 & 0 \\
      0 & 0 & 0 & 1
    \end{bmatrix}\\
    &=
    \begin{bmatrix}
      \frac{1}{2}\sqrt{3} & -\frac{1}{2} & 0 & \frac{1}{10}\sqrt{3} \\
      \frac{1}{2} & \frac{1}{2}\sqrt{3} & 0 & \frac{1}{10} \\
      0 & 0 & 1 & 0 \\
      0 & 0 & 0 & 1
    \end{bmatrix}
  \end{align*}

Inverting (using :raw-html:`<a href="https://robotics-foundation.readthedocs.io/en/latest/python.html#modern_robotics.inv_SE3"><code>inv_SE3</code></a>`) gives us:

.. math::

  \FromTo{s}{e}{\HomogeneousTransformationMatrix} =
  \begin{bmatrix}
    \frac{1}{2}\sqrt{3} & \frac{1}{2} & 0 & -\frac{1}{5} \\
    -\frac{1}{2} & \frac{1}{2}\sqrt{3} & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 1
  \end{bmatrix}

Now it is fairly easy to construct the Adjoint of :math:`\FromTo{s}{e}{\HomogeneousTransformationMatrix}` (using :raw-html:`<a href="https://robotics-foundation.readthedocs.io/en/latest/python.html#modern_robotics.big_adjoint"><code>big_adjoint</code></a>`):

.. math::

  \Adjoint{\FromTo{s}{e}{\HomogeneousTransformationMatrix}} =
  \begin{bmatrix}
    \frac{1}{2}\sqrt{3} & \frac{1}{2} & 0 & 0 & 0 & 0 \\
    -\frac{1}{2} & \frac{1}{2}\sqrt{3} & 0 & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 & 0 & 0 \\
    0 & 0 & 0 & \frac{1}{2}\sqrt{3} & \frac{1}{2} & 0 \\
    0 & 0 & \frac{1}{5} & -\frac{1}{2} & \frac{1}{2}\sqrt{3} & 0 \\
    \frac{1}{10} & -\frac{1}{10}\sqrt{3} & 0 & 0 & 0 & 1 \\
  \end{bmatrix}

Finally we can use this to transfer :math:`\To{e}{\Wrench}` to :math:`\CoorSys{s}`. Note that the sub- and superscript match again if we use this form of the equation.

.. math::

  \begin{align*}
    \To{s}{\Wrench} &= \To{e}{\Wrench} \Adjoint{\FromTo{s}{e}{\HomogeneousTransformationMatrix}} \\
    &=
    \begin{bmatrix}
      0 & 0 & -\sqrt{3} & 0 & -10 & 0
    \end{bmatrix}
  \end{align*}


Code
----

This complete example can be done with the functions from this repository as follows:

.. tab-set::

  .. tab-item:: Python
    :sync: PYTHON

    .. tab-set:: 

      .. tab-item:: Symbolic
        :sync: PYTHON-SYM

        .. code-block:: python

          import sympy as sp
          import modern_robotics.sym as mr

          # Note that we can use sympify to let sympy parse a string for us. If we use
          # sp.Matrix([[0, 0, 0, -5, -5*3**0.5, 0]]) directly, it will first calculate
          # -5*3**0.5 before sympy can make a symbolic expression.
          Fb = sp.sympify("Matrix([[0, 0, 0, -5, -5*sqrt(3), 0]])")

          R = mr.vec_to_SO3(sp.Matrix([0, 0, sp.pi/6]))
          # Similarly we use sympify to get 1/5 in our vector instead of 0.2.
          p = sp.sympify("Matrix([1/5, 0, 0])")

          TRz = mr.R_p_to_SE3(R, sp.zeros(3, 1))
          Ttx = mr.R_p_to_SE3(sp.eye(3), p)

          Tse = TRz * Ttx

          Tes = mr.inv_SE3(Tse)

          Fs = Fb * mr.big_adjoint(Tes)

          print(Fs)

      .. tab-item:: Numeric
        :sync: PYTHON-NUM

        .. code-block:: python

          import numpy as np
          import modern_robotics.num as mr

          # Note that '**' is used as 'to the power' operator in Python, e.g. 3**0.5 is
          # sqrt(3)
          Fb = np.array([[0, 0, 0, -5, -5*3**0.5, 0]])

          R = mr.vec_to_SO3(np.array([[0], [0], [np.pi/6]]))
          p = np.array([[0.2], [0], [0]])

          TRz = mr.R_p_to_SE3(R, np.zeros((3, 1)))
          Ttx = mr.R_p_to_SE3(np.eye(3), p)

          # Note the '@' which indicates the 'matrix product' when using numpy arrays.
          Tse = TRz @ Ttx

          Tes = mr.inv_SE3(Tse)

          # Note the '@' which indicates the 'matrix product' when using numpy arrays.
          Fs = Fb @ mr.big_adjoint(Tes)

          print(Fs)

  .. tab-item:: MATLAB
    :sync: MATLAB

    .. code-block:: matlab

      Fb = [0, 0, 0, -5, -5*sqrt(3), 0];

      R = MR.vec_to_SO3([0; 0; pi/6]);
      p = [0.2; 0; 0];

      TRz = MR.R_p_to_SE3(R, zeros(3,1));
      Ttx = MR.R_p_to_SE3(eye(3), p);

      Tse = TRz * Ttx;

      Tes = MR.inv_SE3(Tse);

      Fs = Fb * MR.big_adjoint(Tes);

      disp(Fs)