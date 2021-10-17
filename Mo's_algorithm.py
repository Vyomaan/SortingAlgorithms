
def printQuerySum(arr,Q):
	
	for q in Q:
		L,R = q 
		s = 0
		for i in range(L,R+1):
			s += arr[i]
			
		print("Sum of",q,"is",s)

arr = [1, 1, 2, 1, 3, 4, 5, 2, 8]
Q = [[0, 4], [1, 3], [2, 4]]
printQuerySum(arr,Q)
