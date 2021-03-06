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
    else:
        return _median_odd_case(data)
    return "invalid input! check the list"


def mode(data: list[float]) -> list[float]:
    modes = []
    value_frequencies = {}

    # keep the count in a dictionary
    for x in data:
        value_frequencies[x] = 0
        print(value_frequencies[x])
    
    for x in data:
        value_frequencies[x] += 1
        print(value_frequencies) # eureka!
    
    #print(max(value_frequencies.values())) # ok but how do i get its key

    for key in value_frequencies:
        if value_frequencies[key] == max(value_frequencies.values()):
            modes.append(key)
    print(modes, "are modes")
        
    return modes
        
    


"""
# driver code
d = [1,2,3,4]
print(median(d))

# median case works! now check odd case

d = [1,2,3,4,5]
print(median(d))
mode([1,2,3,3,4,4])

"""

