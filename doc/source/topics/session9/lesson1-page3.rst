Discrete LTI Systems
====================

In continuous-time, we had several ways to describe the behaviour of LTI systems. Often we started at differential equations, and from that we derived a transfer function as function of :math:`s` to get the most flexible representation. For the discrete-time domain, we start at a similar concept, namely *difference equations*.

Difference equations are the discrete-time equivalent to continuous-time differential equations. Instead of a dependency of a function's time derivative, in these equations there is some dependency on previous samples of a discrete-time signal. The generic form of a linear, constant coefficient difference equation can be written as:

.. math::

  y[k] = \sum\limits_{q=0}^{M} \beta_q x[k - q] - \sum\limits_{p=1}^{N} \alpha_p y[k - p]

Where :math:`p` and :math:`q` are iterators, :math:`M` and :math:`N` are the number of samples we look back for the input :math:`x[k]` and the output :math:`y[k]` respectively. :math:`\beta_i` is the :math:`i`\ :superscript:`th` input coefficient and :math:`\alpha_i` is the :math:`i`\ :superscript:`th` output coefficient. Note that :math:`p` starts at :math:`1` instead of :math:`0` because :math:`y[k-0]` is on the left-hand-side of the equation.

This notation is rather dense, so how about an example:

.. math::

  y[k] = 4 x[k] - 2 x[k-1] - 3 y[k-1]

Here we have :math:`M=N=1`, :math:`\alpha_1=3`, :math:`\beta_0=4`, and :math:`\beta_1=-2`.

Now to get to a transfer function, we would like to transform this entire difference equation to the z-domain, and then in some way divide :math:`Y(z)` by :math:`X(z)`, but how to handle the time delays (e.g. :math:`x[k-1]`)? Let's just try it for an arbitrary sequence :math:`x[k]` with delay :math:`d`.

.. math::

  \begin{align*}
    \ZTransform{x[k-d]} &= \sum\limits_{k=-\infty}^{\infty} x[k-d] z^{-k} \\
    &= \sum\limits_{j=-\infty}^{\infty} x[j] z^{-(j+d)} & j &= k-d \\
    &= \sum\limits_{j=-\infty}^{\infty} x[j] z^{-j}z^{-d} \\
    &= z^{-d}\sum\limits_{j=-\infty}^{\infty} x[j] z^{-j} \\
    &= z^{-d}X(z)
  \end{align*}

So apparently a delay of :math:`d` samples corresponds with multiplication with :math:`z^{-d}` in the z-domain.

Continuing with our example, we can convert the entire difference equation to the z-domain:

.. math::

  \begin{align*}
    \ZTransform{y[k]} &= \ZTransform{4 x[k] - 2 x[k-1] - 3 y[k-1]} \\
    Y(z) &= 4X(z) - 2 z^{-1} X(z) - 3 z^{-1} Y(z)
  \end{align*}

Rewriting we get:

.. math::

  \begin{align*}
    Y(z) + 3 z^{-1} Y(z) &= 4X(z) - 2 z^{-1} X(z) \\
    Y(z) \left(1 + 3z^{-1}\right) &= X(z) \left(4 - 2z^{-1}\right) \\
    H(z) = \frac{Y(z)}{X(z)} &= \frac{4 - 2z^{-1}}{1 + 3z^{-1}}
  \end{align*}

Note that the z-domain transfer function :math:`H(z)` is ambiguous. There can exist multiple impulse responses that map to the same transfer function, the only difference is the region of convergence (ROC) for which the z-transform sum converges. This is outside the scope of this course.


Relation between Laplace and z-domain
-------------------------------------

Once we have derived a system transfer function either in the z-domain or in the Laplace complex frequency domain, we can relate the two of them using a so-called bilinear transform (which ironically is a Möbius transformation). It boils down to substituting the following approximations:

.. math::

  \begin{align*}
    z &= \exp(s\Period_s) \\
    &\approx \frac{1+s\frac{\Period_s}{2}}{1-s\frac{\Period_s}{2}}
  \end{align*}

and

.. math::

  \begin{align*}
    s &= \frac{1}{\Period_s}\ln (z) \\
    &\approx \frac{2}{\Period_s}\frac{1-z^{-1}}{1+z^{-1}}
  \end{align*}

Where :math:`\Period_s` is the sampling period.
