
# 05-Regression

* Introducing statsmodels applied to the advertising dataset
* Model evaluation and hypothesis testing with linear regression
* Introducing the scikit-learn estimator API 

### Links

* [05-statsmodels-exercises.ipynb](https://colab.research.google.com/drive/14a5Ula4W-NNbGWB_C5T819OeXjAB0ju_)
* [poll](poll.md)
* [scratch-notebook](https://colab.research.google.com/drive/1H4sj-XdST_PqBXQTrkutsamSFrOs2wNG)

### Reading (for next week)

ISLR2 -- Chapter 4: Classification (read the sections listed below)

* Section 4.1 & 4.2
* Section 4.3 -- concepts only, don't worry about mathematical details
* Section 4.4 -- might be tough reading, so don't worry about details
  * Sections 4.4.1-3 -- LDA and QDA -- skim
  * Section 4.4.4 -- Naive Bayes -- concepts only, we'll be using this model
* Sections 4.5-4.8 -- Entirely optional (we won't be covering this material)

### assignment-submission guidelines

* [git-intro](http://github.com/ds5110/git-intro)

### Projects

* [projects-spring-2023](https://github.com/ds5110/projects-spring-2023)

## Regression (over/review)

* What is statistical learning?
* Ch 2.1 as advertising dataset (reading assigned week 1)
  * Reducible and irreducible error -- recall equations 2.1-2.3 in ISL...
```math
Y = f(X) + \epsilon
```
```math
\hat{Y} = \hat{f}(X)
```
```math
E(Y - \hat{Y}) = | f(X) - \hat{f}(X) |^2 + \mathrm{Var}(\epsilon)
```

* Reducible error (squared): $| f(X) - \hat{f}(X) |^2$
* Irreducible error (variance): $\mathrm{Var}(\epsilon)$
* Inference (p19) vs prediction -- the inference paradigm...
  * Which predictors are associated with the response?
  * What is the relationship between the response, Y, and each predictor?
  * Can the relationships be summarized using a linear equation or is the relationship more complicated?
* Ch 3.1-4 (reading assigned last week for this week)
  * Advertising dataset
  * Advertising dataset -- the inference paradigm (p20)
    * Which media are associated with sales?
    * Which media generate the biggest boost in sales?
    * How large of an increase in sales is associated with a given increase in TV advertising?
* Parametric methods (p21), for example, assuming a linear relationship (equation ...
```math
f(X) = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + ... + \beta_p X_p
```
* Multiple linear regression (ISL section 3.2, equation 3.19)
```math
Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + ... + \beta_p X_p + \epsilon
```
* In relation to the advertising dataset (equation 3.20)...
```math
\mathrm{sales} = \beta_0 + \beta_1 \times \mathrm{TV} + \beta_2 \times \mathrm{radio} + \beta_3 \times \mathrm{newspaper} + \epsilon
```
* Linear regression -- choose the coefficients to minimize the residual sum of the squares (equation 3.22).
```math
\mathrm{RSS} = \sum_{i=0}^n (y_i - \hat{y}_i)^2 = \sum_{i=0}^n (\hat{\epsilon}_i)^2
```

### Introduction to statsmodels

* [statsmodels.org](https://www.statsmodels.org/stable/index.html)
* statsmodels is a port of R-style statistics to Python
* There are two APIs -- DSL (Domain Specific Language) similar to R, and a numpy-friendly API
* A question you might ask: What's the distribution of the residuals?
  * [seaborn distributions](https://seaborn.pydata.org/tutorial/distributions.html)
    * "An early step in any effort to analyze or model data should be to understand how the variables are distributed."
  * Gaussian noise has a normal distribution
  * [seaborn boxplot](https://seaborn.pydata.org/generated/seaborn.boxplot.html)
    * "A box plot (or box-and-whisker plot) shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable."
  * [seaborn histplot](https://seaborn.pydata.org/generated/seaborn.histplot.html#seaborn.histplot)
   * "A histogram is a classic visualization tool that represents the distribution of one or more variables by counting the number of observations that fall within discrete bins."
  * [seaborn displot](https://seaborn.pydata.org/generated/seaborn.displot.html)
    * Figure-level interface for drawing distribution plots onto a FacetGrid.
* Correlation matrix
  * A question you might ask: Are the predictors (features) correlated with one another?
    * $R^2$ = R-squared is the square of the correlation
  * With numpy (from statsmodels example): [plot_corr](https://www.statsmodels.org/dev/generated/statsmodels.graphics.correlation.plot_corr.html) example
  * With pandas [DataFrame.corr()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html)

### Pandas gotchas

* [notebooks/05-pandas-gotchas.ipynb](notebooks/05-pandas-gotchas.ipynb)
* TL;DR: Don't suppress pandas warnings -- fix them!

### Introduction to scikit-learn

* References...
  * p343 in VanderPlas (pdf) or...
  * [05.02-Introducing-Scikit-Learn.ipynb](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/05.02-Introducing-Scikit-Learn.ipynb)
    * This notebook introduces scikit-learn
    * Data as a table (should be familiar with this)
      * Cells 1-4 talk about the data model using the iris dataset
    * Introduces the scikit-learn "Estimator API"
    * Demo: simple linear regression in Cells 5-11 is worth reviewing
  * Publication: [Estimators API](https://arxiv.org/abs/1309.0238) (2013) -- arxiv.org
  * Two perspectives: ISLR2 & VanderPlas (statistics & CS)
    * VanderPlas is actually an astronomy PhD and contributor to scikit-learn
    * Authors of ISLR2 (notably Hastie & Tibshirani) instrumental with R (formerly S)
    * Physics and astronomy communities successfully leverage the CS perspective
    * Biotech community is a heavy R user
    * Others (fintech, BI) use both
  * Different perspectives/communities typically means different language/jargon
    * Predictors -- Feature Matrix
    * Response -- Target array
* [04-polynomial-regression.ipynb](notebooks/04-polynomial-regression.ipynb)
  * This notebook looks at polynomial regression in detail as prep for the bias-variance tradeoff discussion below.
  * Cell 10 in [05.03-Hyperparameters-and-Model-Validation.ipynb](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/05.03-Hyperparameters-and-Model-Validation.ipynb) uses a scikit-learn pipline for polynomial regression, including `sklearn.pipline`

### Bias-variance tradeoff

* Investigate bias-variance tradeoff based on VanderPlas: [05.03-Hyperparameters and model validation](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/05.03-Hyperparameters-and-Model-Validation.ipynb)
* Implement polynomial regression with simulated datasets
* Revisit (with scikit-learn) the topics in Chapter 2 of ISLR2

[bias-regression.md](bias-regression.md)
