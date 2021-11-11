# %%
import numpy as np
import matplotlib.pyplot as plt


# Runge-Kutta 4 example function
def RK4(t0, y0, x, h, fun, N):
    t = np.zeros((N, ))
    y = np.zeros((N, ))
    t[0] = t0
    y[0] = y0
    for i in range(1, N):
        k1 = fun(t[i-1],       y[i-1],            x[i-1])
        k2 = fun(t[i-1] + h/2, y[i-1] + h*(k1/2), x[i-1])
        k3 = fun(t[i-1] + h/2, y[i-1] + h*(k2/2), x[i-1])
        k4 = fun(t[i-1] + h,   y[i-1] + h*k3,     x[i-1])
        y[i] = y[i-1] + h/6 * (k1 + 2*k2 + 2*k3 + k4)
        t[i] = t[i-1] + h
    return y, t


# Euler example function
def Euler(t0, y0, x, h, fun, N):
    t = np.zeros((N, ))
    y = np.zeros((N, ))
    t[0] = t0
    y[0] = y0
    for i in range(1, N):
        y[i] = y[i-1] + h * fun(t[i-1], y[i-1], x[i-1])
        t[i] = t[i-1] + h
    return y, t


# Parameters
R = 1
C = 2

# Initial values
# y = u(t), voltage over resistor
# x = i(t), current delivered by current source
q0 = 0     # initial charge
u0 = q0/C  # initial voltage

# Simulation properties
t0 = 0                # start time
tN = 10               # end time (10 second simulation)
h = 0.1               # time-step size
N = round((tN-t0)/h)  # number of samples


# Create f(t, y, x) as function
def fun(t, y, x):
    return x/C - y/(R*C)


i = np.zeros((N, 1))  # i(t)
i[0] = 1/h            # simulate Dirac delta to get impulse response

y1, t1 = RK4(t0, u0, i, h, fun, N)
y2, t2 = Euler(t0, u0, i, h, fun, N)

plt.plot(t1, y1, label="Runge-Kutta 4")
plt.plot(t2, y2, label="Euler")
plt.plot(t1, 1/C*np.exp(-t1/(R*C)), label="Exact")

plt.legend()
plt.show()
