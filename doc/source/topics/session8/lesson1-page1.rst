Signals
=======

Before we can take a closer look at the systems that we have seen so far, first we have to look at signals a bit. We can formally define a signal as a function :math:`x` that maps from a domain :math:`D` to a value. :math:`D` is interpreted as time, and if :math:`D` is an interval in the space of real numbers :math:`\mathbb{R}`, :math:`x` is a continuous signal, and if :math:`D` is a subset of the real integers :math:`\mathbb{Z}`, :math:`x` is a discrete signal. We denote discrete signals as sequences: :math:`x(k) = x[k]`.

.. figure:: /_static/figures/session8/signals/signals-001.svg

  Example of a continuous signal.

.. figure:: /_static/figures/session8/signals/signals-002.svg

  Example of a discrete signal.


Periodic signals
----------------

A signal is considered periodic with period :math:`\Period` if :math:`x(t+\Period)=x(t)` for all :math:`t`. For periodic signals the following properties hold:

* The period :math:`\Period` is a positive real number.
* If :math:`x` is periodic with period :math:`\Period`, then :math:`x` is periodic with period :math:`2\Period`, :math:`3\Period`, :math:`4\Period`, etc.
* If :math:`x` is periodic with period :math:`\Period`, then :math:`x(nt)` is periodic with :math:`\Period` for all positive integers :math:`n`.
* If :math:`x` and :math:`y` are both periodic with period :math:`\Period`, then
  * :math:`\alpha x + \beta y` is periodic with period :math:`\Period`,
  * :math:`x\cdot y` is periodic with period :math:`\Period`.
* If :math:`x` is periodic and :math:`f` is a function, then :math:`f(x(t))` is periodic.
* Constant functions are periodic.

Periodic signals have a frequency, which can be defined as: For a periodic signal :math:`x` with period :math:`\Period`, the number :math:`\Frequency = \frac{1}{T}` is called the frequency of :math:`x`, expressed in Hertz (:math:`\Unit{Hz}`). The number :math:`\AngularFrequency=\frac{2\pi}{T}` is called the angular frequency of :math:`x`, expressed in radians per second (:math:`\Unit{rad \cdot s^{-1}}`).

.. figure:: /_static/figures/session8/signals/signals-003.svg

  Example of a periodic signal with period :math:`\Period`.


Symmetry
--------

.. rubric:: Even

A function :math:`x(t)` is even if :math:`x(t)=x(-t)` for all :math:`t`.

.. figure:: /_static/figures/session8/signals/symmetry-001.svg

  Example of a non-periodic even function.

.. figure:: /_static/figures/session8/signals/symmetry-002.svg

  Example of a periodic even function.

.. figure:: /_static/figures/session8/signals/symmetry-003.svg

  Another example of a periodic even function.

.. rubric:: Odd

A function :math:`x(t)` is odd if :math:`x(t)=-x(-t)` for all :math:`t`.

.. figure:: /_static/figures/session8/signals/symmetry-004.svg

  Example of a non-periodic odd function.

.. figure:: /_static/figures/session8/signals/symmetry-005.svg

  Example of a periodic odd function.

.. figure:: /_static/figures/session8/signals/symmetry-006.svg

  Another example of a periodic odd function.

.. rubric:: Half-wave odd

A *periodic* signal :math:`x(t)` is half-wave odd if :math:`x(t)=-x(t + \frac{\Period}{2})`.

.. figure:: /_static/figures/session8/signals/symmetry-007.svg

  Example of a periodic half-wave odd function.


Basic functions to build signals
--------------------------------

.. rubric:: Unit step function

Defined as:

.. math::

  \step(t) =
  \begin{cases}
    1, & t > 0, \\
    0, & t < 0.
  \end{cases}

The domain around :math:`t=0` is shown in the figure below.

.. figure:: /_static/figures/session8/signals/signals-004.svg

  Unit step function :math:`\step(t)`.

