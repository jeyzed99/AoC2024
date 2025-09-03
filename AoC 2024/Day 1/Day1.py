input = open("Day1Input.txt", "r")

output = input.readline()
leftList = []
rightList = []



while output:
    leftList.append(int(output[0:5]))
    rightList.append(int(output[8:14]))
    output = input.readline()

input.close()

leftList.sort()
rightList.sort()

distance = []

for i in range(0,1000):
    distance.append(abs(leftList[i]-rightList[i]))

sum = 0

for i in distance:
    sum += i

#part 2
similarity = 0

for i in range(0,1000):
    for j in range(0,1000):
        if leftList[i] == rightList[j]:
            similarity+= leftList[i]

print(similarity)