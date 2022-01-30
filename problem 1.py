prime_no = []
sum = 0
prime_sum = []
for i in range(100):
    if i > 1:
        for j in range(2,i//2):
            if i%j == 0:
                break
        else:
            prime_no.append(i)
print(prime_no)
for k in prime_no:
    sum += k
    if sum < 100 and sum in prime_no:
        prime_sum.append(sum)


print(prime_sum)

