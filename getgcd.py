def get_common_factors(n):
	l1=[];
	for i in range(1,n+1):
		if(n%i==0):
			l1.append(i);
	return l1;

def get_gcd(list1,list2):
	#list1=get_common_factors(4);
	#list2=get_common_factors(2);
	while(list1 !=[] and list2 !=[]):
		n1=list1.pop();
		n2=list2.pop();
		if(n1==n2):
			return n1;
		elif(n1>n2):
			list2.append(n2);
		elif(n1<n2):
			list1.append(n1);
	return 1;
#print(get_gcd());
list_final=[10,20,30];
def calgcd_list(list_final):
	n1=list_final.pop();
	#n2=list_final.pop();
	if(list_final==[]):
		return n1;
	else:
		n2=list_final.pop();
		list1=get_common_factors(n1);
		list2=get_common_factors(n2);
		res=get_gcd(list1,list2);
		list_final.append(res);
		#print(list_final);
		return list_final;
while (list_final !=[]):
	res=calgcd_list(list_final);
print("the gcd of give list is--->",res);
	
	
