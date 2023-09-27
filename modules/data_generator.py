import numpy as np

class data_generator:
  def __init__(self):
    self.data_1 = {
      'x': np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1)),
      'y': np.array([5, 20, 14, 32, 22, 38]),
      'x_new': np.arange(5).reshape((-1, 1)),
    }
    print(self)
    