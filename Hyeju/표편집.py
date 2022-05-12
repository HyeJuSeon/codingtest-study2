def solution(n, k, cmd):
    table = {i:[i - 1, i + 1] for i in range(n)}
    table[0] = [None, 1]
    table[n - 1] = [n - 2, None]
    stack = []
    curr = k
    ans = ['O'] * n
    for c in cmd:
        if c[0] == 'U':
            _, x = c.split()
            for _ in range(int(x)):
                curr = table[curr][0]
        elif c[0] == 'D':
            _, x = c.split()
            for _ in range(int(x)):
                curr = table[curr][1]
        elif c[0] == 'C':
            ans[curr] = 'X'
            prev, next = table[curr]
            stack.append([prev, curr, next])
            if next == None:
                curr = table[curr][0]
            else:
                curr = table[curr][1]
            if next == None:
                table[prev][1] = None
            elif prev == None:
                table[next][0] = None
            else:
                table[prev][1] = next
                table[next][0] = prev
        elif c[0] == 'Z':
            prev, i, next = stack.pop()
            ans[i] = 'O'
            if next == None:
                table[prev][1] = i
            elif prev == None:
                table[next][0] = i
            else:
                table[prev][1] = i
                table[next][0] = i
    return ''.join(ans)

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
