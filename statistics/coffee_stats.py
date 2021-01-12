# monte carlo methods :
# six types of coffee offered at store
# equal chance of getting each
# how many times must you go to the store before getting each type of coffee?

from random import seed
from random import random



coffee_1 = 0
coffee_2 = 0
coffee_3 = 0
coffee_4 = 0
coffee_5 = 0
coffee_6 = 0


for x in range(100):
    x = random()

    if (x >=0) and (x < (1/6)):
        coffee_1 +=1
    if (x >=(1/6)) and (x < (2/6)):
        coffee_2 +=1
    if (x >=(2/6)) and (x < (3/6)):
        coffee_3 +=1
    if (x >=(3/6)) and (x < (4/6)):
        coffee_4 +=1
    if (x >=(4/6)) and (x < (5/6)):
        coffee_5 +=1
    if (x >=(5/6)) and (x < 1):
        coffee_6 +=1
    
print(coffee_1, coffee_2, coffee_3, coffee_4, coffee_5,coffee_6)



def go_to_store(visits):
    


