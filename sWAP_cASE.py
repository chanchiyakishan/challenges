def swap_case(s):
    li = list(s)
    counter = 0
    for i in s:
        if i == i.lower():
            li[counter] = i.upper()
        else:
            li[counter] = i.lower()
        counter += 1
    string = ""
    return string.join(li)
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
