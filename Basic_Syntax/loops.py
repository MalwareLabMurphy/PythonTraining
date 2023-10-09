## NB: Remove hashtag/octothorpe from beginning of a given command in order to execute.


## FOR loops and WHILE loops used to iterate over a sequence.
## BREAK statement to end loops.
## Functions such as RANGE with parameters START, STOP, STEP.

## Spell Out Individual Letters

#name = "Murphy the Malware Lab"

#for l in name:
    #print(l)
    
## Print Items in a List in Order

#names= ["Murphy", "Molly", "Milo", "Maggie"]

#for name in names:
    #print(name)

## Calculating Dog Treats with While Loop

#dog_treats= 50

#while dog_treats > 0:
    #dog_treats=dog_treats - 5
    #print(f"You ate 5 dog treats and now have {dog_treats} remaining.")
    
#print(f"You have {dog_treats} left... guess it's time to buy more!")

## Iterating Over a Range (Count by 3s)

#for x in range (1, 20, 3):
    #print(x)

## Infinite Loop: Dog Licking Foot

while(True):
    print("Dog is licking your foot.")
    
    lick_loop = input("Say STOP to make the dog stop:")
    
    if(lick_loop == "STOP"):
        print("Okay he finally stopped.")
        break
