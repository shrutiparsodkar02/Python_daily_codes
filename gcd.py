l1=[];
def getlcm(l3):
	while l3 !=[]:
		n=l3.pop();
		print(n);
		for i in range(1,n+1):
			if(n%i==0):
				l1.append(i);
	return l1;

	


