import matplotlib.pyplot as plt
import numpy as np

def f(x, T):
  return 0.2*(T-x)

def euler(x, T, d, t):
  """
  Args:
    x: initial temperature
    T: stable/room temperature for heat equation
    d: step size
    t: final time period
  
  Returns:
    plot of solution to heat equation with given parameters
  """
  t = np.arange(0, t, d)
  ts = []
  for i in t:
    ts.append(x)
    x = x + d*f(x, T)
    
  fig, ax = plt.subplots(figsize=[10,7])
  ax.plot(t, ts)
  ax.set_ylim(0, T)
  ax.set_ylabel('Temperature (C)')
  ax.set_xlabel('Time')
  fig.suptitle(f"Solution to heat equation using Euler's method", fontsize=15)