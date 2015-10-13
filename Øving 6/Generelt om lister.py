__author__ = 'Anders'
li = [1,2,3,4,5,6]
for i,n in enumerate(li):
    li[i] = n*-1
li.sort(reverse=True)
print(li)