import math

def inverse(L , m ,  p , Li , Li2 , n , gray): 
	#L is given list and Li is empty list in which lists would be added
	# requested item ends up at position p in L
	# subset transfer only involves elements after position m in L'
	# n is size of list L
	#Li2 stores gray code for the corresponding list in L1
	Li.append(L);
	gray2 = gray
	Li2.append(gray2)
	L2 = L
	p2 = p
	if(p==n):
		return ;
	else:
		for i in range(p-m):
			child1 = L2
			g = child1[p2]
			h = child1[p2 - 1]
			if(g>h):
				gray2 += math.factorial(child1[p2]-1)
			else:
				gray2 -= math.factorial(child1[p2]-1)
			child1 = swap(L2,p2)
			x = inverse(child1 , p2 , p+1 , Li, Li2 , n, gray2)
			L2 = child1
			p2 = p2-1

def swap(list, pos1):
    list2 = list[:]
    list2[pos1], list2[pos1 - 1] = list2[pos1 - 1], list2[pos1]
    return list2

if(__name__ == '__main__'):
	Li = []
	Li2 = []
	inverse([5,4,3,2,1],0,4,Li,Li2,5,119)    
	print(Li)
	print(Li2)