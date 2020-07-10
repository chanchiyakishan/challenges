cube = lambda x: x * x * x# complete the lambda function 

def fibonacci(n):
    fibolist = list()
    nterms = n
    n1, n2 = 0, 1
    count = 0

    # check if the number of terms is valid
    if nterms <= 0:
        pass
    elif nterms == 1:
        pass
    else:
        pass
    while count < nterms:
        fibolist.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    return fibolist
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
