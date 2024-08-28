# extracting repeated items

list = [10,5,6,7,2,1,3,7,7,7,2,3,1,5,6,7,1,11,15,17,18,18,20,21,20,21]
repeated = []
remaining = []

for i in list:
    if i in remaining:
        if i in repeated: continue
        else: repeated.append(i)
    else: remaining.append(i)

remaining.sort()
repeated.sort()
print("All Items without repeat are : ", remaining)
print("Repeated Items are : ", repeated)
