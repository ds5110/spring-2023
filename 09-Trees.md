
# 09-Trees

* projects (revised timeline)
* EDA of multidimensional data with maps (earthquakes II)
* model selection & feature importance -- regularization

## Reading (for next week)

* ISLR2 -- Chapter 8, Section 8.1: The Basics of Decision Trees
* ISLR2 -- Chapter 8, Sections 8.2.1: Random Forests, 8.2.2: Bagging, 8.2.3: Boosting
* ISLR2 -- Chapter 9, Sections 9.3.1: Support Vector Machines
  * Read for the concepts related to "Classification with Non-Linear Decision Boundaries"
  * After skimming 9.3.1 the first time, you may want to refer back to other parts of Chapter 9
  * We'll be applying the concepts in class and in homework assignments.
  * Don't miss Section 9.5 -- if nothing else, skim it!

## Notebooks

* [09-geopandas.ipynb](https://colab.research.google.com/drive/1lSlWcg1Z9s6uCRTRxYavAMdY0odxjZUE)
* [09-airports-to-earthquakes.ipynb](https://colab.research.google.com/drive/1V4irrK5ex39u9WVETcwqVR-NR0nFJ2l3)
* [09-observable-filtered-earthquakes](https://colab.research.google.com/drive/1wlrA5lnadw4_y-byzAEgliIPZ65ThO3Y)
* [09-observable-filtered-earthquakes](https://colab.research.google.com/drive/1wlrA5lnadw4_y-byzAEgliIPZ65ThO3Y)
* [scratch-notebook](https://colab.research.google.com/drive/1H4sj-XdST_PqBXQTrkutsamSFrOs2wNG)
* [poll everywhere](https://pollev.com/pbogden)

## Projects

* Revised [plan](plan.md)

## EDA with geopandas

* [09-geopandas.ipynb](https://colab.research.google.com/drive/1lSlWcg1Z9s6uCRTRxYavAMdY0odxjZUE)
  * Revisiting geopandas
  * Geospatial ecosystem
  * Contextily for static images of interactive maps

## EXERCISE: Multidimensional EDA of earthquakes

* What's going on in AK? Recall...
  * We did GeoPandas and observable-quakes in 02-DataViz and 03-Tidy
  * We investigated histograms and spatial dependence
* What we found...
  * Last time -- we found that small quakes were located over the US
  * Last time -- there were hints of time dependence in the histograms
  * Last time -- there was a swarm of earthquakes over AK
* It's time to explore what's going on in AK -- what's the story up there?
  * Features options -- magnitude, time, lat, lon, depth, etc.
  * [USGS earthquake feeds](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php)

## Interactive EDA

* [09-airports-to-earthquakes.ipynb](https://colab.research.google.com/drive/1V4irrK5ex39u9WVETcwqVR-NR0nFJ2l3)
  * observable-jupyter demo
* [09-observable-filtered-earthquakes](https://colab.research.google.com/drive/1wlrA5lnadw4_y-byzAEgliIPZ65ThO3Y)

## Feature importance and model selection

* [Feature importances with a forest of trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html)
  * This demo uses simulated data with `make_classification`
  * Application of the scikit-learn estimator API with a new model type: random forest
  * Built-in model-specific metrics for assessing feature importance based on "impurity decrease"
* EXERCISE
  * assess feature importance visually 

## Regularization


