f = open('input.txt', 'r')

left = []
right = []

for line in f:
    parts = line.split()
    if len(parts) >= 2:
        left.append(int(parts[0]))
        right.append(int(parts[1]))

left.sort()
right.sort()
lenght = 0

arrayLen = len(right)

for i in range (arrayLen):
     lenght += abs(right[i]-left[i])

print(f"Distance {lenght}")


similarity = 0

checked = []
for i in range(arrayLen):
    score = 0
    if left[i] not in checked:
        print(left[i])
        for j in range(arrayLen):
            if(left[i]==right[j]):
                score +=1
    similarity += score * left[i]
    checked.append(left[i])

print(f"Smiliarity {similarity}")
