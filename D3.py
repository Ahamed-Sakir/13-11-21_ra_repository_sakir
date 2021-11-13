import random
import timeit

start = timeit.default_timer()
max_num = 30000

first_list = [random.randint(0, max_num*3) for _ in range(max_num)]
second_list = [random.randint(0, max_num*4) for _ in range(max_num)]

first_dict = {}
for lm in first_list:
    if lm in first_dict:
        first_dict[lm] += 1
    else:
        first_dict[lm] = 1
second_dict = {}
for lm in second_list:
    if lm in second_dict:
        second_dict[lm] += 1
    else:
        second_dict[lm] = 1

num_list_2 = []
for key in first_dict:
    if key in second_dict:
        for i in range(first_dict[key]):
            num_list_2.append(i)

stop = timeit.default_timer()

print('Time: ', stop - start)       