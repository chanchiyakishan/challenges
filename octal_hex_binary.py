def print_formatted(number):
    length = len(bin(number).split("b")[1])
    print("Decimal Octal Hex Binary")
    for i in range(1,number+1):
        print(str(i).rjust(length), oct(i).split("o")[1].rjust(length), str(hex(i).split("x")[1].rjust(length)).upper(), bin(i).split("b")[1].rjust(length))
if __name__ == '__main__':
    n = int(input("Enter the value:"))
    print_formatted(n)
