a, b = input().split()
a = int(b)
col, row = 2*a+3, a+2
def one(a):
    global text
    for i in range(col):
        if i in (0, s+1, col-1):
            text[i] += ' '*row
        else:
            text[i] += ' ' * (row-1) + '|'
    return text

def two(a):
    global text
    for i in range(col):
        if i in (0, s+1, col-1):
            text[i] += ' ' + '-'*s + ' '
        else:
            if i < s+1:
                text[i] += ' ' * (row-1) + '|'
            else:
                text[i] += '|' + ' ' * (row-1)
    return text

def three(a):
    global text
    for i in range(col):
        if i in (0, s+1, col-1):
            text[i] += ' ' + '-'*s + ' '
        else:
            text[i] += ' ' * (row-1) + '|'
    return text

def four(a):
    global text
    for i in range(col):
        if i in (0, col-1):
            text[i] += ' '*row
        elif i == s+1:
            text[i] += ' ' + '-'*s + ' '
        else:
            if i < s+1:
                text[i] += '|' + ' ' * s + '|'
            else:
                text[i] += ' ' * (row-1) + '|'
    return text

def five(a):
    global text
    for i in range(col):
        if i in (0, s+1, col-1):
            text[i] += ' ' + '-'*s + ' '
        else:
            if i < s+1:
                text[i] += '|' + ' ' * (row-1)
            else:
                text[i] += ' ' * (row-1) + '|'
    return text

def six(a):
    global text
    for i in range(col):
        if i in (0, s+1, col-1):
            text[i] += ' ' + '-'*s + ' '
        else:
            if i < s+1:
                text[i] += '|' + ' ' * (row-1)
            else:
                text[i] += '|' + ' ' * s + '|'
    return text

def seven(a):
    global text
    for i in range(col):
        if i == 0:
            text[i] += ' ' + '-'*s + ' '
        elif i in (s+1, col-1):
            text[i] += ' '*row
        else:
            text[i] += ' ' * (row-1) + '|'
    return text

def eight(a):
    global text
    for i in range(col):
        if i in (0, s+1, col-1):
            text[i] += ' ' + '-'*s + ' '
        else:
            text[i] += '|' + ' ' * s + '|'
    return text

def nine(a):
    global text
    for i in range(col):
        if i in (0, s+1, col-1):
            text[i] += ' ' + '-'*s + ' '
        else:
            if i < s+1:
                text[i] += '|' + ' ' * s + '|'
            else:
                text[i] += ' ' * (row-1) + '|'
    return text

def zero(a):
    global text
    for i in range(col):
        if i in (0, col-1):
            text[i] += ' ' + '-'*a + ' '
        elif i == a+1:
            text[i] += ' '*row
        else:
            text[i] += '|' + ' ' * a + '|'
    return text

text = [''] * col
func_dict = {
    '0': zero,
    '1': one,
    '2': two,
    '3': three,
    '4': four,
    '5': five,
    '6': six,
    '7': seven,
    '8': eight,
    '9': nine
}
def run(number):
    func_dict[number](a)
    for i in range(col):
        text[i] += ' '

for i in b:
    run(i)

for i in text:
    print(i)