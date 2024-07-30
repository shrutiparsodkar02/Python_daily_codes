l1=[10,20,30,40]
num1=int(input("enter the element you want to search"))
for i in l1:
	if num1==i:
		print("element found in index "+l1[i])
else:
	print("not found ")
