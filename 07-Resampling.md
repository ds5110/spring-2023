# 07-Resampling

* bias-variance tradeoff (overfitting & underfitting)
* estimating true and test MSE (training and validation scores, high and low-variance models)
* cross validation and the "best" model -- tuning model complexity

## notebooks

* [06-default-naive-bayes-exercises.ipynb](https://colab.research.google.com/drive/1VIB7_4mLNiGCOI7f3EkEEQmLA2r-B7Z_)
* [07-validation-curve-exercises.ipynb](https://colab.research.google.com/drive/1FcNLs5iN2rwCkyK-odHe-1sMeOepKoEp)
* [scratch-notebook](https://colab.research.google.com/drive/1H4sj-XdST_PqBXQTrkutsamSFrOs2wNG)
* https://pollev.com/pbogden

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
