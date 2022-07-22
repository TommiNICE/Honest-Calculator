# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_list = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]
memory = 0.0
continue_calc = True


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        output = True
    else:
        output = False
    return output


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
    return print(msg)


while True:
    calc = input(msg_0)
    list_calc = calc.split(" ")
    oper = list_calc[1]
    try:
        if list_calc[0] == "M" and list_calc[2] == "M":
            y = memory
            x =memory
        elif list_calc[0] == "M":
            y = float(list_calc[2])
            x = memory
        elif list_calc[2] == "M":
            x = float(list_calc[0])
            y = memory
        else:
            x = float(list_calc[0])
            y = float(list_calc[2])
    except ValueError:
        print(msg_1)
        continue
    check(x, y, oper)
    result = 0.0
    if oper == "+":
        result = x + y
    elif oper == "-":
        result = x - y
    elif oper == "*":
        result = x * y
    elif oper == "/":
        try:
            result = x / y
        except ZeroDivisionError:
            print(msg_3)
            continue
    else:
        print(msg_2)
        continue
    print(result)
    while True:
        print(msg_4)
        answer = input(str())
        if answer == "y":
            if is_one_digit(result):
                msg_index = 10
                while True:
                    print(msg_list[msg_index])
                    answer = input(str())
                    if answer == "y":
                        if msg_index < 12:
                            msg_index += 1
                            continue
                        else:
                            memory = result
                            break
                    elif answer == "n":
                        break
                    else:
                        continue
            else:
                memory = result

            while True:
                print(msg_5)
                answer = input(str())
                if answer == "y":
                    continue_calc = True
                    break
                elif answer == "n":
                    continue_calc = False
                    break
                else:
                    continue
            break
        elif answer == "n":
            while True:
                print(msg_5)
                answer = input(str())
                if answer == "y":
                    continue_calc = True
                    break
                elif answer == "n":
                    continue_calc = False
                    break
                else:
                    continue
            break
        else:
            break
    if continue_calc:
        continue
    else:
        break


