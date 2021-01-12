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
```python
    # private helper functions first:

    def _median_odd_case(data: list[float])-> float:
      # average of two middle elements in list:
      middle = len(data) / 2
      low_mid = math.floor(middle)
      high_mid = math.ceil(middle)
      return (low_mid + high_mid)/2
    

    def _median_even_case(data: list[float])->float:
      # 
```

### Mode

