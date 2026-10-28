A={1,2,3,4}
B={3,4,5,6}

#Find all unique numbers in A and B.
symmetric_difference=A ^ B
print(f"The unique numbers are in both sets:",symmetric_difference)


#Find elements common to both sets.
intersection=A & B
print(f"The common numbers are in both sets:",intersection)


#find A-B and B-A explain why their result differ.
print(f"The A-B is: ",A-B)
print(f"The B-A is :",B-A)
#A-B: B's same elements are subtracted from A, it shows remening elements in A. 
#B-A: A's same elements are subtracted from B, it shows remening elements in B.
# thats why both results are different. 


#Find elements in either A or B, both not in boths.
symmetric_difference=A ^ B
print(f"The elements are A or B but not in both:",symmetric_difference)


