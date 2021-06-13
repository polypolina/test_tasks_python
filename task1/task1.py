import sys


def validate(nb, base):
    if nb < 0 or len(set(base)) != len(base):
        raise ValueError


def ito_base(nb, base):
    b = len(base)
    result = ''
    while nb > 0:
        mod = nb % b
        nb = nb // b
        result += base[mod]

    return result[::-1]


def main():
    try:
        nb = int(sys.argv[1])
        base = sys.argv[2]
        validate(nb, base)
    except (IndexError, ValueError):
        print("Использование: task1.py arg1 - integer arg2 - sting (arg2 must contain unique characters)")
    else:
        print(ito_base(nb, base))


if __name__ == "__main__":
    main()
