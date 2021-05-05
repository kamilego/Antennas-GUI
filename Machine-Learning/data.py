with open(r"C:\Users\Proj-North\Desktop\OLD\data.txt") as t:
    r = t.readlines()

try:
    for num in range(0,len(r)-1,2):
    	r.pop(num)
except IndexError:
    print("sorry -- can't pop that")

r = [elem.replace("\n", "") for elem in r]


r2 = [r[i].split(",") for i in range(0,len(r),2)]
r1 = [elem[0] for elem in r2]
for elem in r2:
    del elem[0]

r3 = [r[i].split(",") for i in range(1,len(r),2)]
for elem in r3:
    del elem[0]

z = zip(r2,r3)
z = list(z)
c= []
for elem in z:
    c.append(list(zip(elem[0],elem[1])))

result = []

for elem in c:
	result.append(list(map(list, elem)))

for num, elem in enumerate(result):
	for line in elem:
		line.insert(0,r1[num])

# result.extend()

result = sum(result, [])
for elem in result:
    print(elem)

print(result)
print(len(result))
