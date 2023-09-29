import numpy as np
import statsmodels.api as sm

class data_generator:
  def __init__(self):
    self.data_1 = {
      'x': np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1)),
      'y': np.array([5, 20, 14, 32, 22, 38]),
      'x_new': np.arange(5).reshape((-1, 1)),
    }
    
    self.data_2 = {
      'x': np.array([ [0, 1], [5, 1], [15, 2], [25, 5], [35, 11], [45, 15], [55, 34], [60, 35] ]),
      'y': np.array([4, 5, 20, 14, 32, 22, 38, 43]),
      'x_new': np.arange(10).reshape((-1, 2)),
    }

    self.data_3 = {
      'x': np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1)),
      'y': np.array([15, 11, 2, 8, 25, 32]),
    }

    self.data_3_1 = {
      'x': np.array([ [0, 1], [5, 1], [15, 2], [25, 5], [35, 11], [45, 15], [55, 34], [60, 35]]),
      'y': np.array([4, 5, 20, 14, 32, 22, 38, 43]),
    }

    self.data_4 = {
      'x': np.array([[0, 1], [5, 1], [15, 2], [25, 5], [35, 11], [45, 15], [55, 34], [60, 35]]),
      'y': np.array([4, 5, 20, 14, 32, 22, 38, 43]),
      'x_new': sm.add_constant(np.arange(10).reshape((-1, 2))),
    }
    print(self)
    