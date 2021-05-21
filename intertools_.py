import itertools




numbers= [0, 1, 2,3, 5,6,7,8,9]





def lt_3(n):
	if n>3:
		return False
	return True


result_w_def=filter(lt_3,numbers)

for item in result_w_def:
	print(item)


letters = ['a', 'b','c','d']

names=['Corey', 'Nicole']


selector=[True, False, False, True]


select_result= itertools.compress(letters,selector)

for item in select_result:
	print(item)


# all thoses function of itertools must be used with for loop


result = itertools.combinations(letters,3)
all_result= itertools.permutations(letters,3)
all_results_repeat=itertools.product(numbers,repeat=4)
all_r=itertools.combinations_with_replacement(numbers,4)


combined=itertools.chain(letters, names)


r_result = itertools.islice(range(10),1,5)
r_result_step2= itertools.islice(range(10),1,5,2)


for item in combined :
	print(item)

#print(itertools.__dict__)


#for item in r_result_step2:
	#print(item)


#print(line)





acc_result=itertools.accumulate(numbers)# for loop to see result





