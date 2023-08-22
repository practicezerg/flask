import random


def random_num():
    num_list2 = [num for num in range(1, 26)]
    return str(random.choice(num_list2))



def hello_user(login):
    return f"Hellow {login}"
