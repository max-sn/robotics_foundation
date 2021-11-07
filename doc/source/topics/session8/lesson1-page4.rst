Laplace
=======

Where the Fourier transform is outstanding at describing continuous *signals*, we are also (maybe even more) interested in describing the behaviour of *systems*. Since the nature of physical systems often includes some kind of damping, which can be seen as a decay of signals, and since decaying signals are *possible* with the Fourier transform, but not necessarily efficient, we can introduce a different transformation which also takes into account the decay of signals, as exponential function. We call this transform the *Laplace* transform, for a signal :math:`x(t)` denoted with :math:`\LaplaceTransform{x(t)}`. The following video goes through the fundamentals.

.. raw:: html

  <iframe style="width: 695px; height: 390px;" src="https://www.youtube-nocookie.com/embed/ZGPtPkTft8g" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Contrary to the transform denoted in the video, we typically use the following definition of the Laplace transform, which only considers the part of the function that occurs in non-negative time. The :math:`0^-` indicates that the lower bound should be approached from the lower value, but this only matters when dealing with the Dirac delta function. Besides, we will not try to solve this integral ourselves.

.. math::

  \LaplaceTransform{x(t)} = X(s) = \int\limits_{0^-}^{\infty} x(t) \exp(-st) \DeltaD t

Where :math:`s` is the complex variable :math:`s=\sigma+i\AngularFrequency` (recall that :math:`\AngularFrequency` was the angular frequency, :math:`\AngularFrequency=2\pi\Frequency`). Using this transform gives us a whole lot of additional information about a system (with its impulse response) or a signal.

It is very closely related to the Fourier transform, e.g. compare the following two definitions (note that here we use the angular frequency :math:`\AngularFrequency` instead of the frequency :math:`\Frequency` for the Fourier transform):

.. math::

  \begin{align*}
    \LaplaceTransform{x(t)} = X(s) &= \int\limits_{0^-}^{\infty} x(t) \exp(-s t) \DeltaD t \\
    &= \int\limits_{0^-}^{\infty} x(t) \exp(-(\sigma + i \AngularFrequency) t) \DeltaD t \\
    &= \int\limits_{0^-}^{\infty} x(t) {\color{red}{\exp(-\sigma t)}}\exp(-i\AngularFrequency t) \DeltaD t \\
    \FourierTransform{x(t)} = X(\AngularFrequency) &= \int\limits_{-\infty}^{\infty} x(t) \exp(-i \AngularFrequency t) \DeltaD t
  \end{align*}

The exponential in red is added with respect to the Fourier transform, this takes care of the natural decay of signals. In fact, the Fourier transform is a special case of the Laplace transform where the real part of :math:`s` is zero. Note that the Laplace transform maps a function to the *complex* frequency domain, whereas the Fourier transform maps to the *imaginary* frequency domain only. In general we call both *the frequency domain*.


Applications of the Laplace transform
-------------------------------------

Great thing about the Laplace transform is that the properties that were true for the Fourier transform, are also true for the Laplace transform.

.. rubric:: Convolution

Convolution in the frequency domain is still a multiplication. Given two functions :math:`x(t)` and :math:`y(t)` and their respective Laplace transformations :math:`X(s)` and :math:`Y(s)`, the following holds:

.. math::

  \LaplaceTransform{x * y} = X(s)Y(s)

.. rubric:: Differentiation

Let :math:`x(t)` be a smooth signal with corresponding Laplace transform :math:`X(s)` and assume that :math:`\lim\limits_{t\rightarrow\infty}x(t)=0` and :math:`\lim\limits_{t\rightarrow-\infty}x(t)=0`. Then :math:`\LaplaceTransform{\dot{x}(t)}` exists and:

.. math::

  \LaplaceTransform{\dot{x}(t)} = sX(s)

.. rubric:: Integration

Let :math:`x(t)` be a continuous, integrable signal with corresponding Laplace transform :math:`X(s)`, if :math:`X(0)=0` then:

.. math::

  \LaplaceTransform{\int_{-\infty}^{t} x(\tau) \DeltaD \tau} = \frac{1}{s} X(s)

.. rubric:: Impulse response

For an LTI system, the response to any arbitrary input is defined by the impulse response :math:`h(t)`. If the input is :math:`x(t)` then:

.. math::

  y(t) = (x * h)(t)

