r=1/4
tol = 0.001
lim = 1/(1-r)
i=0
sum = 0

while(lim-sum > tol):
    sum += r**i
    i+=1

dif = lim-sum
print("Sum:", sum)
print("Antall iterasjoner:", i)
print("Differanse:", dif)