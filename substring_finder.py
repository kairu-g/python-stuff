def findSub(string, substr):
    pos = -1
    isSub = False
    if len(string) >= len(substr):
        for i in range(len(string) - 1):
            if string[i] == substr[0]:
                for j in range(0, len(substr) - 1):
                    if len(string) - 1 < len(substr) or string[i + j] != substr[j]:
                        isSub = False
                        break
                    else:
                        pos = i
                        isSub = True
        if isSub == True:
            return pos
        else:
            return -2



string1 = input('Write a string: ')
string2 = input('Write your substring: ')
position = findSub(string1, string2)
if position > 0:
    print('Substring found at index position ' + str(position) + '.')
else:
    print('Substring was not found.')
