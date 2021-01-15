
#baaabbacddc

notes = list(input())

i =1

count = 1
while count > 0:
    count = 0
    for i in range(1,len(notes)):
        if notes[i-1] == notes[i]:
            notes.pop(i-1)
            notes.pop(i-1)
            count+=1
            break

str = ''
print(str.join(notes))