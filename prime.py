def print_primeNUm():
	max=int(input("enter the number till which you want to get prime number"))
	for num in range(2,max+1):
		for i in range(2,num):
			if(num%i)==0:
				break
		else:
			print(num)
print_primeNUm()
