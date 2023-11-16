
def permute(lst):
    if len(lst)==1:
        return [lst]
    perm = []
    for i in range(len(lst)):
        for per in permute(lst[:i]+lst[(i+1):]):
            perm.append([lst[i]]+per)
    return perm

print(permute([1,2,3,4]))