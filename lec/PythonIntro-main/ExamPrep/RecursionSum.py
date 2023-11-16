def recursive_list_sum(data_list):
	total = 0
	for element in data_list:
		if type(element) == type([]):
			total = total + recursive_list_sum(element)
		else:
			total = total + element

	return total

lst = [1, 2, [3, [5, [1,2,6], 4]],[5,6]]
print( recursive_list_sum(lst))

def hanoiTowets(n, A, B, C):
	if n != 0:
		hanoiTowets(n-1, A, C, B) #move n-1 discs from A to C. this leaves disk n alone on A
		print(" Move disk ", n, " from peg ", A, " to peg ", C)  # move disk n from A to C
		hanoiTowets(n-1, C, B, A) #move n-1 discs from C to B so they sit on disk n


hanoiTowets(5, 1, 3, 2)
