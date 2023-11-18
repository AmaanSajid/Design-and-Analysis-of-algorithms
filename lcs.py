def lcs(v1, v2):
	x = len(v1)
	y = len(v2)
	L = [[None]*(y + 1) for i in range(x + 1)]
	for i in range(x + 1):
		for j in range(y + 1):
			if i == 0 or j == 0 :
				L[i][j] = 0
			elif v1[i-1] == v2[j-1]:
				L[i][j] = L[i-1][j-1]+1
			else:
				L[i][j] = max(L[i-1][j], L[i][j-1])
	return L[x][y]

v1 = "AGGTAB"
v2 = "GXTXAYB"
print("Length of LCS is ", lcs(v1, v2))


