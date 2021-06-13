import re
import sys


def f(str1, str2):
    pattern = "^"
    for i in range(len(str2)):
        if str2[i] != "*":
            pattern += str2[i]
        else:
            pattern += ".*"
    pattern += "$"
    if re.search(pattern, str1):
        return "OK"
    else:
        return "KO"


def main():
    str1 = sys.argv[1]
    str2 = sys.argv[2]
    print(f(str1, str2))


if __name__ == "__main__":
    main()