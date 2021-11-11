Numerical integration for simulation
====================================

Integrating a signal :math:`x(t)` to get :math:`y(t)` 'the old-fashioned' way is done by:

.. math::

  y(t) = y(0) + \int\limits_{0}^{t} f(\tau) \DeltaD \tau = f(0) + F(t) - F(0)

Where we define (in the scope of this lesson, not to be mistaken with the Fourier, Laplace, or z-transform of :math:`f(t)`):

.. math::

  f(t) = \Diff{F(t)}

In words, :math:`F(t)` is the *anti-derivative* of :math:`f(t)`. Finding it can be cumbersome and even challenging for more complex integrals. For some integrals, the anti-derivative does not even exist. Besides, :math:`f(t)` could also be a function of :math:`y(t)`: :math:`f(t, y(t))`, which turns the above equation into a differential equation. This is typically encountered in systems with feedback loops.

Calculating the integral as shown above gives us an *exact* result, but 'exact' is still limited by our tools and the application. If an exact result is not a requirement, a good alternative is to look at numerical methods to get an *approximation* of the exact result. In our intended application, modelling and simulation of physical systems, we work with approximations by the definition of models, which can never be exact representations of the physical world.

Besides, using an numerical approach enables us to use sample sequences in discrete-time instead of continuous-time signals.


Basic concept
-------------

We assume that the function :math:`f(t, y(t))` is a function of time, and possibly a function :math:`y(t)` which makes it a differential equation. We assume that the function itself is unknown, but can still be evaluated at any point in time, either by interpolation of a sampled sequence or by processing an entire model numerically.

The basic approach to calculating an integral numerically is by splitting it in several parts, and approximating these parts with shapes that are more easily evaluated. These parts are not necessarily of the same length. In an equation that would look as follows:

.. math::
  
  \begin{align*}
    y(t) &= y(0) + 
    \int\limits_{0}^{t} f(\tau) \DeltaD\tau \\
    &=
    y(0) +
    \int\limits_{0}^{\TimeInstance{1}} f(\tau) \DeltaD\tau +
    \int\limits_{\TimeInstance{1}}^{\TimeInstance{2}} f(\tau) \DeltaD\tau +
    \cdots +
    \int\limits_{\TimeInstance{n-1}}^{t} f(\tau) \DeltaD\tau
  \end{align*}

Where :math:`0 < \TimeInstance{1} < \TimeInstance{2} < \cdots < \TimeInstance{n-1} < \TimeInstance{n}`. In a simulation, we would start by only calculating the first part:

.. math::

  y(\TimeInstance{1}) = y(0) + \int\limits_{0}^{\TimeInstance{1}} f(\tau) \DeltaD\tau

And we continue with the second part, but since we already calculated the first part, we can substitute that as initial value:

.. math::

  y(\TimeInstance{2}) = y(\TimeInstance{1}) + \int\limits_{\TimeInstance{1}}^{\TimeInstance{2}} f(\tau) \DeltaD\tau

So generalized we would calculate the following equation for every time step:

.. math::

  y(\TimeInstance{k}) = y(\TimeInstance{k-1}) + \int\limits_{\TimeInstance{k-1}}^{\TimeInstance{k}} f(\tau) \DeltaD\tau

In this lesson we will only see fixed time-step methods. For these methods the time instances are defined as follows:

.. math::

  \TimeInstance{k} = k\TimeStep, \quad k \in 0,1,2,\ldots

Where :math:`\TimeStep` is the duration of the time-step.

Now that the basic approach is defined, we can choose an approximation to solve the integral part. Several integration methods can be used, which are characterised by the following properties:

order of the method
  An :math:`n`\ :superscript:`th`-order integration method uses an :math:`n-1`\ :superscript:`th`-order polynomial to describe the interval of the signal to be integrated.

one-step or multi-step
  An integration method is called *one-step* if all information to calculate :math:`y(\TimeInstance{k})` is based on the time-interval :math:`\TimeInstance{k-1}` to :math:`\TimeInstance{k}`. If a method uses more than one time-interval 'in the past' to estimate :math:`y(\TimeInstance{k})`, it is called *multi-step*.

implicit or explicit
  An *explicit* integration method does not use the current input :math:`f(\TimeInstance{k})` to estimate the current output :math:`y(\TimeInstance{k})`, such that the estimate of :math:`y(\TimeInstance{k})` only depends on previous values. Explicit methods can be used directly in a feedback system. If an *implicit* method has to be used in a feedback system, the current input (which then depends on the current output, and we have in fact a differential equation) has to be approximated by means of iteration.


