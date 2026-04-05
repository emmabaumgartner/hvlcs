#Opt(i, j) = { 
#0						if i = 0 / if no matches
#	opt(n-1, m-1) + vA[i]				if Ai = Bj
# max(opt[i-1][j] + vA[i], opt[i][j-1] + vA[j])	if Ai != Bj / otherwise

def hvlcs(A, B, vA, vB):
    n = len(A)
    m = len(B)
    # opt array
    opt = [[]]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                opt[i][j] = opt[i - 1][j - 1] + vA[i - 1]
            else:
                opt[i][j] = max(opt[i - 1][j] + vA[i - 1], opt[i][j - 1] + vB[j - 1])
    return opt[n][m]

def backtracking(A, B, vA, vB, opt):
    return 0

if __name__ == "__main__":
    print("Hello World")
