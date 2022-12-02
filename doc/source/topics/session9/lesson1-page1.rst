Discrete time
=============

A distinction that we have to make when working with digital processing units, such as computers, is the distinction between continuous variables and discrete (quantized) variables. Because we treat signals typically as a certain variable *amplitude* as function of another variable *time*, we have four different kind of signals. The figure below shows how we can divide between them.

.. figure:: /_static/figures/session9/signals/signals-001.svg

  Four types of the same signal :math:`x(t)`, divided between continuous- and discrete amplitude, and continuous- and discrete time.
  
Signals with both continuous amplitude and continuous time are called *analog* signals and are generally what we encounter in the physical world. Signals with both discrete amplitude and discrete time are called *digital* signals and are typically what we encounter after measurements, but also in simulation. Sensors utilize power transformations between domains to transform a physical phenomenon to (typically) an electric signal, which in turn is quantized by an ADC (analog-digital converter) to make it applicable for digital processing units.


Signals
-------

.. rubric:: Unit step function

The discrete variant of :math:`u(t)`.

.. math::

  u[k] =
  \begin{cases}
    1 & k \geq 0 \\
    0 & k < 0 
  \end{cases}

.. rubric:: Kronecker delta function

The discrete variant of the Dirac delta function :math:`\delta(t)`.

.. math::

  \delta[k] =
  \begin{cases}
    1 & k = 0 \\
    0 & k \neq 0
  \end{cases}

Similar to the Dirac delta function's sifting property for integrals, the Kronecker delta function has the sifting property for sums, which also means that it is the neutral element for discrete convolution:

.. math::

  (x * \delta)[k] = \sum\limits_{n=-\infty}^{\infty} x[n] \delta[k - n] = x[k]


Sampling
--------

This process of digitizing an analog signal is called sampling of a signal and is often done at a fixed frequency called the *sampling frequency* :math:`\Frequency_s`.

Let's assume we have a continuous-time (analog) signal :math:`x_1(t)`:

.. math::

  x_1(t) = \Amplitude \cos\left(2\pi\Frequency t\right)

.. figure:: /_static/figures/session9/signals/signals-002.svg


If we were to sample this signal at a fixed sampling frequency :math:`\Frequency_s`, starting at time :math:`t=0`, the moments in time we would have a measurement of :math:`x_1(t)` would be in the set :math:`t\in {0, \Period_s, 2\Period_s,\ldots}` where :math:`\Period_s` is the sampling period :math:`\Period_s=\frac{1}{\Frequency_s}`. The sampled signal :math:`x_1[k]` would then be given by:

.. math::

  x_1[k] = \Amplitude \cos\left(2\pi\Frequency k \Period_s\right), \quad k\in 0,1,2,\ldots

.. figure:: /_static/figures/session9/signals/signals-003.svg

Now let's assume that we have another signal:

.. math::

  x_2(t) = \Amplitude \cos\left(2\pi (\Frequency + \Frequency_s) t\right)

The frequency of this signal is exactly the sampling frequency higher than our original signal's frequency :math:`\Frequency`. If we also sample this signal at the same sampling frequency :math:`\Frequency_s`, we get the following sample sequence:

.. math::

  \begin{align*}
    x_2[k] &= \Amplitude \cos\left(2\pi(\Frequency+\Frequency_s) k \Period_s\right) \\
    &= \Amplitude \cos\left(2\pi\Frequency k \Period_s+2\pi\Frequency_s k \Period_s\right) \\
  \end{align*}

Given that :math:`\Frequency_s=\frac{1}{\Period_s}\Rightarrow\Frequency_s\Period_s=1`:

.. math::

  \begin{align*}
    x_2[k] &= \Amplitude \cos\left(2\pi\Frequency k \Period_s+2\pi k \right) \\
    &= \Amplitude \cos\left(2\pi\Frequency k \Period_s\right)
  \end{align*}

Gives us the exact same sequence (recall that :math:`\cos(\phi + 2\pi k) = \cos(\phi)` for :math:`k\in 0,1,2,\ldots`). This can also be shown graphically:

.. figure:: /_static/figures/session9/signals/signals-004.svg

It is left as exercise for the reader to prove that this applies to all signals :math:`x^{\star}(t)=\cos(2\pi(\Frequency + n\Frequency_s)k\Period_s)` with :math:`n\in 0,1,2,\ldots`, e.g. :math:`x_3(t)=\cos(2\pi(\Frequency + 2\Frequency_s)k\Period_s)`:

.. figure:: /_static/figures/session9/signals/signals-005.svg


Now consider a new signal :math:`x_4(t)`, with a frequency that is equal to a quarter of the sampling frequency :math:`\Frequency=\frac{\Frequency_s}{4}`:

.. math::

  \begin{align*}
    y_1(t) &= \Amplitude \cos\left(2\pi\alpha\Frequency_s k\Period_s\right) \\
    &= \Amplitude \cos\left(2\pi\alpha k\right) \\
  \end{align*}

Where :math:`\alpha` is some value :math:`\alpha\in[0,0.5)`. If we compare this to another signal:

.. math::

  \begin{align*}
    y_2(t) &= \Amplitude \cos\left(2\pi(1-\alpha)\Frequency_s k\Period_s\right) \\
    &= \Amplitude \cos\left(2\pi k - 2\pi\alpha k\right) \\
    &= \Amplitude \cos\left(- 2\pi\alpha k\right) \\
    &= \Amplitude \cos\left(2\pi\alpha k\right) \\
  \end{align*}

Gives again the same sequence. Note that this does not only hold for the cosine wave, it also holds for the sine wave but with a certain additional phase shift. Apparently there is some symmetry around half the sampling frequency, and if the frequency increases above half the sampling frequency with a certain number, we get the same sample sequence as for a signal that has a frequency the same number *below* half the sampling frequency. This half of the sampling frequency is also known as the *folding frequency* or more commonly known as the *Nyquist frequency*.

Both of these properties of sampling are called *aliasing*, because various continuous-time signals are represented by the same sample sequence, they are aliases of each other in the discrete-time domain.

This aliasing phenomenon means that if you want to reconstruct the original signal :math:`x(t)` from the sample sequence :math:`x[k]`, there are various possible signals. In general we solve this by low-pass filtering the continuous-time signal before sampling, to make sure that no higher frequency signals are present, and choosing a sampling frequency which is sufficiently fast, i.e.:

.. math::

  \Frequency_s > 2\Frequency

Where :math:`\Frequency` is the highest expected frequency in the signal.