Methods
-------


Euler
~~~~~

.. figure:: /_static/figures/session9/integration_methods/integration_methods-001.svg

  Graphical depiction of the Euler method.

The Euler method is the simplest method of numerical integration. It assumes that the value of :math:`f(t)` is equal to :math:`f(\TimeInstance{k-1})` for the period :math:`\TimeInstance{k}\ldots\TimeInstance{k-1}`, thus approximating :math:`f(t)` with a :math:`0`\ :superscript:`th`-order polynomial. The area under the curve is then the amount that this time-step adds to the total integral.

.. math::

  y(\TimeInstance{k}) = y(\TimeInstance{k-1}) + \TimeStep f(\TimeInstance{k-1})

The Euler method is:

* Explicit
* Single step
* First order


Backward Euler
~~~~~~~~~~~~~~

.. figure:: /_static/figures/session9/integration_methods/integration_methods-002.svg

  Graphical depiction of the backward Euler method.

Very similar to the Euler method, the backward Euler method assumes that the value of :math:`f(t)` is equal to :math:`f(\TimeInstance{k})` for the period :math:`\TimeInstance{k}\ldots\TimeInstance{k-1}`, also approximating :math:`f(t)` with a :math:`0`\ :superscript:`th`-order polynomial.
  
.. math::

  y(\TimeInstance{k}) = y(\TimeInstance{k-1}) + f(\TimeInstance{k})\TimeStep

The backward Euler method is:

* Implicit
* Single step
* First order

Note that we can also pick a value of :math:`f(t)` between :math:`\TimeInstance{k-1}` and :math:`\TimeInstance{k}`, an example of that is the `midpoint method <https://en.wikipedia.org/wiki/Midpoint_method>`__, which will be treated further below.


Tustin
~~~~~~

.. figure:: /_static/figures/session9/integration_methods/integration_methods-004.svg

  Graphical depiction of the Tustin method.

Obviously the Euler method leaves some to be desired, as the error between actual area under the curve and the estimate is quite large. We can make a better estimate using the Tustin method, also known as the trapezoid method. This method uses a :math:`1`\ :superscript:`st`-order polynomial to estimate :math:`f(t)`, forming a trapezoid with the vertical lines at :math:`t=\TimeInstance{k-1}` and :math:`t=\TimeInstance{k}`, and the :math:`t`-axis.

.. math::

  y(\TimeInstance{k}) = y(\TimeInstance{k-1}) + \frac{1}{2}\TimeStep\left(f(\TimeInstance{k-1}) + f(\TimeInstance{k}) \right)

The Tustin method is:

* Implicit
* Single step
* Second order


Adams-Bashforth
~~~~~~~~~~~~~~~

.. figure:: /_static/figures/session9/integration_methods/integration_methods-005.svg

  Graphical depiction of the Adams-Bashforth method.

Another second order method is the Adams-Bashforth method. This method extrapolates the change rate (steepness) of :math:`f(t)` between :math:`\TimeInstance{k-2}` and :math:`\TimeInstance{k-1}` to approximate the change rate between :math:`\TimeInstance{k-1}` and :math:`\TimeInstance{k}` without knowing :math:`f(\TimeInstance{k})`. This way we can still use the trapezoid area to approximate the integral area under the curve.

The Adams-Bashforth method looks back two steps, but in general only the very first (initial) value of :math:`y(t)` is provided. This issue can be solved by using the Euler method to calculate :math:`y(\TimeInstance{1})`, and then switch to the Adams-Bashforth method to calculate :math:`y(\TimeInstance{2})` and further.

.. math::

  y(\TimeInstance{k}) = y(\TimeInstance{k-1}) + \frac{1}{2}\TimeStep\left(f(\TimeInstance{k-2}) + 3f(\TimeInstance{k-1}) \right)

The Adams-Bashforth method is:

* Explicit
* Two step
* Second order


Heun
~~~~

The Tustin method is implicit, and therefore cannot be used for differential equations. One possible workaround is to first estimate :math:`y_p(\TimeInstance{k})` using the Euler method, and then apply the Tustin method as follows:

.. math::

  y(\TimeInstance{k}) = y(\TimeInstance{k-1}) + \frac{1}{2}\TimeStep\left(f(\TimeInstance{k-1}) + f_p(\TimeInstance{k}, y_p(\TimeInstance{k})) \right)

The Heun method is:

* Explicit
* Single step
* Second order


Runge-Kutta
~~~~~~~~~~~

