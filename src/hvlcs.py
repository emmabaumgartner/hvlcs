#Opt(i, j) = { 
#0						if i = 0 / if no matches
#	opt(n-1, m-1) + vA[i]				if Ai = Bj
# max(opt[i-1][j] + vA[i], opt[i][j-1] + vA[j])	if Ai != Bj / otherwise

def hvlcs(A, B, vA):
    value_set = sorted(set(A) & set(B))

    value_dict = {}
    for i in range(len(value_set)):
        value_dict[value_set[i]] = vA[i]

    n = len(A)
    m = len(B)

    opt = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if A[i] == B[j]:
                opt[i][j] = opt[i + 1][j + 1] + value_dict[A[i]]
            else:
                opt[i][j] = max(
                    opt[i + 1][j],
                    opt[i][j + 1]
                )

    return opt[0][0]

# def backtracking(A, B, vA, vB, opt):

#     return 0

if __name__ == "__main__":
    A = "aacb"
    B = "caab"
    vA = [2, 4, 5]

    # letter_value_dict = {}

    # alphabet = int(input("Input number of characters in alphabet: "))
    # for i in range(alphabet):
    #     letter_value = list(map(str, input().split()))

    #     letter_value[0] = letter_value[0].lower()
    #     letter_value[1] = int(letter_value[1])
    #     letter_value_dict[letter_value[0]] = letter_value[1]

    # vA=letter_value_dict


    # A = input("Input string A: ")
    # B = input("Input string B: ")

    print(hvlcs(A, B, vA))


    # for i in range(len(value_set)):
    #     value_dict[value_set[i]] = vA[i]

    # n = len(A)
    # m = len(B)
    # # opt array
    # opt = [[0 for _ in range(m)] for _ in range(n)]
    # for i in range(1, n):
    #     for j in range(1, m):
    #         if A[i] == B[j]:
    #             if j < m and i < n:
    #                 opt[i][j] = opt[i + 1][j + 1] + value_dict[A[i]]
    #             else:
    #                 opt[i][j] = opt[i][j] + value_dict[A[i]]
    #         else:
    #             if j < m and i < n:
    #                 opt[i][j] = max(opt[i + 1][j] + value_dict[A[i]], opt[i][j + 1] + value_dict[B[j]])
    #             else:                    
    #                 opt[i][j] = max(opt[i][j] + value_dict[A[i]], opt[i][j] + value_dict[B[j]])
