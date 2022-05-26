# n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
# n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
# n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
def solution(n):
    answer = 0

    def toBinary(n):
        binary = ''
        while n > 0:
            n, mod = divmod(n, 2)
            binary += str(mod)
        return binary[::-1]

    count_one = toBinary(n).count('1')

    while True:
        n += 1
        if toBinary(n).count('1') == count_one:
            answer = n
            break

    return answer

print(solution(15))