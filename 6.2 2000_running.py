import timeit

def timer(f ,*args, **optionals):
    exec_time = timeit.timeit(lambda: f(*args, **optionals),number=1)
    return f'execution time is: {exec_time * 10**3:.10f}'


def main():
    print(timer(print, "Hello"))
    print(timer(zip, [1, 2, 3], [4, 5, 6]))
    print(timer("Hi {name}".format, name="Bug"))


if __name__ == '__main__':
    main()
