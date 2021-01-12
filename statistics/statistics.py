import math

# TODO: set up constructor and turn into a proper module

def mean():
    return -1

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
    if len(data)%2 == 0:
        return _median_even_case(data)


def mode():
    return -1



# driver code
d = [1,2,3,4]
print(median(d))

# median case works! now check odd case

d = [1,2,3,4]
print(median(d))