Note that it is not defined at time :math:`t=0`, but approaches :math:`t=0` from the left at :math:`0` and from the right at :math:`1`, indicated by the arrows. If a signal is undefined at a certain time :math:`t`, but both left- and right limits (respectively :math:`x(t^-)` and :math:`x(t^+)`) exist, we choose to define :math:`x(t)=\frac{1}{2}\left(x(t^-) + x(t^+)\right)`. For the unit step function that is:

.. math::

  \step(0) = \frac{1}{2}\left(\step(0^-) + \step(0^+)\right) = \frac{1}{2}

The unit step function is also known as the *Heaviside* step function and is sometimes denoted with :math:`H(t)` or :math:`\theta(t)`, but since we already used these symbols for other variables, we'll keep using :math:`\step(t)` for clarity.

.. rubric:: Rectangular pulse

Defined as:

.. math::

  \rect(t) =
  \begin{cases}
    0, & \Abs{t} > \frac{1}{2}, \\
    1, & \Abs{t} < \frac{1}{2}.
  \end{cases}


.. figure:: /_static/figures/session8/signals/signals-005.svg

  Rectangular pulse function :math:`\rect(t)`.

The :math:`\rect(t)` function can be constructed from the unit step as follows: :math:`\rect(t) = \step(t+\frac{1}{2})\step(-t-\frac{1}{2})`.

.. rubric:: Signum function

Defined as:

.. math::

  \sgn(t) =
  \begin{cases}
    1, & t > 0, \\
    0, & t = 0, \\
    -1, & t < 0.
  \end{cases}

.. figure:: /_static/figures/session8/signals/signals-006.svg

  Signum function :math:`\sgn(t)`.

The :math:`\sgn(t)` function can be constructed from the unit step as follows: :math:`\sgn(t) = 2\step(t)-1`.


.. rubric:: Ramp function

Defined as:

.. math::

  \ramp(t) =
  \begin{cases}
    t, & t \geq 0, \\
    0, & t < 0.
  \end{cases}

.. figure:: /_static/figures/session8/signals/signals-007.svg

  Ramp function :math:`\ramp(t)`.

The :math:`\ramp(t)` function can be constructed from the unit step function as follows: :math:`\ramp(t) = t \step(t)`.

.. rubric:: Dirac delta 'function'

A special kind of signal is the Dirac delta function, which is technically not a function. It is defined by the following properties:

1. :math:`\delta(0) = \infty`,
2. :math:`\delta(t) = 0` for all :math:`t\neq 0`,
3. :math:`\int_{-\infty}^{\infty}\delta(t) \DeltaD t = 1`,
4. :math:`\delta(t)` is an even function.

We can approximate by taking a unit area rectangular pulse, and take the limit of its width approaching :math:`0`, in the following figure that is: :math:`\lim\limits_{\epsilon\rightarrow 0} \frac{1}{\epsilon}\rect(\frac{t}{\epsilon})`.

.. figure:: /_static/figures/session8/signals/signals-008.svg

  Dirac delta function defined as a pulse with width approaching zero.

The area under the pulse will remain :math:`\epsilon \frac{1}{\epsilon}=1`, and the height will become infinitely large.

The Dirac delta function is denoted by means of a vertical arrow, and it can be shifted, scaled, and negatively scaled. The scaling factor is also knows as the 'strength' of the pulse.

.. figure:: /_static/figures/session8/signals/signals-009.svg

  Differently scaled and shifted Dirac delta functions.

A peculiar and useful property of the Dirac delta function is the 'sifting' property. It is defined as follows:

.. math::

  \int\limits_{t_1}^{t_2} x(t)\delta(t - t_0) \DeltaD t =
  \begin{cases}
    x(t_0), & t_1 < t_0 < t_2, \\
    0, & \text{otherwise}
  \end{cases}

We will see later why this is useful.


Convolution
===========

Besides a deeper understanding of signals and their properties, we also need another operation for signals, namely convolution.

Let :math:`x` and :math:`y` be two continuous time signals defined on :math:`\mathbb{R}`. The convolution of :math:`x` and :math:`y` is defined as

