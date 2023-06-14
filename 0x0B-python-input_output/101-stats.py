#!/usr/bin/python3
"""Subroutine to print status codes with nonzero value in
    numericalorder"""

def print_statistic(l, status_codes):
    """script that reads stdin line by line and computes metrics."""
    print("File size: {}".format(l))
    for cle in sorted(status_codes):
        print("{}: {}".format(cle, status_codes[cle]))


if __name__ == "__main__":
    import sys

    l = 0
    status_codes = {}
    validc = ['200', '301', '400', '401', '403', '404', '405', '500']
    res = 0

    try:
        for a in sys.stdin:
            if res == 10:
                print_stats(l, status_codes)
                res = 1
            else:
                res += 1

            a = a.split()

            try:
                l += int(a[-1])
            except (IndexError, ValueError):
                pass

            try:
                if a[-2] in validc:
                    if status_codes.get(a[-2], -1) == -1:
                        status_codes[a[-2]] = 1
                    else:
                        status_codes[a[-2]] += 1
            except IndexError:
                pass

        print_stats(l, status_codes)

    except KeyboardInterrupt:
        print_statistic(l, status_codes)
        raise
