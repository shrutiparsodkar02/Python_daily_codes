def cal_fabonaci():
	max=int(input("enter the number till which you want to get fabonaci series"))
	n1=0
	n2=1
	c=2
	if max==0:
		pass
	elif max==1:
		print(n1)
			
	else:
		print(n1)
		print(n2)
		while(c<max):
			
			n3=n1+n2
			print(n3)
			n1=n2
			n2=n3
			c+=1
			
		
			
			
cal_fabonaci()
