import random
k = [random.randint(-100, 100) for x in range(30)]
biggest = max(k)
r.index(biggest)
print(k)
print(biggest)
print(k.index(biggest)+1)
for i in range(29):
  if k[i]<0 and k[i+1]<0:
    print(k[i],k[i+1])