We can define the Fourier transform of the impulse response as *transfer function* :math:`H(s)=\LaplaceTransform{h(t)}` of the LTI system, then:

.. math::

  Y(s) = X(s) H(s)


Example
-------

Let's take the following circuit.

.. figure:: /_static/figures/session8/iRC_example/iRC_example-001.svg

From this we can construct the following bond graph.

.. figure:: /_static/figures/session8/iRC_example/iRC_example-002.svg

And in turn the following block diagram.

.. figure:: /_static/figures/session8/iRC_example/iRC_example-003.svg

We can re-order the blocks to get a shape that is more readable (even though the relation between the power variables flow and effort of the components is less intuitive now).

.. figure:: /_static/figures/session8/iRC_example/iRC_example-004.svg

From this diagram we can find the differential equation that describes the system's behaviour.

.. math::

  \begin{align*}
    x(t) = i(t) &= C\Diff{u(t)} + \frac{u(t)}{R} \\
    &= C\Diff{y(t)} + \frac{y(t)}{R} \\
  \end{align*}

Now if we assume that the Laplace transform of :math:`x(t)` exists and is :math:`X(s)`, we can transform the entire equation (note how we use a single :math:`s` for the differential of :math:`y(t)`):

.. math::

  \begin{align*}
    X(s) &= C Y(s) s +  \frac{1}{R} Y(s) \\
    &= \left(Cs + \frac{1}{R}\right) Y(s)
  \end{align*}

And rewriting the identity :math:`Y(s) = X(s) H(s)` to :math:`H(s)=\frac{Y(s)}{X(s)}`, we get the transfer function as:

.. math::

  \begin{align*}
    \frac{X(s)}{Y(s)} &= Cx + \frac{1}{R} \\
    \frac{Y(s)}{X(s)} = H(s) &= \frac{1}{Cs + \frac{1}{R}}
  \end{align*}

Using a symbolic solving engine to solve the inverse Laplace transform of :math:`H(s)` we get:

.. math::

  h(t) = \iLaplaceTransform{H(s)} = \step(t)\frac{1}{C}\exp\left(\frac{-t}{RC}\right)

Where the unit step function :math:`\step(t)` ensures that the system response is causal, so zero up to time :math:`t=0`. Depending on which symbolic solver you use, the step function might or might not be included, because the Laplace transform already assumes that the original signal had no value before time :math:`t=0`. MATLAB and Maple do not include it, sympy does. The impulse response is shown below, and the impulse response without step function is included as dashed line.

.. figure:: /_static/figures/session8/impulse_response/impulse_response-001.svg

  Impulse response.


Standard functions Laplace transforms
-------------------------------------

Using the following table, you can find the (inverse) Laplace transforms of some common functions. Most functions that are more complex can be constructed as a combination of those listed here. Fractions in the frequency domain with higher order polynomials in the numerator or denominator can be first split by applying partial fractions expansion, e.g. by using ``〈expression〉.apart()`` for sympy or ``partfrac(〈expression〉)`` for MATLAB.

.. list-table::
  :header-rows: 1

  * - Time domain signal :math:`x(t)`
    - Frequency domain signal :math:`X(s)`
  * - .. math::
        0
    - .. math::
        0
  * - .. math::
        1
    - .. math::
        \frac{1}{s}
  * - .. math::
        t
    - .. math::
        \frac{1}{s^2}
  * - .. math::
        \exp(-\alpha t)
    - .. math::
        \frac{1}{s+\alpha}
  * - .. math::
        t\exp(-\alpha t)
    - .. math::
        \frac{1}{\left(s + \alpha\right)^2}
  * - .. math::
        \sin(\AngularFrequency t)
    - .. math::
        \frac{\AngularFrequency}{s^2 + \AngularFrequency^2}
  * - .. math::
        \cos(\AngularFrequency t)
    - .. math::
        \frac{s}{s^2 + \AngularFrequency^2}
  * - .. math::
        1-\exp(-\alpha t)
    - .. math::
        \frac{\alpha}{s(s+\alpha)}
  * - .. math::
        \exp(-\alpha t)\sin(\AngularFrequency t)
    - .. math::
        \frac{\AngularFrequency}{\AngularFrequency^2 + (\alpha + s)^2}
  * - .. math::
        \exp(-\alpha t)\cos(\AngularFrequency t)
    - .. math::
        \frac{\alpha + s}{\AngularFrequency^2 + (\alpha + s)^2}
