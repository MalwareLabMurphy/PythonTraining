## NB: Remove hashtag/octothorpe from beginning of a given command in order to execute.

## Analysis using "series" and "dataframes". Series = one-dimensional, Dataframes = two-dimensional.

## Import pandas into program...

import pandas as pd

## Pandas has read csv function (will use dummy CSV files while learning syntax). Must be run in same folder or reference the file structure.

#treats_df = pd.read_csv('murphy_treat_budget.csv')
#treats_df

## Additional functions that can be run with Pandas:

#treats_df.head() ## Preview first 5 rows
#treats_df.head(2) ## Preview first 2 rows
#treats_df.tail() ## Preview last 5 rows
#treats_df.columns ## Present list of columns
#treats_df.describe() ## List of common statistical calculations
#treats_df.sort_values(by='Treat_Cost') ## Sort records by specificied value
#treats_df.sort_values(by='Treat_Cost', ascending=False) ## Sort records in descending order

## Can also produce a DataFrame using List of Dictionaries...

pets = [{'pet_no': '1', 'pet_name': 'Murphy', 'daycare_cost': 100},
        {'pet_no': '2', 'pet_name': 'Molly', 'daycare_cost': 80},
        {'pet_no': '3', 'pet_name': 'Milo', 'daycare_cost': 50},
        {'pet_no': '4', 'pet_name': 'Maggie', 'daycare_cost': 50}]

pets_df = pd.DataFrame(pets)
pets_df

## ...or as a Dictionary of Lists!

#pets = {
    #'pet_no': ['1', '2', '3', '4'],
    #'pet_name': ['Murphy', 'Molly', 'Milo', 'Maggie'],
    #'daycare_cost': [100, 80, 50, 50]
#}

## Other functions...

#pet_name= pets_df[pet_name] ## Extract column as a series
#pet_name_list=list(pet_name) ## Then convert that column to a list

## Can replace description() function from above with various statistics (count, min, max, mean, etc.).