Another family of possible methods is the Runge-Kutta family. This family of numeric analysis methods uses intermediate steps between :math:`\TimeInstance{k-1}` and :math:`\TimeInstance{k}`, and calculates :math:`y(t)` and :math:`f(t)` at those steps to get to a more accurate result for :math:`y(\TimeInstance{k})`. These methods are generally explicit, but do require more calculations to solve for :math:`y(\TimeInstance{k})`. Runge-Kutta methods can be implemented in various orders, e.g. the midpoint method mentioned above is a second order Runge-Kutta method. There is a plethora of other options, a lot of them listed `here <https://en.wikipedia.org/wiki/List_of_Runge%E2%80%93Kutta_methods>`__.

.. rubric:: Second order Runge-Kutta (RK2):

.. figure:: /_static/figures/session9/integration_methods/integration_methods-003.svg

  Graphical depiction of a second order Runge-Kutta method, more commonly known as the midpoint method.

.. math::

  y(\TimeInstance{k}) = y(\TimeInstance{k-1}) + \TimeStep k_2

where:

.. math::

  \begin{align*}
    k_1 &= f\left( \TimeInstance{k-1}, y(\TimeInstance{k-1}) \right) \\
    k_2 &= f\left( \TimeInstance{k-\frac{1}{2}}, y(\TimeInstance{k-1}) + \frac{h k_1}{2} \right)
  \end{align*}

The RK2 method is:

* Explicit
* Single step
* Second order

.. rubric:: Fourth order Runge-Kutta (RK4):

The fourth order Runge-Kutta method is considered the 'default' or 'classical' Runge-Kutta method.

.. math::

  y(\TimeInstance{k}) = y(\TimeInstance{k-1}) + \frac{1}{6}\TimeStep\left(c_1 + 2c_2 + 2c_3 + c_4\right)

where:

.. math::

  \begin{align*}
    k_1 &= f\left( \TimeInstance{k-1}, y(\TimeInstance{k-1}) \right) \\
    k_2 &= f\left( \TimeInstance{k-\frac{1}{2}}, y(\TimeInstance{k-1}) + h\frac{k_1}{2} \right) \\
    k_3 &= f\left( \TimeInstance{k-\frac{1}{2}}, y(\TimeInstance{k-1}) + h\frac{k_2}{2} \right) \\
    k_4 &= f\left( \TimeInstance{k}, y(\TimeInstance{k-1}) + hk_3 \right)
  \end{align*}

The RK4 method is:

* Explicit
* Single step
* Fourth order

The Euler method is the simplest Runge-Kutta method, and also the Heun method is a Runge-Kutta method.

All methods listed above are fixed time-step methods. Variable time-step methods also exist, but these are outside the scope of this course.


Example
-------

In the descriptions above we have seen no references to an input, but :math:`f` could also depend on an external input: :math:`f(t, y(t), x(t))`. We again use the current powered RC circuit as example.

.. figure:: /_static/figures/session8/iRC_example/iRC_example-001.svg

  Bond graph of an RC circuit.

.. figure::  /_static/figures/session8/iRC_example/iRC_example-002.svg

  Block diagram of an RC circuit.

The following differential equation describes the behaviour. We want to write it in terms of :math:`\Diff{u(t)}` and then integrate both sides to get the proper expression for our simulator algorithms.

.. math::

  \begin{align*}
    i(t) &= C \Diff{u(t)} + \frac{u(t)}{R} \\
    \Diff{u(t)} &= \frac{i(t)}{C} - \frac{u(t)}{RC} \\
    u(t) &= \frac{q_0}{C} + \int\limits_{0}^{t} \left(\frac{i(\tau)}{C} - \frac{u(\tau)}{RC} \right)\DeltaD \tau
  \end{align*}

We define :math:`x(t)=i(t)` as input and :math:`y(t)=u(t)` as output of the system. We can find :math:`f` and :math:`y(0)` also from the equation above.

.. math::

  \begin{align*}
    y(\TimeInstance{0}) &= u(\TimeInstance{0}) = \frac{q_0}{C} \\
    f(t, y(t), x(t)) &= \frac{x(t)}{C} - \frac{y(t)}{RC}
  \end{align*}

For both scripts we choose :math:`R=1\Unit{\Omega}`, :math:`C=2\Unit{F}`, and :math:`q_0=0\Unit{C}`.

We implement two methods, the Runge-Kutta 4 method and the Euler method and approximate the Dirac delta function with the input signal to get the impulse response of the system. Run the scripts to compare the results to the exact solution that we found in the previous session.


Python
~~~~~~

.. include:: example.py
  :code: python


MATLAB
~~~~~~

.. include:: example.m
  :code: matlab
