import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import statsmodels.api as sm

class linear_regression_analyzer:
  def __init__(self):
    print(self)
  
  def simple_linear_regression(self, x_vars, y_var):
    model = LinearRegression()

    model.fit(x_vars, y_var)

    r_sq = model.score(x_vars, y_var)

    y_pred = model.predict(x_vars)

    # y_pred = model.intercept_ + model.coef_ * x
    
    # print(f"predicted response:\n{y_pred}")

    # y_pred = model.intercept_ + model.coef_ * x.reshape(-1)
    
    # print(f"predicted response:\n{y_pred}")

    return {
      'model': model,
      'intercept': model.intercept_,
      'slope': model.coef_,
      'determination_coeff': r_sq,
      'predicted_response': y_pred,
    }