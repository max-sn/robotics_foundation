Fourier
=======

Until this point in the course we have treated both systems and signals only in the time-domain, i.e. we have only looked at in- and output signals defined as functions of time, and treated the system's behaviour as a series of operations on these signals, but we let our simulation software solve the responses. Under the hood, this software has to solve the differential equations that are formed by the series of operations (block diagram), or use some other clever method. It turns out that there are other ways to represent the input signals and system's behaviour, which make solving these differential equations less complex.

We have also seen the impulse response, but we're not yet convinced that this is a better method for determining the response of systems, particularly with the cumbersome convolution operation. Fortunately, there is a way to simplify convolutions and expressing the impulse response, namely by using the frequency domain. For this, we can use the Fourier transform. A nice analogy found `online <https://betterexplained.com/articles/an-interactive-guide-to-the-fourier-transform/>`_ is:

:What does the Fourier transform do?:
  Given a smoothie, it finds the recipe.

:How?:
  By running the smoothie through a series of filters to extract each ingredient.

:Why?:
  Recipes are easier to analyze, compare, and modify than the smoothie as a whole.

:How do we get the smoothie back?:
  By re-blending the ingredients, this is what the inverse Fourier transform does.



Inverse Fourier transform
-------------------------

First we will ook at getting back from the frequency domain to the time domain, to get an idea of how a signal is represented in the frequency domain.

.. raw:: html

  <iframe style="width: 695px; height: 390px;" src="https://www.youtube-nocookie.com/embed/1JnayXHhjlg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Note that the instructor of the videos has omitted the scaling with :math:`\frac{1}{\Period}` in the inverse Fourier transform, he explains this in the next video. This is the version that we will use in this course.

.. math::

  f(t) = \frac{1}{\Period}\int\limits_{-\infty}^{\infty} F(\Frequency) \exp(2\pi i \Frequency t) \DeltaD \Frequency


Where :math:`\Frequency` is the frequency in Hertz, and can be expressed in terms of the angular frequency :math:`\AngularFrequency` as follows: :math:`\Frequency=\frac{\AngularFrequency}{2\pi}\Unit{H}`. Note that :math:`\AngularFrequency` is similar to angular velocity as we have seen it before in this course, in that the units are the same (:math:`\Unit{rad \cdot s^{-1}}`) and it can be regarded as how many radians the (co)sine wave progresses per second.

:math:`F(\Frequency)` is a complex function of the frequency, and for a given frequency :math:`\Frequency`, it returns the amplitude and phase shift of that frequency's presence in the original signal :math:`f(t)`, in the form of a complex number. Recall that from a complex number :math:`z=a+ib`, we can get the amplitude as :math:`\Amplitude=\sqrt{a^2 + b^2}` and the phase shift as :math:`\PhaseShift=\arctantwo(b, a)`.

Another important equality that is used here is Euler's formula:

.. math::

  \exp(it) = \cos t + i \sin t

This gives a generalization for all possible complex sinusoids.

As an example, let's say that a certain response of :math:`F(\Frequency)` at :math:`\Frequency=\Frequency_1` is given by:

.. math::

  F(\Frequency_1) = \frac{\sqrt{2}}{2} + i\frac{\sqrt{2}}{2}

If we solve the *inside* of the inverse Fourier transform integral for this value of :math:`\Frequency`, we get:

.. math::

  \begin{align*}
    F(\Frequency_1)\exp(2\pi i \Frequency_1 t) &= \left(\frac{\sqrt{2}}{2} + i\frac{\sqrt{2}}{2}\right)\left(\cos(2\pi \Frequency t) + i \sin (2\pi \Frequency t)\right) \\
    &= \underbrace{\frac{\sqrt{2}}{2}\cos(2\pi \Frequency t) - \frac{\sqrt{2}}{2}\sin(2\pi \Frequency t)}_{\text{Real part of signal }f(t)} +
    \underbrace{\frac{\sqrt{2}}{2}\cos(2\pi \Frequency t)i - \frac{\sqrt{2}}{2}\sin(2\pi \Frequency t)i}_{\text{Imaginary part of signal }f(t)}
  \end{align*}

