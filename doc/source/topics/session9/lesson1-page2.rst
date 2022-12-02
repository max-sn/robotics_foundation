Discrete-time Fourier transform and :math:`z`-transform
=======================================================

Recall that the continuous-time Fourier transform (CTFT) was:

.. math::

  \FourierTransform{x(t)} = X(\AngularFrequency) = \int\limits_{-\infty}^{\infty} x(t) \exp(-i\AngularFrequency t) \DeltaD t

If the signal :math:`x(t)` instead is a sample sequence :math:`x[k]`, the infinite integral turns into an infinite sum instead, giving:

.. math::

  \FourierTransform{x[k]} = X(\AngularFrequency) = \sum\limits_{k=-\infty}^{\infty} x[k] \exp(-i\AngularFrequency k)

Which is referred to the *Discrete-time Fourier transform* (DTFT). The results is still a continuous-frequency function, mapping the sample sequence :math:`x[k]` to the imaginary axis of the complex frequency plane.

Also, we could generalize the CTFT to map continuous-time systems to the complete complex frequency plane, by adding another exponential term and thereby defining the Laplace transform:

.. math::

  \LaplaceTransform{x(t)} = X(s) = \int\limits_{-\infty}^{\infty} x(t) \exp(-st) \DeltaD t

For discrete-time systems, there is an equivalent transform, called the z-transform. This maps discrete-time systems to a *different* complex frequency domain, so we will refer to that as the z-domain, after the complex variable :math:`z`. The z-transform is defined as:

.. math::

  \ZTransform{x[k]} = X(z) = \sum\limits_{k=-\infty}^{\infty} x[k] z^{-k}

Recall that we could find the response of a system to a certain input by convoluting it with the impulse response of the system:

.. math::

  y(t) = (h * x)(t)

Now suppose we choose :math:`x(t)=\exp(i\AngularFrequency t)`, by applying the convolution integral we get the following:

.. math::

  \begin{align*}
    y(t) &= \int\limits_{-\infty}^{\infty} h(\tau) x(t - \tau) \DeltaD \tau \\
    &= \int\limits_{-\infty}^{\infty} h(\tau) \exp(i\AngularFrequency(t - \tau)) \DeltaD \tau \\
    &= \int\limits_{-\infty}^{\infty} h(\tau) \exp(i\AngularFrequency t)\exp(- i\AngularFrequency\tau) \DeltaD \tau \\
    &= \underbrace{\exp(i\AngularFrequency t)}_{x(t)} \underbrace{\int\limits_{-\infty}^{\infty} h(\tau) \exp(- i\AngularFrequency\tau) \DeltaD \tau}_{H(\AngularFrequency)}
  \end{align*}

Where we can recognize that the output is a modulation of the input, with the transfer function :math:`H(\AngularFrequency)` as we defined it with the CTFT. We can do the same for the discrete version, by choosing :math:`x[k]=z^{k}`. Now applying the discrete convolution sum with the impulse response sequence :math:`h[k]`, we get:

.. math::

  \begin{align*}
    y[k] &= \sum\limits_{n=-\infty}^{\infty} h[n] x[k - n] \\
    &= \sum\limits_{n=-\infty}^{\infty} h[n] z^{k - n} \\
    &= \sum\limits_{n=-\infty}^{\infty} h[n] z^{k}z^{-n} \\
    &= \underbrace{z^{k}}_{x[k]} \underbrace{\sum\limits_{n=-\infty}^{\infty} h[n] z^{-n}}_{H(z)}
  \end{align*}

Where we can now recognize the input sequence :math:`x[k]` and the discrete transfer function of the system, as a function of the complex variable :math:`z`, given by the z-transform of the impulse response sequence:

.. math::

  H(z) = \ZTransform{h[k]} = \sum\limits_{k=-\infty}^{\infty} h[k] z^{-k}


In the table below you can find the z-transforms of some common functions.

.. raw:: html

  <div id="scoped-table-div">
  <style scoped>
    #scoped-table-div table {
      border-collapse: collapse;
      margin-right: auto;
      margin-left: auto;
    }
    #scoped-table-div thead {
      background-color: #333;
      color: white;
    }
    #scoped-table-div .odd {
      background-color: #f5f5f5;
    }
    #scoped-table-div th, td {
      padding-left: 6px;
      padding-right: 6px;
    }
  </style>

.. list-table::
  :header-rows: 1

  * - Time domain sequence :math:`x[k]`
    - Z domain signal :math:`X(z)`
  * - .. math::
        0
    - .. math::
        0
  * - .. math::
        1
    - .. math::
        \frac{1}{1-z^{-1}}
  * - .. math::
        k
    - .. math::
        \frac{z^{-1}}{(1-z^{-1})^2}
  * - .. math::
        \exp(-\alpha k)
    - .. math::
        \frac{1}{1-\exp(-\alpha)z^{-1}}
  * - .. math::
        k\exp(-\alpha k)
    - .. math::
        \frac{\exp(-\alpha)z^{-1}}{\left(1 - \exp(-\alpha)z^{-1}\right)^2}
  * - .. math::
        \sin(\AngularFrequency n)
    - .. math::
        \frac{\sin(\AngularFrequency)z^{-1}}{1 - 2\cos(\AngularFrequency)z^{-1} + z^{-2}}
  * - .. math::
        \cos(\AngularFrequency t)
    - .. math::
        \frac{1-\cos(\AngularFrequency)z^{-1}}{1 - 2\cos(\AngularFrequency)z^{-1} + z^{-2}}
  * - .. math::
        1-\exp(-\alpha t)
    - .. math::
        \frac{1}{1-z^{-1}} - \frac{1}{1-\exp(-\alpha)z^{-1}}
  * - .. math::
        \exp(-\alpha t)\sin(\AngularFrequency t)
    - .. math::
        \frac{1 - \exp(-\alpha)\cos(\omega)z^{-1}}{1-2 \exp(-\alpha)  \cos(\omega) z^{-1} + \exp(-2\alpha) z^{-2}}
  * - .. math::
        \exp(-\alpha t)\cos(\AngularFrequency t)
    - .. math::
        \frac{\exp(-\alpha)\sin(\omega)z^{-1}}{1-2 \exp(-\alpha)  \cos(\omega) z^{-1} + \exp(-2\alpha) z^{-2}}

.. raw:: html

  </div>
