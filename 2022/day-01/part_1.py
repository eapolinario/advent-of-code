import sys

def main():
    lines = []
    elves = []
    calories = []
    for line in sys.stdin:
        line = line.rstrip()
        if line:
            calories.append(int(line))
        else:
            elves.append(calories)
            calories = []
    elves.append(calories)

    print(max(map(sum, elves)))

if __name__ == '__main__':
    raise SystemExit(main())
