## NB: Remove hashtag/octothorpe from beginning of a given command in order to execute.

## Import pandas into program...

import pandas as pd

pets = [{'pet_no': '1', 'pet_name': 'Murphy', 'pet_type': 'dog', 'daycare_cost': 100},
        {'pet_no': '2', 'pet_name': 'Molly', 'pet_type': 'dog', 'daycare_cost': 80},
        {'pet_no': '3', 'pet_name': 'Milo', 'pet_type': 'cat', 'daycare_cost': 50},
        {'pet_no': '4', 'pet_name': 'Maggie', 'pet_type': 'cat', 'daycare_cost': 50}]

pets_df = pd.DataFrame(pets)
pets_df

## Can append items to DF

marky_dict={'pet_no': '5', 'pet_name': 'Marky', 'pet_type': 'horse', 'daycare_cost': 200}
pets_df=pets_df.append(marky_dict, ignore_index=True)

## Find data with "loc" and "iloc".

#pets_df.iloc[0] ## Returns first row of DF as series
#pets_df.iloc[1,1] ## Returns second row, second column (Index starts with 0!)
#pets_df.iloc[1,:] ## Row two, ALL of the columns
#pets_df.iloc[:,1] ## All of the rows, column two
#pets_df.iloc[:,1:2] ## Similar to above, range does NOT inclide second value
#pets_df.iloc[:,1:3] ## All rows for second and third columns
#pets_df.iloc[1:4,1:4] ## Rows 2-4, Columns 2 and 3

## Loc function similar to iloc, but accepts CONDITION for records.

#pets_df.loc[pets_df['daycare_cost']==50] ## Records where daycare cost = 50
#pets_df.loc[pets_df['daycare_cost'] > 50] ## Records where daycare costs > 50
#pets_df.loc[pets_df['pet_name'].str.contains('a')] ## Returns pets with an "a" in their name
#pets_df.loc[pets_df['pet_name'].str.contains('mag', case=False)] ## Case insensitive version of "contains"
#pets_df.loc[pets_df['pet_name'].str.startswith('Ma')] ## Records that start with "Ma"


## Pandas has "fillna" function for records with null values.

#pets_df = pets_df.fillna('')

## Ability to aggregate using "groupby" function.

#pet_type_df= pets_df.groupby('pet_type')

## Aggregate function examples...

#pet_type_df.count() ## Counts by pet type
#pet_type_df['daycare_cost'].min() ## Smallest daycare cost by pet type

## Can bin by ranges and label them too.

dcc_bins = [0, 75, 150, 300]
dcc_labels = ['Low', 'Medium', 'High']
dcc_tier = pd.cut(pets_df['daycare_cost'], bins=dcc_bins, labels=dcc_labels)
pets_df['daycare_cost_tier'] = dcc_tier
pets_df

## For help with how a function works, put a "?" after it.