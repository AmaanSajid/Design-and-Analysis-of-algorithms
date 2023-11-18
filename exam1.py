# Python program to print topological sorting of a DAG
from collections import defaultdict

# Class to represent a graph


class Graph:
	def __init__(self, vertices):
		self.graph = defaultdict(list) # dictionary containing adjacency List
		self.V = vertices # No. of vertices

	# function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)

	# A recursive function used by topologicalSort
	def topologicalSortUtil(self, v, visited, stack):

		# Mark the current node as visited.
		visited[v] = True

		# Recur for all the vertices adjacent to this vertex
		for i in self.graph[v]:
			if visited[i] == False:
				self.topologicalSortUtil(i, visited, stack)

		# Push current vertex to stack which stores result
		stack.append(v)

	# The function to do Topological Sort. It uses recursive
	# topologicalSortUtil()
	def topologicalSort(self):
		# Mark all the vertices as not visited
		visited = [False]*self.V
		stack = []

		# Call the recursive helper function to store Topological
		# Sort starting from all vertices one by one
		for i in range(self.V):
			if visited[i] == False:
				self.topologicalSortUtil(i, visited, stack)

		# Print contents of the stack
		print(stack[::-1]) # return list in reverse order


# Driver Code
if __name__ == '__main__':
	g = Graph(8)
	#as the topical will calculate all the numbers which in order we need to keep the graph continously 
	
	g.addEdge(3, 7)
	g.addEdge(3, 4)
	g.addEdge(2, 7)
	g.addEdge(1, 4)
	g.addEdge(1, 6)
	g.addEdge(7, 0)
	g.addEdge(7, 5)
	g.addEdge(7, 6)
	g.addEdge(4, 5)

	print("Following is a Topological Sort of the given graph")
	g.topologicalSort()
    A=g.topologicalSort()
for i in range(100):
    if A[i]==0:
        A[i]=2
    elif A[i]==1:
        A[i]=3
    elif A[i]==2:
        A[i]=5
    elif A[i]==3:
        A[i]=7
    elif A[i]==4:
        A[i]=8
    elif A[i]==5:
        A[i]=9
    elif A[i]==6:
        A[i]=10
    else:
        A[i]=11
    
