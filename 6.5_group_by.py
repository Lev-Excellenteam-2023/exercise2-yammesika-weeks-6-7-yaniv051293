def group_by(func, args):
    dic = {}
    for item in args:
        dic.setdefault(func(item), []).append(item)
    return dic


def main():
    assert(group_by(len, ["hi", "bye", "yo", "try"])=={2: ["hi", "yo"], 3: ["bye", "try"]})

if __name__ == '__main__':
    main()
