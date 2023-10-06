##NB: Remove hashtag/octothorpe from beginning of a given command in order to execute.

##Use dictionaries to set KV pairs in Python. Created with curly brackets.

#pet={
    #'name' : 'Murphy',
    #'species' : 'Dog',
    #'age' : 7
#}
#pet['name']

##To make it look better, from pprint import pprint!

##Delete entries from dictionary with "del"

#pet={
    #'name' : 'Murphy',
    #'species' : 'Dog',
    #'age' : 7
#}
#del pet['age']
#print(pet)

##Use "in" to determine if dictionary has certain key.

#pet={
    #'name' : 'Murphy',
    #'species' : 'Dog',
    #'age' : 7
#}
#if ('name' in pet):
    #print("This pet has a name.")
#else:
    #print("No name yet...")
    
##List keys or values with .keys() or .values(). List items with items(), KV pairs represented as tuples.

#pet={
    #'name' : 'Murphy',
    #'species' : 'Dog',
    #'age' : 7
#}
#pet_items=pet.items()
#for i in pet_items:
    #print(i)
    
##List of dictionaries for use in PANDAS...

pets=[{
    'name' : 'Murphy',
    'species' : 'Dog',
    'age' : 7},
    {'name' : 'Molly',
    'species' : 'Dog',
    'age' : 2},
    {'name' : 'Milo',
    'species' : 'Cat',
    'age' : 13},
    {'name' : 'Maggie',
    'species' : 'Cat',
    'age' : 9}]
for p in pets:
    print(p['name'])