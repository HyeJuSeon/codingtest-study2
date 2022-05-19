'''프로그래머스 - 수식 최대화

- 분할정복
- 우선순위가 "+" > "-" > "*"인 경우, 가장 우선순위가 낮은 "*"로 split을 하면
  "+", "-"인 값들만 남게 되고, 다시 다음으로 우선순위가 낮은 "-"로 split을 해서
  "+"인 값들만 남긴다.
- 우선순위가 높은 "+" 값들을 계산한 뒤, 재귀를 타고 올라오면서 다음 우선순위인 값들을
  계산하며 올라오고, 최종 값을 리턴한다.
- python eval 메서드 => eval("1+2") = 3, 문자열로 식을 받아 연산 후 숫자로 출력

'''

from itertools import permutations

def get_priorities(expression):
    opers = set() # 등장하는 유니크한 연산자
    for e in expression:
        if e in ["+", "-", "*"]:
            opers.add(e)

    return set(permutations(opers, len(opers)))

def calc(priority, n, expression):
    if n == len(priority): # 연산자 수만큼 쪼개면 남는 수끼리의 연산만 해주면 된다
        return str(eval(expression))
    if priority[n] == '*':
        res = eval('*'.join([calc(priority, n+1, e) for e in expression.split('*')]))
    if priority[n] == '+':
        res = eval('+'.join([calc(priority, n+1, e) for e in expression.split('+')]))
    if priority[n] == '-':
        res = eval('-'.join([calc(priority, n+1, e) for e in expression.split('-')]))
    return str(res)


def solution(expression):
    answer = 0
    priorities = get_priorities(expression,)
    for priority in priorities:
        res = int(calc(priority, 0, expression)) # 반대로 뒤집힌 경우도 들어가 있으니까 인덱스 0부터
        answer = max(answer, abs(res))

    return answer