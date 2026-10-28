sets={10,20,30,40,50}

num=int(input("Enter a any number in set: "))
if num in sets:
    print(f"{num} is found in set.")
else:
    print(f"{num} is not found in set.")
    