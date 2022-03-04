def intnum_validation(msg1, msg2):
    while True:
        num = input(msg1)
        if num.isnumeric() and int(num) >= 0:
            num=int(num)
            break
        else:
            print(msg2)
    return num

def floatnum_validation(msg1, msg2):
    while True:
        num = input(msg1)
        if num.isnumeric() and float(num) >= 0:
            num=float(num)
            break
        else:
            print(msg2)
    return num

def str_validation(msg1, msg2):
    while True:
        a = input(msg1)
        if a.replace(' ', "").isalpha():
            a=a.title()
            break
        else:
            print(msg2)
    return a


def str_num_validation(msg1, msg2):
    while True:
        a = input(msg1)
        if a.replace(' ', "").replace(',', '').replace('.', '').isalnum():
            a=a.title()
            break
        else:
            print(msg2)
    return a



