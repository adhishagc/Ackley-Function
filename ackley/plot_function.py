#importing libraries
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from .ackley_function import ackley_function_range

def plot_ackley_general():
  #this function will plot a general ackley function just to view it.
  limit = 1000 #number of points
  #common lower and upper limits for both x1 and x2 are used
  lower_limit = -5
  upper_limit = 5
  #generating x1 and x2 values
  x1_range = [np.random.uniform(lower_limit,upper_limit) for x in range(limit)]
  x2_range = [np.random.uniform(lower_limit,upper_limit) for x in range(limit)]
  #This would be the input for the Function
  x_range_array = [x1_range,x2_range]
  #generate the z range
  z_range = ackley_function_range(x_range_array)
  #plotting the function
  fig = plt.figure()
  ax = fig.gca(projection='3d')
  ax.scatter(x1_range, x2_range, z_range, label='Ackley Function')
  
def plot_ackley(x1_range,x2_range):
  #This would be the input for the Function
  x_range_array = [x1_range,x2_range]
  #generate the z range
  z_range = ackley_function_range(x_range_array)
  #plotting the function
  fig = plt.figure()
  ax = fig.gca(projection='3d')
  ax.scatter(x1_range, x2_range, z_range, label='Ackley Function')