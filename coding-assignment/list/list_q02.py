# concate two list index wise 
list1 = ["m","na","i","DE"]
list2 = ["y","me","s","EPTI"]
list3 = [i+j for i, j in zip(list1,list2)]
print(list3)