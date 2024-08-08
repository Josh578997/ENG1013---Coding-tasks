deck = [5, 7 ,1, 9, 2, 8, 12, 11, 4, 3, 10, 6]

#optimised bubble sort
for a in range(len(deck)-1,0,-1):
    swapped = False
    for i in range(len(deck)-1):
        if deck[i] > deck[i+1]:
            tmp = deck[i]
            deck[i] = deck[i+1]
            deck[i+1] = tmp
            swapped = True
    if not swapped:
        break

print(deck)
