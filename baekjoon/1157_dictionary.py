""" 
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된
알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를
구분하지 않는다.

여러개인 경우 ?
"""

testWord = input().lower()

a_to_z = list(map(chr,range(ord('a'),ord('z')+1)))

myDictionary = dict.fromkeys(a_to_z,0)

for oneChar in testWord:
    myDictionary[oneChar] += 1

max_key = max(myDictionary, key=myDictionary.get)
max_value = max(myDictionary.values())

count = 0
for key,value in myDictionary.items():
    if value == max_value:
        count += 1
    if count >= 2:
        break

if count == 2:
    print("?")
else:
    print(max_key.upper())