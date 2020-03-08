def sockMerchant(n, ar):
    track = set()
    count = 0
    for each in ar:
        if each in track:
            count += 1
            track -= {each}
        else:
            track |= {each}

    return count


test_string = "UDDDUDUU"


def countingValleys(n, s):
    valleys = 0
    open_valley = False
    elevation = 0
    for c in s:
        if c == "U":
            elevation += 1
            if elevation == 0 and open_valley:
                valleys += 1
                open_valley = False
        elif c == "D":
            if elevation == 0:
                open_valley = True
            elevation -= 1
        else:
            continue

        print(c, elevation, valleys)

    return valleys

countingValleys(0, test_string)



seq = [0, 0, 0, 1, 0, 0]

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):

    jumps = 0
    position = None
    if len(c) == 0:
        return
    if not c[0]:
        position = 0
    else:
        position = 1

    while position < len(c):

        cursor = position + 2
        if cursor < len(c) and not c[cursor]:
            position += 2
            jumps += 1
        elif cursor-1 < len(c):
            position += 1
            jumps += 1
        else:
            break

        print(position, cursor, jumps)

    return jumps

print(jumpingOnClouds(seq))
