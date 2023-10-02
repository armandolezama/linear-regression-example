import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import statsmodels.api as sm

class linear_regression_analyzer:
  def __init__(self):
    print(self)
  
  def simple_linear_regression(self, x_var, y_var):
    model = LinearRegression()

    model.fit(x_var, y_var)

    r_sq = model.score(x_var, y_var)

    y_pred = model.predict(x_var)

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
  
  def multi_linear_regression(self, x_vars, y_var):
    model = LinearRegression().fit(x_vars, y_var)

    r_sq = model.score(x_vars, y_var)

    y_pred = model.predict(x_vars)

    ## y_pred = model.intercept_ + np.sum(model.coef_ * x, axis=1)

    return {
      'model': model,
      'intercept': model.intercept_,
      'slope': model.coef_,
      'determination_coeff': r_sq,
      'predicted_response': y_pred,
    }
  
  def polynomial_regression(self, x_var, y_var, include_bias = False, fit_intercept = True):
    x_ = PolynomialFeatures(degree=2, include_bias=include_bias).fit_transform(x_var)

    model = LinearRegression(fit_intercept=fit_intercept).fit(x_, y_var)

    r_sq = model.score(x_, y_var)

    y_pred = model.predict(x_)

    return {
      'model': model,
      'intercept': model.intercept_,
      'coefficients': model.coef_,
      'determination_coeff': r_sq,
      'predicted_response': y_pred,
    }

  def detailed_OLS_linear_regression(slef, x_var, y_var):
    x = sm.add_constant(x_var)
    model = sm.OLS(y_var, x)
    results = model.fit()
    predicted = results.predict(x)

    return {
      'results': results,
      'determination_coeff': results.rsquared,
      'adj_determination_coeff': results.rsquared_adj,
      'regression_coefficients': results.params,
      ## Predicted and fitted values are the same
      'fitted_values': results.fittedvalues,
      'predicted': predicted,
    }
