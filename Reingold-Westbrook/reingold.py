import inverse_subset_transfer
import trotter
import math

def move(arr1, arr2):
	#arr1 to arr2 conversion
  	k = 0
  	for i in range(len(arr1)):
  		x = arr2[i]
  		index = arr1.index(x)
  		arr1.remove(x)
  		arr1.insert(i,x)
  		k+=index-i
  	return k

def offline(L , requests):
	n = len(L)
	m = len(requests)
	Li,Li2 = [],[]
	all_permutations, inversion_vector = trotter.printPermutation(n, Li, Li2)
	DYN = [None]*(m+1)
	for i in range(m+1):
		DYN[i] = [None]*math.factorial(n)
	for i in range(math.factorial(n)):
		temp = all_permutations[i][:]
		temp2 = L[:]
		DYN[0][i] = move(temp,temp2)
	for i in range(1,m+1):
		for j in range(math.factorial(n)):
			temp_list = all_permutations[j][:]
			r = requests[i-1]
			subset_inverse_list = []
			gray_inverse = []
			inverse_subset_transfer.inverse(temp_list, 0 , temp_list.index(r)+1 , subset_inverse_list , gray_inverse , n , j)
			
			store = [None]*len(gray_inverse)
			for k in range(len(gray_inverse)):
				store[k] = DYN[i-1][gray_inverse[k]] + subset_inverse_list[k][:].index(r)+1 + move(temp_list[:],subset_inverse_list[k][:])
			x = min(store)
			DYN[i][j]=x	
	return min(DYN[m])		

print(offline([1,2,3],[3,2,2,3]))

