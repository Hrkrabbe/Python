k = 10
fib = [0,1]
sum = 0

for i in range(2,k):
    fib.append(fib[i-1] + fib[i-2])
    
for i in fib:
    sum+=i
    
print(fib[0:k+1])
print("Sum:",sum)