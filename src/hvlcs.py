#Opt(i, j) = { 
#0						if i = 0 / if no matches
#	opt(n-1, m-1) + vA[i]				if Ai = Bj
# max(opt[i-1][j] + vA[i], opt[i][j-1] + vA[j])	if Ai != Bj / otherwise

def hvlcs(A, B, vA):
    n = len(A)
    m = len(B)

    opt = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if A[i] == B[j]:
                opt[i][j] = opt[i + 1][j + 1] + vA[A[i]]
            else:
                opt[i][j] = max(
                    opt[i + 1][j],
                    opt[i][j + 1]
                )

    return opt, opt[0][0]

def backtracking(A, B, opt):
    i = 0
    j = 0
    n = len(A)
    m = len(B)
    sol_array = []
    while i < n and j < m:
        if A[i] == B[j]:
            sol_array.append(A[i])
            i += 1
            j += 1
        elif opt[i + 1][j] >= opt[i][j + 1]:
            i += 1
        else:
            j += 1
    return sol_array

if __name__ == "__main__":
    letter_value_dict = {}

    alphabet = int(input("Input number of characters in alphabet: "))
    for i in range(alphabet):
        letter_value = list(map(str, input().split()))

        letter_value[0] = letter_value[0].lower()
        letter_value[1] = int(letter_value[1])
        letter_value_dict[letter_value[0]] = letter_value[1]


    A = input("Input string A: ")
    B = input("Input string B: ")

    opt_array, opt_value = hvlcs(A, B, letter_value_dict)
    print(opt_value)
    sol_array = backtracking(A, B, opt_array)
    print(sol_array)
    