def add(N, number):
    N |= (1 << number)
    return N

def remove(N, number):
    N &= ~(1 << number)
    return N

def toggle(N, number):
    N ^= (1 << number)
    return N

def check(N, number):
    check = N & (1 << number)
    return 1 if check else 0

def all():
    return 2097150

def empty():
    return 0

if __name__ == "__main__":
    N = int(input())
    S = 0

    while True:
        if N == 0:
            break
        N -= 1
        cmd, num = '', 0
        command = input().split()

        if len(command) == 2:
            cmd, num = command[0], int(command[1])
        else:
            cmd = command[0]

        if cmd == "add":
            S = add(S, num)
        elif cmd == "remove":
            S = remove(S, num)
        elif cmd == "toggle":
            S = toggle(S, num)
        elif cmd == "all":
            S = all()
        elif cmd == "empty":
            S = empty()
        elif cmd == "check":
            print(check(S, num))

