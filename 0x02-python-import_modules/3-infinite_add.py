#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import math
    result = 0
    for i in sys.argv[1:]:
        result += int(i)
        print("{}".format(result))