To get rid of the imaginary part, because in this course we are only interested in real signals, we also take the response of :math:`F(\Frequency)` at :math:`\Frequency=-\Frequency_1`. It turns out that if :math:`F(\Frequency_1)=a+ib`, the response :math:`F(-\Frequency_1)=\ComplexConjugate{a+ib}=a-ib`, where the line over the complex number denotes the 'complex conjugate' of that number. This sounds more difficult than it really is, because it simply means that the imaginary part is negated. This is the same conclusion as the instructor derives when plotting the real- and imaginary part of :math:`F(\Frequency)` separately and concluding that the real part is even, and the imaginary part is odd.


Forward Fourier transform
-------------------------

.. raw:: html

  <iframe style="width: 695px; height: 390px;" src="https://www.youtube-nocookie.com/embed/kKu6JDqNma8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

The part about scaling at the start of the video also applies to the Fourier *transform* not only to the Fourier series.

Important message: any continuous periodic signal can be expressed as the sum of a set of carefully chosen sinusoids. The Fourier transform finds for us the necessary frequencies, amplitudes, and phase shifts of all sinusoids in the signal. 

An example of a periodic signal is shown below:

.. figure:: /_static/figures/session8/sinusoids/sinusoids-001.svg

  Continuous signal :math:`f(t)`.

.. figure:: /_static/figures/session8/sinusoids/sinusoids-002.svg

  First sinusoid to compose :math:`f(t)`. It is completely defined by the phase shift :math:`\PhaseShift`, period :math:`\Period` or frequency :math:`\Frequency` (one implies the other), and the amplitude :math:`\Amplitude`.

.. figure:: /_static/figures/session8/sinusoids/sinusoids-003.svg

  Second sinusoid to compose :math:`f(t)`.
  
If the signal's period goes towards infinity, and in doing so makes the signal non-periodic, a continuous and complex function of frequency is needed to represent all sinusoids. The real part of this complex function represents the (scaled) amplitudes of the sinusoids, and the imaginary part represents the phase shift of the sinusoids. This is what the Fourier transform can provide.

The forward Fourier transform is defined as:

.. math::

  F(\Frequency) = \int\limits_{-\infty}^{\infty} f(t) \exp(-2\pi i \Frequency t) \DeltaD t


'Dividing' a signal :math:`f(t)` with a :math:`15\Unit{Hz}` signal, as shown in the video, gives us how much of the :math:`15\Unit{Hz}` signal is present in the signal :math:`f(t)`. I don't particularly like the analogy with dividing 15\\$ by 5\\$ bills, because in this example it implies that there cannot be any other bills (read: frequencies), e.g. 1\\$ bills, present in the original 15\\$ (read: signal :math:`f(t)`), because we already divided by 5\\$ bills, and their value is not independent. For frequencies, this independence between devisors is there. For example, if we add 5 1\\$ bills to the original 15\\$, we get 20\\$, which is now equal to 4 5\\$ bills. If we add 5 times the :math:`1\Unit{Hz}` signal to the original signal :math:`f(t)`, this does *not* change the presence of the :math:`5\Unit{Hz}` signal in :math:`f(t)`.

Don't mistake how the division analogy is written, it is not :math:`\exp(\frac{f(t)}{i2\pi \Frequency t})` (it looks like that due to writing it by hand), it is:

.. math::

  \frac{f(t)}{\exp(i2\pi \Frequency t)} = f(t)\exp(-i2\pi \Frequency t)

The examples that the instructor shows in the video are used to show that dividing by an exponent with a certain frequency will result in a signal without power if that frequency is not present in the initial signal. If the frequency *is* present, the result will have power.

Let's use the same examples as in the video. We have a certain function, given by :math:`\cos(t)`, and we want to check whether there is any :math:`2\Unit{rad \cdot s^{-1}}=\frac{2}{2\pi}\Unit{Hz}` signal present in there.

.. math::

  \begin{align*}
    f(t) &= \cos(t) \\
    \Frequency  &= \frac{2}{2\pi} \\ 
    f(t)\exp(-i2\pi \Frequency t) &= \cos(t) \exp(-i2 t) \\
    &= \cos(t) \left( \cos(2 t) - i\sin(2 t)\right)
  \end{align*}

