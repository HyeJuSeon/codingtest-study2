import sys

def solve():
    n = int(sys.stdin.readline())
    m = 0 # 스택에 마지막으로 들어간 수
    s = []
    ans = ""
    while n:
        x = int(sys.stdin.readline())
        if x > m:
            while x > m:
                m += 1
                s.append(m)
                ans += '+'
            s.pop()
            ans += '-'
        else:
            found = False
            if s:
                top = s[-1]
                s.pop()
                ans += '-'
                if top == x:
                    found = True
            if not found:
                print("NO")
                return
        n -= 1
    for ch in ans:
        print(ch)
solve()

