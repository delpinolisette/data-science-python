# How can I work with data with dates?

### Step 1: Create your pandas dataframe with date options:
- set the `parse_dates=True` option in the `pandas.read_csv('directory/filename.csv', parse_dates=True, index_col='date')` and map your index columns whichever column name corresponds to the dates in the original csv with `index_col=name_date_column`
- It is always a good idea to set your index column to track dates rather than traditional indices (0,1,2,...)

### Step 2: 
- subset your data my week, month, etc and produce new dataframe for analysis and plotting. 
- example method: I want to subset a Covid case tracking data frame with dates in the index column, in the form `yyyy-mm-dd` ,and make a new dataframe tracking covid cases by week:
``` python
cases_by_week = doc_df.resample('7D')['positive_cases'].sum().to_frame()
```