from termcolor import colored

target= [(0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (3, 12), (3, 13), (3, 14), (3, 15), (2, 15), (1, 15), (1, 16), (1, 17), (2, 17), (3, 17), (3, 18), (3, 19), (2, 19), (1, 19), (1, 20), (1, 21), (1, 22), (1, 23), (2, 23), (3, 23), (3, 24), (3, 25), (3, 26), (3, 27), (2, 27), (1, 27), (1, 28), (1, 29), (2, 29), (3, 29), (3, 30), (3, 31), (4, 31), (5, 31), (6, 31), (7, 31), (7, 30), (7, 29), (6, 29), (5, 29), (5, 28), (5, 27), (6, 27), (7, 27), (8, 27), (9, 27), (9, 28), (9, 29), (9, 30), (9, 31), (10, 31), (11, 31), (12, 31), (13, 31), (13, 32), (13, 33), (14, 33), (15, 33), (15, 34), (15, 35), (14, 35), (13, 35), (13, 36), (13, 37), (12, 37), (11, 37), (11, 38), (11, 39), (12, 39), (13, 39), (14, 39), (15, 39), (15, 38), (15, 37), (16, 37), (17, 37), (17, 38), (17, 39), (18, 39), (19, 39), (20, 39)]

def colorize(s: str):

    # print characters that match the target in green, else in red
    # only used to help with visualizing the effects of the algorithm over time
    for i in range(len(s)):
        if s[i] == target[i]:
            print(colored(s[i], "green"), end="")
        else:
            print(colored(s[i], "red"), end="")


# gen = current generation number, phr = string to print, fit = string's fitness
def summarize(gen: int, phr: str, fit: float) -> None:

    # cleanly summarizes the data of the "best we've seen so far"
    print(f"Geração #{gen:3}: ", end="")
    colorize(phr)
    print(f"  score: {fit:2}/{len(target)}")
