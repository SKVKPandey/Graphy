
def Gen(val):

    from random import randint
    from time import sleep


    total_1 = 0
    final_1 = val
    num_list = []

    while True:

        if total_1 >= final_1:
            total_1 = final_1

        num_list.append(total_1)

        if total_1 == final_1:
            return(num_list)
            break
            

        else:
            total_1 = total_1 + 10 + randint(-6, 8)


