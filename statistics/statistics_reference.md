# Statistics
Implementations of important measures and algorithms from scratch. 

The motivation for the implementations from scratch is that these are great ways to describe large amounts of data, and implementing them by hand is the best way to understand how they work. 

These functions can also be found in my python module `statistics.py`, and can be imported for any project. 

# Central Tendencies

Usually want some measure of where the data is centered. We can use...

## Mean
- average, good first glace at central tendency. 
- depends on every single point, sensitive to outliers. 
- sum of data divided by amount of data points:
```python
def mean(data: List[float]) -> float:
    # sum() and len() well defined since we have a list of floats. 
    return sum(data)/len(data)

mean(data) # returns mean of list of data. 
```

## Median
- less sensitive to extreme outliers, since it measures the halfway point of the data. 
- different functions for even and odd cases:
  - code includes underscore notation for *private* functions in python (only means to be called by our internal median function, not other users):
    - [discussion on "privacy" in python](https://stackoverflow.com/questions/1547145/defining-private-module-functions-in-python)
    - [more information on private methods](https://www.geeksforgeeks.org/private-methods-in-python/)

- my implementation of median: 
```python
def _median_even_case(data: list[float])-> float:
    # average of two middle elements in list:
    middle = int((len(data) / 2) - 1)
    low_mid = data[middle]
    high_mid = data[middle + 1]
    return (low_mid + high_mid)/2

def _median_odd_case(data: list[float])-> float:
    # just the middle of the data:
    middle = (len(data) / 2) - 1  # indexing starts at 0
    #print(middle)
    true_mid = data[math.ceil(middle)]
    #print(true_mid)
    return true_mid


def median(data):
    # TODO - validate that the list is sorted
    if len(data)%2 == 0:
        return _median_even_case(data)
    else:
        return _median_odd_case(data)
    return "invalid input! check the list"
```
- issue with this implementation is that it can only take in sorted input, so future additions must only allow sorted input or sort the input.

- TODO: add sorting sub-function to statistics package. 

### Quantiles

Generalization of the median
- median is the "half" quantile. it is the value under which $50%$ of the data lies. 

implementation of quantiles:

```python
"""
quantile:

input - a percent value, ex: 0.10 = 10%, which markes the percentile value, must be a sorted list!
output - the percentile in the dataset
"""

def quantile(data:list[float], p: float) -> float:
    # TODO - validate that the list is sorted
    p_index = int(p*len(data)) # get the interger marking the percentile in the data

    return data[p_index]


```
- as with the median, the list needs to be sorted, but we can implement this at a later time. 

## Mode

- less common but still useful
- counts the most common values in the dataset
- the output should be a list to account for the fact that two or more values could be tied for highest frequency. 
- implementation here:

```python

"""
first version of implementation:
"""

def mode(data: list[float]) -> list[float]:
    # keep the count in a list
    for x in data:
        



```
