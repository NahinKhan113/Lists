if __name__ == '__main__':
    a = list()
    n = int(input())
    for i in range(0,n):
        command = input().rsplit()
        try:
            if command[0] == 'insert':
                a.insert(int(command[1]),int(command[2]))
            elif command[0] == 'append':
                a.append(int(command[1]))
            elif command[0] == 'remove':
                a.remove(int(command[1]))
            elif command[0] == 'pop':
                a.pop()
            elif command[0] == 'sort':
                a.sort()
            elif command[0] == 'reverse':
                a.reverse()
            elif command[0] == 'print':
                print(a)
            else:
                continue
        except:
            pass
input('press Enter to exit')
