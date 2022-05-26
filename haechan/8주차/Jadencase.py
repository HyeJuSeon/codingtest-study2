def solution(s):
    s = s.lower()
    if s[0] != " ":
        s = s[0].upper() + s[1:]

    for i, string in enumerate(s):
        try:
            if string == " ":
                s = s[:i+1] + s[i+1].upper() + s[i+2:]
        except: # 문자열 맨 뒤에 공백이 붙는 경우, 인덱스 범위가 넘어갈 수 있는데, 무시한다
            pass
    return s