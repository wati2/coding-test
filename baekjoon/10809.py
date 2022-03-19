# 알파벳 소문자로만 이루어진 단어 S
# 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는
# a ~ z 를 의미함

# 처음에 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는
# 프로그램을 작성하시오

inputWord = list(input())

a_to_z = list(map(chr, range(ord('a'),ord('z')+1)))

result = []
resultAsString =""

for i in a_to_z:
    try:
        result.append(inputWord.index(i))
    except:
        result.append(-1)


for i in result:
    resultAsString += " " + str(i)

print(resultAsString.strip())