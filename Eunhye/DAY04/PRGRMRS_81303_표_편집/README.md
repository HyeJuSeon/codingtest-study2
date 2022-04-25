## 풀이

## 코드

```python
def solution(n, k, cmds):
    class Node:
        def __init__(self, idx, up, down) -> None:
            self.idx = idx
            self.up = up
            self.down = down
            self.state = "O"

    def u(k, x):
        for _ in range(x):
            k = table[k].up
        return k
    def d(k, x):
        for _ in range(x):
            k = table[k].down
        return k
    def c(k, x):
        pick = table[k]
        trash.append(pick)
        pick.state = "X"
        if pick.up != None: table[pick.up].down = pick.down
        if pick.down != None: table[pick.down].up = pick.up
        return pick.down if pick.down != None else pick.up
    def z(k, x):
        pick = trash.pop()
        pick.state = "O"
        if pick.up != None: table[pick.up].down = pick.idx
        if pick.down != None: table[pick.down].up = pick.idx
        return k

    switch = {
                "U" : u,
                "D" : d,
                "C" : c,
                "Z" : z,
            }

    table = [Node(i, i-1, i+1) for i in range(n)]
    table[0].up = None
    table[n-1].down = None

    trash = []

    for cmd in cmds:
        k = switch[cmd[0]](k, int(cmd[2:]) if cmd[2:] else 0)

    return "".join([cell.state for cell in table])
```
