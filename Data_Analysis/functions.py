## NB: Remove hashtag/octothorpe from beginning of a given command in order to execute.

## Define function using "def" command.

#name = 'Murphy'

#def introduce():
    #print(f'Hello, my name is {name}!')
    
#introduce()

## Also define function to accept arguments.

#age= 7

#def introduce(name):
    #print(f'Hello, my name is {name}, and I am {age} years old!')
    
#introduce('Murphy')

## Here's another!

#treat_number=5
#pet='Murphy'

#def feed_pet(feed_amt, pet):
    #total_food = feed_amt + treat_number
    #return f'{pet} has now eaten {total_food} treats today.'

#feed_pet(5, pet)

## Lambda functions- limited and short.

treat_number=5

feed_pet = lambda treats, treat_number: treat_number + treats

total_treats=feed_pet(5, treat_number)
total_treats