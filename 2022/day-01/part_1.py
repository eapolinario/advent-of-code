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

    summed_elves = list(map(sum, elves))
    summed_elves.sort(reverse=True)
    print(summed_elves[0] + summed_elves[1] + summed_elves[2])

if __name__ == '__main__':
    raise SystemExit(main())
