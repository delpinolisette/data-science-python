# Cheat Sheet of All Things Learned
TOC:
1. assig 1
2. assig 2
3. assig 3
4. assig 4
5. assig 5
6. assig 6
7. assig 7
8. assig initial project proposal
9.  example assigment
10. final proj folder
11. group 9 -2 2020
12. lab ses 1
13. lab ses 2
14. lab ses 3
15. lab ses 4
16. lab ses 5
17. lab ses 6
18. lab ses 7
19. lab ses 8
20. lab ses 9
21. lec 0 
22. lec 10
23. lec 1
24. lec 2
25. lec 3
26. lec 4
27. lec 5
28. lec 6
29. lec 7
30. lec 8
31. lec 9
32. using github


---

# Things Learned from 1:
- '%matplotlib inline' is a magic function that displays matplotlib backend in line and also saves the plots. [more info here](https://stackoverflow.com/questions/43027980/purpose-of-matplotlib-inline)
- `sorted(list)` returns a sorted list, useful in testing such as `assert(sorted(county)==['Armstrong', 'Crawford', 'Dauphin', 'Fulton', 'Philadelphia'])`
- `list_name.index('item whose index i want')` function is useful for returning index. 
### Testing Sample Code:
```python
assert(var_name==534)
assert(bool_name==False)
```
### `Enumerate`

`enumerate(list_name)` turns a list into index, list_item pair. Good for iterating :
```python
for idx, name in enumerate(county):
    
    if wagner[idx] > wolf[idx]:
        won = 'Wagner'
        winner.append(won)
    else:
        won = 'Wolf'
        winner.append(won)
        
    print('{} won in {} county'.format(won,name))
```
`help(enumerate)` gives extra info. 

### All Visualization Examples

```python
plt.hist(male, alpha=0.5, label='male')
plt.hist(female, alpha=0.5, label='female')
plt.legend()
plt.vlines([fmean, mmean], *plt.ylim(), linestyles='dashed')


plt.xlabel("height (inches)", fontsize=12)
plt.title("Distribution of heights for adult females and males")

```
- `ord(character)` is the inverse of the `char(num)` function. returns the unicode corresponding to the character passed in. 
- `zip` function aligns a number of lists of the same length. The output of a zipped list is a tuple of aligned list items. Example:
```python
zipped = zip(state, candy, amount)

for trp in zipped:
    if trp[1] == 'Skittles':
      skittle_state.append(trp[0])
      skittle_amount.append(trp[2])
```

# Things Learned from 2

- in markdown can have some light HTML:

```html
<img src="img/nytimes_art.png" width="400px" style="float: left; padding: 10px; margin-right:20px;"/>

<div style="padding: 30px; ">

<h3>Some quotes from the article:</h3>

<blockquote style="background-color: #ffffcc">
    Test1
</blockquote>

<blockquote style="background-color: #ffcccc">Test 2</blockquote>
 
</div>
```


- example: to load in a data frame:

`rem_df = pd.read_csv("data//sleeping_mammals.csv")`

- can check we've created a data frame with `assert(type(rem_df)==pd.DataFrame)`
- to get shape of the data frame try: 

```python
s = rem_df.shape
nrows = s[0] # number of rows
ncols = s[1] # number of columns
```
- to take a *random* sample from the data frame, try `rsample = rem_df.sample(12)`
- 