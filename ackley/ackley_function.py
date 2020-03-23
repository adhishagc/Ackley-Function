#importing libraries
import numpy as np
import math

def ackley_function(x1,x2):
  #returns the point value of the given coordinate
  part_1 = -0.2*math.sqrt(0.5*(x1*x1 + x2*x2))
  part_2 = 0.5*(math.cos(2*math.pi*x1) + math.cos(2*math.pi*x2))
  value = math.exp(1) + 20 -20*math.exp(part_1) - math.exp(part_2)
  #returning the value
  return value

def ackley_function_range(x_range_array):
  #returns an array of values for the given x range of values
  value = np.empty([len(x_range_array[0])])
  for i in range(len(x_range_array[0])):
    
    #returns the point value of the given coordinate
    part_1 = -0.2*math.sqrt(0.5*(x_range_array[0][i]*x_range_array[0][i] + x_range_array[1][i]*x_range_array[1][i]))
    part_2 = 0.5*(math.cos(2*math.pi*x_range_array[0][i]) + math.cos(2*math.pi*x_range_array[1][i]))
    
    value_point = math.exp(1) + 20 -20*math.exp(part_1) - math.exp(part_2)
    value[i] = value_point
  #returning the value array
  return value