import sys


def validate(nb, base):
    if nb < 0 or len(set(base)) != len(base):
        raise ValueError


def ito_Base(nb, base):
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
        print("incorrect value")
    else:
        print(ito_Base(nb, base))


if __name__ == "__main__":
    main()