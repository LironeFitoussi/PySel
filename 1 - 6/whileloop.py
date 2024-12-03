it = 10

while it >= 1 :
    if it == 9:
        it = it - 1
        continue   
    if it == 3:
        break
    print(f"Value of 'it' is {it}")
    it = it - 1
    
print("While loop is done")