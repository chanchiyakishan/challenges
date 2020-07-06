import textwrap

def wrap(string, max_width):
    value = string
    # Wrap this text. 
    wid = max_width
    wrapper = textwrap.TextWrapper(width=wid) 
    word_list = wrapper.wrap(text=value) 
    li = list()
    for element in word_list: 
        li.append(element)
        li.append("\n")
    string = ""
    return string.join(li)
if __name__ == '__main__':
    string, max_width = input("enter the string you want to wrap"), int(input("Enter the amount of string to be wrappend into line"))
    result = wrap(string, max_width)
    print(result)
