
# 01 -- Intro

## Goals

* Introductions
* Course overview
* Tools -- Git, Github, Colab and libraries

## links

* repo for class notes: https://github.com/ds5110/spring-2023
* polleverywhere: https://PollEv.com/pbogden
* [scratch notebook](https://colab.research.google.com/drive/1H4sj-XdST_PqBXQTrkutsamSFrOs2wNG) -- shared

## Reading and exercises

In preparation for class next week...

* ISL
  * Ch 1: [ISL](https://www.statlearning.com/) -- Background and notation
    * Bring any questions if you have on this chapter to class.
  * Ch 2: [ISL](https://www.statlearning.com/) -- Intro/overview
    * We'll review Section 2.1 in class, so bring any questions you have on this section.
    * We'll implement some of the material in Python.
    * Skim Section 2.2 -- the material is important and we'll get to it at some point.
    * We won't cover Sections 2.3 and 2.4, which depend on R.
* PDS -- matplotlib
  * We'll start working with seaborn and matplotlib next week to visualize and work with tidy data.
  * PDS github repo: https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/
  * Read the following notebooks, and experiment by running the code in Colab...
    * 04.00-Introduction-To-Matplotlib.ipynb
    * 04.01-Simple-Line-Plots.ipynb
    * 04.02-Simple-Scatter-Plots.ipynb
  * These notebooks use numpy -- make sure you understand what's going on.
    * If numpy is new to you, then look at relevant notebooks in Chapter 2 of PDS
* [Seaborn data structures](https://seaborn.pydata.org/tutorial/data_structure.html) -- pydata.org
  * This section in the Seaborn documentation describes "tidy" data
  * Experiment with Seaborn by running the following code (from the seaborn documentation) in Colab.
  ```
  # Ref: https://seaborn.pydata.org/tutorial/data_structure.html
  import seaborn as sns

  flights = sns.load_dataset("flights")
  flights.head()
  ```
  * If you run the code above in one cell, then run the next line in another cell to produce the plot
  ```
  sns.relplot(data=flights, x="year", y="passengers", hue="month", kind="line");
  ```
  * If this is new to you, then look at the scratch notebook (link above)
    * I've set up a notebook that runs some code.
    * Seaborn uses Pandas DataFrames by default.
    * If this is new to you, then look at the introductory notebooks in Chapter 3 of PDS
* [How to ask a good question](https://stackoverflow.com/help/how-to-ask) -- stackoverflow.com
  * It's important to know how to ask a good technical question.
  * Stackoverflow can be a great resource for answering good questions and debugging, provided it's used well.
  * Be careful about how you use google and stackoverflow. And be super careful about random blogs.
* For awareness...
  * [Ch 12: R4DS](https://r4ds.had.co.nz/tidy-data.html)
    * "Tidy data" is a adopted from the R community
  * [Introduction to licenses](https://observablehq.com/@observablehq/licenses) -- observablehq.com
    * Attribution and licenses are important when using published work.
    * Remember [Northeastern's academic integrity policy](https://osccr.sites.northeastern.edu/academic-integrity-policy/)
    * Copy and paste could have legal implications that extend beyond academic integrity (unlikely for us right now).

## Introductions

Brief introductions.

## Overview

[history](history.md)

## Syllabus

[syllabus](syllabus.md)

## Projects

* [stinky2](https://ds5110.github.io/stinky2/)

## Github intro

* [Github Quickstart](https://docs.github.com/en/get-started/quickstart)
* Make sure you can clone a repo, make local changes, and push them back to github.
* Bring questions next time if you have difficulty or connect during office hours.

## Q: R or Python?

* R or Python or...?
  * [Berkeley](https://bootcamp.berkeley.edu/blog/most-in-demand-programming-languages/)
  * [Northeastern](https://www.northeastern.edu/graduate/blog/most-popular-programming-languages/)
  * [Tiobe index](https://www.tiobe.com/tiobe-index/)
* R perspective
  * Data science overview -- [Hadley Wickham's perspective](https://r4ds.had.co.nz/explore-intro.html)
  * [ISL online course](https://www.statlearning.com/online-course)
  * [Lecture 1](https://youtu.be/5N9V07EIfIg) -- youtube
* Python perspective
  * [NumPy.org](https://numpy.org/)
    * The feature gallery on the home page is worth reviewing
    * The core of NumPy is well-optimized C code
    * [Black Hole case study](https://numpy.org/case-studies/blackhole-image/)
    * Note [the data-processing pipeline](https://numpy.org/case-studies/blackhole-image/#the-challenges)
  * [Python for data analysis](https://wesmckinney.com/) (2022) by Wes McKinney
    * McKinney's book focusses on "structured data" -- tidy/tabular
    * [1. Preliminaries](https://wesmckinney.com/book/preliminaries.html)
    * [Why Python?](Reviews the core packages)

## Student responsibilities

* python -- the latest release installed locally
* editor -- vscode, or others (e.g., vim), but not atom as it was deprecated over the summer:-(
  * [vim - vscode](https://www.cs.cmu.edu/~07131/f20/topics/readings/week-4/week-4-vim-vscode.pdf) -- cmu.edu
  * [vscode & vim](https://marketplace.visualstudio.com/items?itemName=vscodevim.vim) -- visualstudio.com
* REPL -- make sure you can run code from the command line (REPL = read-eval-print-loop)
  * PDS discussed this, as does McKinney
* Installation
  * PDS has recommendations for using miniconda in Chapter 1 of the 2nd edition
  * McKinney's book as well: [Installation](https://wesmckinney.com/book/preliminaries.html#installation_and_setup)
    * Section 1.3: Essential Python Libraries
    * Section 1.4: Installation and setup

## In-class exercise -- colab intro

* [Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook) by Jake VanderPlas
  * The book is available as jupyter notebooks that open automatically in Colab
  * [Colab](https://colab.research.google.com/)
  * [Colab & Tensorflow](https://youtu.be/inN8seMm7UI)
    * Video featuring Jake VanderPlas
* Colab -- https://colab.research.google.com/
  * Colab is Jupyter as a service, with GUI improvements & GPU access (and an underlying business model)
  * Authenticate with your "husky.neu.edu" email -- just replace "northeastern.edu" with "husky.neu.edu"
  * Colab and jupyter are for prototyping and in-class exercises, but NOT for code submission.
  * You can share Colab notebooks, but editing is not synchronous.  You need to "save" explicitly.
* Accessing the iris dataset from Colab
  * Look here: https://github.com/mwaskom/seaborn-data/blob/master/iris.csv
  * Use the "raw" link
  * `!curl -O "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"`

## Command line...really?

* The following excerpts come from [this Nature article](../resources/nature_observable.pdf)
  * "Reactive, reproducible, collaborative: computational notebooks evolve" by Jeffrey Perkel, Nature, p156, Vol 593, 6 May 2021
  * "A 2019 study found that just 24% of 863,878 publicly available Jupyter notebooks on GitHub could be successfully re-executed, and only 4% produced the same results."
  * "Notebooks are messy. You write stuff, keep old crusty code behind, and it's hard to kind of figure out which cells to execute in the right order because you're trying different things."
* For these and other reasons...
  * Colab for prototyping & class interactions
  * GitHub for assignments & projects

## In-class exercise -- colab

* [colab.md](colab.md)

## In-class exercise -- Earthquakes

* [my notebook](https://colab.research.google.com/drive/1nT2yKBAJ-rm7MysxeNVe74Uao0G2a4l3)


