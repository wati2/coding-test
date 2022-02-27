# N
# 00h 00m 00s
# Nh 59m 59s
# if 3 included counter ++

h = int(input())

count = 0

for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count +=1

print(count)