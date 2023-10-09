## NB: Remove hashtag/octothorpe from beginning of a given command in order to execute.

## Lists are created with angle brackets - []

#names=["Murphy", "Molly", "Milo", "Maggie"]
#print(names)

## Print individual items in list with loops!

#names=["Murphy", "Molly", "Milo", "Maggie"]
#for x in names:
#    print(x)

## Lists are indexed, starting at '0'. Can print location with index function.

#names=["Murphy", "Molly", "Milo", "Maggie"]
#print(names[0])

#names=["Murphy", "Molly", "Milo", "Maggie"]
#print(names.index("Milo"))

## Append function can add items to end of list. Insert function can add at specific position. Remove will... remove!

#names=["Murphy", "Molly", "Milo", "Maggie"]
#names.append("Marky")
#print(names)

#names=["Murphy", "Molly", "Milo", "Maggie"]
#names.insert(2, "Marky")
#print(names)

#names=["Murphy", "Molly", "Marky", "Milo", "Maggie"]
#names.remove("Marky")
#print(names)

## Sort function will sort in ascending order... reverse=True for descending

#names=["Murphy", "Molly", "Milo", "Maggie"]
#names.sort()
#print(names)

#names=["Murphy", "Molly", "Milo", "Maggie"]
#names.sort(reverse=True)
#print(names)

## Len function will count items in list.

#names=["Murphy", "Molly", "Milo", "Maggie"]
#len(names)

## Lists are MUTABLE, not tuples! Tuples closed in parentheses.

(name, animal) = ("Murphy", "Dog")
print(name)

