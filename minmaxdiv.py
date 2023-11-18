
from array import array


class pair:
	def __init__(self):
		self.min = 0
		self.max = 0

def getMinMax(arr: list, n: int) -> pair:
	minmax = pair()

	# If there is only one element then return it as min and max both
	if n == 1:
		minmax.max = arr[0]
		minmax.min = arr[0]
		return minmax

	# If there are more than one elements, then initialize min
	# and max
	if arr[0] > arr[1]:
		minmax.max = arr[0]
		minmax.min = arr[1]
	else:
		minmax.max = arr[1]
		minmax.min = arr[0]

	for i in range(2, n):
		if arr[i] > minmax.max:
			minmax.max = arr[i]
		elif arr[i] < minmax.min:
			minmax.min = arr[i]

	return minmax

if __name__ == "__main__":
	arr = []
  
# number of elements as input
n = int(input("Enter number of elements : "))
  
# iterating till the range
for i in range(0, n):
    ele = int(input("input the numbers in list"))
    arr.append(ele)
minmax = getMinMax(arr, n)
print("Minimum element is", minmax.min)
print("Maximum element is", minmax.max)	


