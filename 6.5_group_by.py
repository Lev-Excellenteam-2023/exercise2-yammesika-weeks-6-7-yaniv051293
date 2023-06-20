def group_by(func, args):
    return {key: [item for item in args if func(item) == key] for key in set(map(func, args))}


def main():
    assert (group_by(len, ["hi", "bye", "yo", "try"]) == {2: ["hi", "yo"], 3: ["bye", "try"]})


if __name__ == '__main__':
    main()
