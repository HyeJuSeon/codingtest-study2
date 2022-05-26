def solution(s):
    bool = False
    for i in range(len(s)):
        if bool == False:
            s = s[:i]+s[i].upper()+s[i+1:]
        elif bool:
            s = s[:i]+s[i].lower()+s[i+1:]

        if s[i].isalpha() or s[i].isnumeric():
            bool = True
        elif s[i].isalpha() == False:
            bool = False
    return s

s = "for the last week"
print(solution(s))