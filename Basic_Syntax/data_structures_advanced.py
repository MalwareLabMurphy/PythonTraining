## NB: Remove hashtag/octothorpe from beginning of a given command in order to execute.

## Will first import pprint to make everything pretty!

from pprint import pprint

## Dictionaries of Lists

#names= ['Murphy', 'Molly', 'Milo', 'Maggie']
#breeds= ['Lab', 'Pointer', 'Tabby', 'Tabby']

#pets= {
    #'name': names,
    #'breed': breeds
#}

#pprint(pets)

## Can also do with 'X in range'

#names= ['Murphy', 'Molly', 'Milo', 'Maggie']
#breeds= ['Lab', 'Pointer', 'Tabby', 'Tabby']

#for x in range(len(names)):
    #n=names[x]
    #b=breeds[x]
    
    #print(f'{n} is a {b}')
    
##List comprehension: at least one expression, at least one transformation clause

#names= ['Murphy', 'Molly', 'Milo', 'Maggie']

#upper_pets=[]
#for n in names:
    #upper_pets.append(n.upper())
    
#upper_pets

## Easier way to do this...

#names= ['Murphy', 'Molly', 'Milo', 'Maggie']

#upper_pets= [p.upper() for p in names]
    
#upper_pets

## Dictionary comprehension: still transformation and expression

#names= ['Murphy', 'Molly', 'Milo', 'Maggie']
#ages= [7, 2, 13, 9]

#pet_ages = { n:a for (n,a) in zip(names,ages)}
#pet_ages

## Another simpler way to do this...

names= ['Murphy', 'Molly', 'Milo', 'Maggie']
ages= [7, 2, 13, 9]

pet_ages = dict(zip(names,ages))
pet_ages