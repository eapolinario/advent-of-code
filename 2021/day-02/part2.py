import sys
def read_input():
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip())

    return lines

def main():
    depth = 0
    pos = 0
    aim = 0
    for line in read_input():
        dir, unit = line.split(' ')
        unit = int(unit)
        if dir == 'forward':
            pos += unit
            depth += aim * unit
        elif dir == 'up':
            # depth -= unit
            aim -= unit
        elif dir == 'down':
            # depth += unit
            aim += unit
        else:
            raise Exception('not supposed to happen')

    print(f'multiplication is {pos * depth}')



if __name__ == '__main__':
    main()
