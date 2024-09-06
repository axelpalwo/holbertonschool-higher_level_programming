#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    index = 1
    if len(sys.argv) > 1:
        while index < len(sys.argv):
            result += int(sys.argv[index])
            index += 1
    print(result)
