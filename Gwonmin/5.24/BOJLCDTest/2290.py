s,n = input().split()
s = int(s)
result = []

for i in range(len(n)):
    number = []
    if n[i] == '1':
        for j in range(2*s+3):
            row = []
            if j%(s+1) == 0:
                row.append(' '*(s+2))
            else:
                row.append(' '*(s+1) + 'ㅣ')
            number.append(row)

    elif n[i] == '2':
        for j in range(2*s+3):
            row = []
            if j%(s+1) == 0:
                row.append(' '+'-'*s+' ')
            elif j < (s+1) :
                row.append(' '*(s+1) + 'ㅣ')
            else:
                row.append('ㅣ' + ' '*(s+1))
            number.append(row)

    elif n[i] == '3':
        for j in range(2*s+3):
            row = []
            if j%(s+1) == 0:
                row.append(' '+'-'*s+' ')
            else:
                row.append(' '*(s+1) + 'ㅣ')
            number.append(row)

    elif n[i] == '4':
        for j in range(2*s+3):
            row = []
            if j%(2*s+2) == 0:
                row.append(' '*(s+2))
            elif j < (s+1) :
                row.append('ㅣ'+' '*s+ 'ㅣ')
            elif j%(s+1) == 0:
                row.append(' '+'-'*s+' ')
            else:
                row.append(' '*(s+1) + 'ㅣ')
            number.append(row)

    elif n[i] == '5':
        for j in range(2*s+3):
            row = []
            if j%(s+1) == 0:
                row.append(' '+'-'*s+' ')
            elif j < (s+1) :
                row.append('ㅣ'+' '*(s+1))
            else:
                row.append(' '*(s+1) + 'ㅣ')
            number.append(row)

    elif n[i] == '6':
        for j in range(2*s+3):
            row = []
            if j%(s+1) == 0:
                row.append(' '+'-'*s+' ')
            elif j < (s+1) :
                row.append('ㅣ'+' '*(s+1))
            else:
                row.append('ㅣ'+' '*s+ 'ㅣ')
            number.append(row)

    elif n[i] == '7':
        for j in range(2*s+3):
            row = []

            if j == 0:
                row.append(' '+'-'*s+' ')
            elif j%(s+1) == 0:
                row.append(' '*(s+2))
            else:
                row.append(' '*(s+1) + 'ㅣ')
            number.append(row)

    elif n[i] == '8':
        for j in range(2*s+3):
            row = []
            if j%(s+1) == 0:
                row.append(' '+'-'*s+' ')
            else:
                row.append('ㅣ'+' '*s+ 'ㅣ')
            number.append(row)

    elif n[i] == '9':
        for j in range(2*s+3):
            row = []
            if j%(s+1) == 0:
                row.append(' '+'-'*s+' ')
            elif j < (s+1) :
                row.append('ㅣ'+' '*s+'ㅣ')
            else:
                row.append(' '*(s+1)+ 'ㅣ')
            number.append(row)

    elif n[i] == '0':
        for j in range(2*s+3):
            row = []
            if j == (s+1):
                row.append(' '*(s+2))
            elif j%(s+1) == 0:
                row.append(' '+'-'*s+' ')
            else:
                row.append('ㅣ'+' '*s+'ㅣ')
            number.append(row)

    if i != len(n)-1:
        for j in range(2*s+3):
            row = []
            row.append(' ')
            number.append(row)

    result.append(number)


for i in range(len(result)):
    for j in range(len(result[i])):
        print(' '.join(result[i][j]))