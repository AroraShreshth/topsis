# TOPSIS Python Package 

Made by [Shreshth Arora](http://shreshtharora.com)

This is a package made for implementation of TOPSIS in [UCS538](https://psrana.com/ucs538) course at [Thapar Institute of Engineering and Technology](http://thapar.edu) . 

This Repository will be activily maintained and more features will be added to it as time progress. The below is the impmentation of the using the python package in it's current state.

## What is Topsis ?

Technique for Order Preference by Similarity to Ideal Solution (TOPSIS) originated in the 1980s as a multi-criteria decision making method. TOPSIS chooses the alternative of shortest Euclidean distance from the ideal solution, and greatest distance from the negative-ideal solution.

It is a method of compensatory aggregation that compares a set of alternatives by identifying weights for each criterion, normalising scores for each criterion and calculating the geometric distance between each alternative and the ideal alternative, which is the best score in each criterion.

### Install from pip

> pip install topsis-shreshth-101803503

### Run in Command Prompt

> topsis data.csv "1,1,3.5,0.34"  "-,+,+,-" result.csv

### Dataset used for testing

| Model | Correlation | R<sup>2</sup> | RMSE | Accuracy |
| ----- | ----------- | ------------- | ---- | -------- |
| M1    | 0.79        | 0.62          | 1.25 | 60.89    |
| M2    | 0.66        | 0.44          | 2.89 | 63.07    |
| M3    | 0.56        | 0.31          | 1.57 | 62.87    |
| M4    | 0.82        | 0.67          | 2.68 | 70.19    |
| M5    | 0.75        | 0.56          | 1.3  | 80.39    |


#### Final Result is stored in csv format by name of your choice