.. math::

  x * y = \int\limits_{-\infty}^{\infty} x(\tau) y(t-\tau) \DeltaD \tau

The result is again a continuous time signal. Convolution has the following properties:

* :math:`x * y = y * x` commutativity
* :math:`x * (y * z) = (x * y) * z` associativity
* :math:`x * (y + z) = x * y + x * z` distributivity
* :math:`x*(\alpha y) = \alpha(x * y)` linearity

For convolution, the Dirac delta function is the so-called *neutral element*, because :math:`x*\delta = \delta*x = x`. This follows directly from the 'sifting' property:

.. math::

  \begin{align*}
    x(t) * \delta(t) &= \int\limits_{-\infty}^{\infty} x(\tau) \delta(t-\tau) \DeltaD \tau \\
    &= \int\limits_{-\infty}^{\infty} x(\tau) \delta(\tau-t) \DeltaD \tau \\
    &= x(t)
  \end{align*}

We can swap :math:`t-\tau` with :math:`\tau-t` because the Dirac delta function is even, so :math:`\delta(t)=\delta(-t)`.


.. admonition:: Example

  Let's use two unit step functions as an example. For one of the step functions we substitute :math:`t` with :math:`t - \tau`, and we multiply both functions. We can visualize the result as follows, where we change :math:`t` and look at the different signals:

  .. raw:: html

    <figure class="align-default" id="convolution-anim-1">
      <object data="/_static/figures/session8/convolution1/master.svg" type="image/svg+xml" width="650px"></object>
      <figcaption>
        <p><span class="caption-text">Animation showing the convolution of two unit step functions.</span><a class="headerlink" href="#convolution-anim-1" title="Permalink to this image"></a></p>
      </figcaption>
    </figure>

  The bottom-right graph is the result of the convolution, which is nothing more than the area under the third graph.

  Another example is the convolution of a unit step function with the ramp function. Again we change :math:`t` and look at the different signals:

  .. raw:: html

    <figure class="align-default" id="convolution-anim-2">
      <object data="/_static/figures/session8/convolution2/master.svg" type="image/svg+xml" width="650px"></object>
      <figcaption>
        <p><span class="caption-text">Animation showing the convolution of a unit step function with a ramp function.</span><a class="headerlink" href="#convolution-anim-2" title="Permalink to this image"></a></p>
      </figcaption>
    </figure>

Before we can understand exactly how and why convolution is so important, we have to dive a little deeper into systems. We will do that on the next page.


Code example
------------

With MATLAB or numpy you can do numerical convolution of sampled signals. Note that no actual time information is used in the convolution functions, the time between samples is assumed to be unit length. This means that the result should be scaled with the time step duration.

See the following example. Can you explain why there is a downward ramp on the right of the resulting signal?

.. tab-set::

  .. tab-item:: Python
    :sync: PYTHON

    .. code-block:: python
      
      import numpy as np
      import matplotlib.pyplot as plt


      def step(t):
          return (t > 0).astype(np.float)


      def rect(t):
          return step(t+1/2) * step(-t+1/2)


      dur = 5           # uni-lateral time length
      N = 101           # number of samples
      dt = dur/(N - 1)  # time step duration

      t = np.linspace(-dur, dur, N)
      x = step(t)
      y = rect(t)

      xy = dt * np.convolve(x, y, mode='same')

      plt.plot(t, xy)
  
  .. tab-item:: MATLAB
    :sync: MATLAB

    .. code-block:: matlab

      dur = 5;           % uni-lateral time length
      N = 101;           % number of samples
      dt = dur/(N - 1);  % time step duration

      t = linspace(-5, 5, 101);
      x = step(t);
      y = rect(t);

      xy = conv(x, y, 'same');

      plot(t, xy)

      function x = step(t)
          x = double(t > 0);
      end

      function x = rect(t)
          x = step(t+1/2) .* step(-t+1/2);
      end
