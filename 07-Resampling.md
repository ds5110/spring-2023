# 07-Resampling

* bias-variance tradeoff (overfitting & underfitting)
* estimating true and test MSE (training and validation scores, high and low-variance models)
* cross validation and the "best" model -- tuning model complexity

## notebooks

* [06-default-naive-bayes-exercises.ipynb](https://colab.research.google.com/drive/1VIB7_4mLNiGCOI7f3EkEEQmLA2r-B7Z_)
* [07-validation-curve-exercises.ipynb](https://colab.research.google.com/drive/1FcNLs5iN2rwCkyK-odHe-1sMeOepKoEp)
* [scratch-notebook](https://colab.research.google.com/drive/1H4sj-XdST_PqBXQTrkutsamSFrOs2wNG)
* https://pollev.com/pbogden

## Reading (for next week)

* ISLR2 -- Chapter 6.1-6.4: Model selection
  * There's a fair amount of reading. Try to get the main concepts and don't get caught up in the math.
  * In particular, try to understand the main points of subset selection and shrinkage methods.
  * Skim the section on Cp, AIC, BIC, and Adjusted R2.
  * Lasso and Ridge are important: How do they work? Why might you want to use one versus the other?
  * If you're not familiar principal components, then read 6.3 for an introduction to the concepts.
  * High dimensional situations. What does it mean to be high-dimensional? What are some problems that arise? 
* [05.09-Principal-Component-Analysis.ipynb](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/05.09-Principal-Component-Analysis.ipynb)
  * VanderPlas has a good section on principal components implemented in Python. It's worth a look.

## Naive Bayes

* Continued from last time -- naive Bayes
* Gaussian naive Bayes is a [generative model](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/05.05-Naive-Bayes.ipynb)
* Bayes classifier (ISL p37, Eqn 2.10) maximizes Pr(Y = j|X = x_0) -- minimizes the test error rate (eqn 2.9)

## Assessing model accuracy

* reducible and irreducible error (ISL p18)
* training and test error -- "we don't care about training MSE, but we want to minimize test MSE"
* model selection by comparing test MSE to optimal "flexibility"
* VanderPlas calls this a validation curve (validation score vs model complexity)
* ISL slide 16 in Ch2_Statistical_Learning.pdf -- interpretability vs flexibility
