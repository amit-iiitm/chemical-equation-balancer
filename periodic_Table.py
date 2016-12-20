import periodictable as pt
import re
import collections
import numpy as np

#ls include the elements in periodic table
valid_ele=pt.elements
ls=[]
for i in range(1,109):
	ls.append(str(valid_ele[i]))
#print type(ls)

print ls

input_eq= raw_input()

lhs=input_eq.split('->')[0]
rhs=input_eq.split('->')[1]

# print lhs
# print rhs

reac_list=[]
prod_list=[]
for element in lhs.split('+'):
	reac={}
	temp=""
	for j in range(len(element)):
		char=""
		char+=element[j]
		#print "char here is " + char
		#print "lenghth is " + str(len(element))
		#print j
		if (j+1<len(element) and re.match(r'[a-z]',element[j+1])):
			char+=element[j+1]
			j=j+1
			
		#print char
		#print type(char)
		#print type(ls[0])
		if char in ls:
			reac[char]=1
			# if char in reac.keys():
			# 	reac[char]=1+reac[char]
			# else:
			# 	reac[char]=1
			temp=char
		if(re.match('[0-9]',element[j])):
			reac[temp]=int(element[j])

	print reac
	reac_list.append(reac)
	

for element in rhs.split('+'):
	
	prod={}
	temp=""
	for j in range(len(element)):
		char=""
		char+=element[j]
		#print "char here is " + char
		#print "lenghth is " + str(len(element))
		#print j
		if (j+1<len(element) and re.match(r'[a-z]',element[j+1])):
			char+=element[j+1]
			j=j+1
			
		#print char
		#print type(char)
		#print type(ls[0])
		if char in ls:
			prod[char]=1
			# if char in prod.keys():
			# 	prod[char]=1+prod[char]
			# else:
			# 	prod[char]=1
			temp=char
		if(re.match('[0-9]',element[j])):
			prod[temp]=int(element[j])

	print prod
	prod_list.append(prod)

no_ele=1
for r in reac_list:
	print r.values()
	for val in r.values():
		no_ele*=val
for p in prod_list:
	print
	for val in p.values():
		no_ele*=val

print no_ele



unique_ele=set()
for r in reac_list:
	for key in r.keys():
		unique_ele.add(key)
print unique_ele




#unique_ele=set(unique_ele)
for r in reac_list:
	for key in unique_ele:
		if key in r.keys():
			print "key is already present"
		else:
			r[key]=0

for p in prod_list:
	for key in unique_ele:
		if key in p.keys():
			print "key is already present"
		else:
			p[key]=0

print reac_list
print prod_list


final_a_inp=[]


for r in reac_list:
	r_sorted = collections.OrderedDict(sorted(r.items()))
	print r_sorted.items()
	print r_sorted.values()
	final_a_inp.append(r_sorted.values())

print final_a_inp

for r in prod_list:
	r_sorted = collections.OrderedDict(sorted(r.items()))
	print r_sorted.items()
	val_arr= r_sorted.values()
	new_val_arr=[]
	for val in val_arr:
		val=0-val
		print val
		new_val_arr.append(val)
	final_a_inp.append(new_val_arr)
	
	

"""
coeff_array=[]
for i in range(len(final_a_inp)+1):
	coeff_array.append(0)
coeff_array[0]=1

final_a_inp.append(coeff_array)
"""
#print final_a_inp
final_a_inp=map(list, zip(*final_a_inp))

#print final_a_inp
num_rows= len(final_a_inp)
num_cols=len(final_a_inp[0])
print num_rows, num_cols
if num_cols>num_rows:
	coeff_array=[]
	for i in range(len(final_a_inp)+1):
		coeff_array.append(0)
	coeff_array[0]=1

	final_a_inp.append(coeff_array)
#i am here




	

final_b_inp=[]
for i in range(len(final_a_inp)-1):
	final_b_inp.append(0)
final_b_inp.append(no_ele)


print final_a_inp
print final_b_inp




#error showing here
a=np.array(final_a_inp)
b=np.array(final_b_inp)
res=np.linalg.solve(a,b)
print res
print type(res)
for r in res:
	r=int(r)

print res
print type(res)
res=np.ceil(res)
res_list=res.tolist()
"""
for r in res:
	res_list.append(int(r))
"""
print res_list
print type(res_list)


def greatest_common_divisor(_A):
	iterator = 1
	factor = 1
	a_length = len(_A)
	smallest = 99999

	#get the smallest number
	for number in _A: #iterate through array
	  if number < smallest: #if current not the smallest number
		smallest = number #set to highest

	while iterator <= smallest: #iterate from 1 ... smallest number
		for index in range(0, a_length): #loop through array
			if _A[index] % iterator != 0: #if the element is not equally divisible by 0
		  		break #stop and go to next element
			if index == (a_length - 1): #if we reach the last element of array
		  		factor = iterator #it means that all of them are divisibe by 0
		iterator += 1 #let's increment to check if array divisible by next iterator
	#print the factor
	print factor
	return factor

factor=greatest_common_divisor(res_list)

result_eq=""
result_eq+=str(int(res_list[0]/factor))
ind=1
for ch in input_eq:
	result_eq+=ch
	if ch=='+':
		result_eq+=str(int(res_list[ind]/factor))
		ind+=1
	if ch=='>':
		result_eq+=str(int(res_list[ind]/factor))
		ind+=1
	
	
print result_eq

