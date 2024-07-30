str1=input("enter the string  ")
substr2=input("enter the substring  ")
if((str1.find(substr2))==-1):
	print(substr2+" not found in the string")
else:
	print(substr2+" found in the string ")
