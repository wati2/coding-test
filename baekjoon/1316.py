
def checkGroupWord(word):
    char_list = list(word)
    check_list = []
    continous = False
    saveWord = None

    for oneChar in char_list:
        if saveWord == None:
            saveWord = oneChar
            check_list.append(oneChar)
            continue

        if oneChar == saveWord:
            continous = True
        else: 
            continous = False
            saveWord = oneChar


        if not continous:
            if oneChar in check_list:
                return False
            else:
                check_list.append(oneChar)

    return True

n = int(input())
lis = []
count = 0

for i in range(n):
    lis.append(input())

for i in lis:
    if checkGroupWord(i):
        count += 1

print(count)