For both the real part (:math:`\cos(t)\cos(2t)`) and the imaginary part (:math:`i\cos(t)\sin(2t)`) the sum over all :math:`t` will be zero.

Now let's check if there is any :math:`1\Unit{rad \cdot s^{-1}}=\frac{1}{2\pi}\Unit{Hz}` signal present in there.

.. math::

  \begin{align*}
    f(t) &= \cos(t) \\
    \Frequency  &= \frac{1}{2\pi} \\ 
    f(t)\exp(-i2\pi \Frequency t) &= \cos(t) \exp(-i t) \\
    &= \cos(t) \left( \cos(t) - i\sin(t)\right)
  \end{align*}

Now only for the imaginary part (:math:`i\cos(t)\sin(t)`) the sum over all time will be zero, for the real part (:math:`\cos^2(t)`), the sum over all time will be infinity. But, remember that we still have to scale this sum by :math:`\frac{1}{\Period}` to get the amplitude of the signal's :math:`1\Unit{rad \cdot s^{-1}}` contents. We used the Fourier transform, so implicitly we assumed that the signal was non-periodic (forget for the moment that it actually is periodic), which means that the period is also infinity. So if we want to scale the sum over all time of the real part with the inverted period, we get: :math:`\frac{\infty}{\infty}`. Unfortunately this is where our nice derivation turns into more nasty math, and we have to do some trickery with the Dirac delta function to get a meaningful value for the amplitude, which in this case is:

.. math::

  F(\Frequency) = \frac{1}{2}\left(\delta\left(\Frequency - \frac{1}{2\pi}\right) + \delta\left(\Frequency + \frac{1}{2\pi}\right)\right)

The fact that the Fourier transform of a sinusoid is in the form of Dirac delta functions is not surprising. If we look at the inverse Fourier transform, we multiply the frequency domain representation of the function :math:`F(\Frequency)` with all frequencies between :math:`-\infty` and :math:`\infty` and then sum over all frequencies. To get our original frequency back, we simply plug in a shifted Dirac delta function that is infinitely large at our original frequency, and zero for all other frequencies. The amplitude is split between the negative original frequency and the positive original frequency.

We denote the Fourier transform of an arbitrary signal :math:`x(t)` as :math:`\FourierTransform{x(t)}`.


Applications of the Fourier transform
-------------------------------------

Now we spent a lot of time and effort to get our signals described in the frequency domain, but why did we bother? There are a few operations that are convenient to do in the frequency domain.

.. rubric:: Convolution

A big advantage of the frequency domain is that convolution in this domain is simply a multiplication. Given two functions :math:`x(t)` and :math:`y(t)` and their respective frequency domain representations :math:`X(\Frequency)` and :math:`Y(\Frequency)`, the following holds:

.. math::

  \FourierTransform{x * y} = X(\Frequency)Y(\Frequency)

.. rubric:: Differentiation

Let :math:`x(t)` be a smooth signal with corresponding Fourier transform :math:`X(\Frequency)` and assume that :math:`\lim\limits_{t\rightarrow\infty}x(t)=0` and :math:`\lim\limits_{t\rightarrow-\infty}x(t)=0`. Then :math:`\FourierTransform{\dot{x}(t)}` exists and:

.. math::

  \FourierTransform{\dot{x}(t)} = i\AngularFrequency X(\Frequency) = i2\pi\Frequency X(\Frequency)

.. rubric:: Integration

Let :math:`x(t)` be a continuous, integrable signal with corresponding Fourier transform :math:`X(\Frequency)`, if :math:`X(0)=0` then:

.. math::

  \FourierTransform{\int_{-\infty}^{t} x(\tau) \DeltaD \tau} = \frac{1}{i\AngularFrequency} X(\Frequency) = \frac{1}{i2\pi\Frequency} X(\Frequency)

.. rubric:: Impulse response

For an LTI system, the response to any arbitrary input is defined by the impulse response :math:`h(t)`. If the input is :math:`x(t)` then:

.. math::

  y(t) = (x * h)(t)

We can define the Fourier transform of the impulse response as *transfer function* :math:`H(\Frequency)=\FourierTransform{h(t)}` of the LTI system, then:

.. math::

  Y(\Frequency) = X(\Frequency) H(\Frequency)

