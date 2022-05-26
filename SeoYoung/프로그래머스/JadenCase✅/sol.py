# 모든 단어의 첫 문자가 대문자, 그 외의 알파벳은 소문자
# 문자열 s가 주어졌을 때, s를 jadencase로 바꾼 문자열을 리턴하는 함수를 완성
# 웨.. 런타임 에러..?
# def solution(s):
#     answer = []
#     for word in s.split(' '):
#         answer.append(word[0].upper()+word[1:].lower())
#     return ' '.join(answer)

def solution(s):
    answer=''
    for w in s.split(' '):
        w=w.lower()
        w=w.capitalize()
        answer+=w+' '
    return answer[:-1]