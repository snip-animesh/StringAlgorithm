# All permutations for a given string . all characters must be distinct .
# Logic from --> https://www.youtube.com/watch?v=4lIQCoG4MnY

def permutation(word):
    if len(word)==1:
        return [word]
    perms=permutation(word[1:])
    result=[]
    char=word[0]
    # print(perms)
    for perm in perms:
        for i in range(len(perm)+1):
            result.append(perm[:i]+char+perm[i:])
    return result


result=permutation("aabc")
print(result)
