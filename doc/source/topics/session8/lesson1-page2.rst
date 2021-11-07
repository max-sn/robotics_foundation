LTI systems
===========

We have already seen various examples of systems that we can model, all of them ideal representations of real world physical systems. For the following lesson, it is important to note what kind of systems we are typically dealing with when modelling real world physical systems. 

An important subset of systems in modelling and simulation is the set of LTI (linear time-invariant) systems. If a system is considered as a unique mapping from a certain input :math:`x(t)` to a certain output :math:`y(t)`, the properties 'linearity' and 'time-invariance' can be described as follows.

.. rubric:: Linearity

A system is considered linear if and only if: For arbitrary input :math:`x_1(t)` and :math:`x_2(t)` with corresponding output (response) :math:`y_1(t)` and :math:`y_2(t)`, and for an arbitrary constant :math:`\alpha` the following holds:

1. the response to :math:`x_1(t)+x_2(t)` is :math:`y_1(t)+y_2(t)`; and
2. the response to :math:`\alpha x_1(t)` is :math:`\alpha y_1(t)`.

As example, the differentiator is a system that differentiates its input to get its output. Let :math:`y_1(t)=\dot{x}_1(t)` and :math:`y_2(t)=\dot{x}_2(t)`. The response to :math:`x_1(t) + x_2(t)` is:

.. math::

  \begin{align*}
    \Diff{(x_1(t) + x_2(t))} &= \dot{x}_1(t) + \dot{x}_2(t) \\
    &= y_1(t) + y_2(t)
  \end{align*}

And the response to :math:`\alpha x_1(t)` is:

.. math::

  \begin{align*}
    \Diff{(\alpha x_1(t))} &= \alpha\Diff{x_1(t)} \\
    &= \alpha \dot{x}_1(t) \\
    &= \alpha y_1(t)
  \end{align*}

The differentiator complies to both requirements, therefore it is linear.

Another example is the system with :math:`y(t) = x(t) + 2`. Let :math:`y_1(t)=x_1(t) + 2` and :math:`y_2(t)=x_2(t)+2`. The response to :math:`x_1(t) + x_2(t)` is:

.. math::

  \begin{align*}
    (x_1(t) + x_2(t)) + 2 &= x_1(t) + x_2(t) + 2 \\
    &\neq y_1(t) + y_2(t)
  \end{align*}

Therefore this system is not linear.

.. rubric:: Time-invariance

A system is considered time-invariant if and only if: For an arbitrary input :math:`x(t)` and corresponding output (response) :math:`y(t)`, and for all constants :math:`t_0`, the response to :math:`x(t-t_0)` is :math:`y(t-t_0)`.

As example, consider the system with :math:`y(t)=\cos(x(t))`. The response to :math:`x_1(t)=x(t-t_0)` is:

.. math::

  \begin{align*}
    y_1(t) &= \cos(x_1(t)) \\
    &= \cos(x(t-t_0)) \\
    &= y(t-t_0)
  \end{align*}

It complies to the time-invariance requirement, so it is time-invariant.

A convenient property of LTI systems, is that sinusoidal signals that are processed by an LTI system, don't change shape. They can be phase shifted or scaled, but note that even integrating or differentiating a sinusoid still returns a sinusoid.


Impulse response
----------------

The behaviour of an LTI system is completely determined by its impulse response :math:`h(t)`. We define the impulse response as the response that the system has when the input is :math:`\delta(t)`.

The response of an LTI system to any arbitrary input :math:`x(t)` can then be determined by the convolution of the input signal with the impulse response:

.. math::

  y(t) = x(t) * h(t)

Following the example of the gain block, that is:

.. math::

  y(t) = x(t) * (C\delta(t)) = C(x * \delta)(t) = Cx(t)

Another example: the integrator block, defined as (note that :math:`x` is still a function of time, but to integrate it we pass the integration variable :math:`\tau` as variable):

.. math::

  y(t) = \int\limits_{-\infty}^{t} x(\tau) \DeltaD \tau

To find the impulse response we apply :math:`\delta(t)` as input, and see what the response (output) is.

.. math::

  h(t) = \int\limits_{-\infty}^{t} \delta(\tau) \DeltaD \tau

The outcome depends on whether :math:`0` is in the range :math:`(-\infty, t)` or not. If :math:`t < 0`, it is not, which means that :math:`h` will be zero. If :math:`t > 0` we can find :math:`h` with the sifting property:

.. math::

  \int\limits_{-\infty}^{t} \delta(\tau) \DeltaD \tau = \int\limits_{-\infty}^{t} 1 \cdot \delta(\tau) \DeltaD \tau = 1

So :math:`h(t)` is:

.. math::

  \begin{align*}
    h(t) &=
    \begin{cases}
      0, & t < 0, \\
      1, & t > 0
    \end{cases} \\
    &= u(t)
  \end{align*}

So the impulse response of the integrator system is the unit step function :math:`u(t)`. This follows from the fact that the unit step function is the integral (or anti-derivative) of the Dirac delta function, and vice-versa the derivative of the unit step function is the Dirac delta function.
