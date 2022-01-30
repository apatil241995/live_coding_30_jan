

# example 2

def demo(nums, groups):
    sz = len(nums)
    l1 = []
    count = 0
    l2 = []
    for i in range(sz + 1):
        for j in range(i):
            for k in range(len(groups)):
                if nums[j:i] == groups[k]:
                    l1.append(nums[j:i])
    if len(l1) == len(groups):
        for l in range(len(l1)):
            for j in range(len(l1[l])):
                if l1[l][j] in l1[l+1]:
                    return "False"
            break
    if l1 == groups:
        for m in range(len(l1)):
            if l1[m] == groups[m]:
                count += 1
        if count == len(l1):
            return "True"
        else:
            return "False"
    else:
        for m in range(len(l1)):
            if l1[m] == groups[m]:
                continue
            else:
                l2.insert(m,groups[m])

    for m in range(len(l1)):
        if l2[m] == groups[m]:
            count += 1
    if count == len(l1):
        return "True"
    else:
        return "False"



# example 1
a1 = [1,-1,0,1,-1,-1,3,-2,0]
b1 = [[1,-1,-1],[3,-2,0]]
# example 2
a2 = [1,2,3,4,10,-2]
b2 = [[10,-2],[1,2,3,4]]
# example 3
a3 = [7,7,1,2,3,4,7,7]
b3 = [[1,2,3],[3,4]]

print(demo(a1, b1))
print(demo(a2, b2))
print(demo(a3, b3))
