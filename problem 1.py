prime_no = []
sum = 0
prime_sum = []
l1 = []
for i in range(1000):
    if i > 1:
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            prime_no.append(i)
print(prime_no)
for k in prime_no:
    sum += k
    l1.append(k)
    if sum < 1000 and sum in prime_no:
        prime_sum.append(sum)
print(prime_sum[-1])
print(prime_sum)
print(l1)