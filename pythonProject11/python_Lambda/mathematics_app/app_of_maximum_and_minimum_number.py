int_a = int(input('enter first input'))
min_val = int_a
max_val = int_a
int_b = int(input('enter first input'))
int_c = int(input('enter first input'))

if max_val <= int_b:
    max_val = int_b
elif max_val <= int_c:
    max_val = int_c

if min_val >= int_b:
    min_val = int_b
elif min_val >= int_c:
    min_val = int_c
print(min_val)
print(max_val)

int_num = int(input('enter first input'))
min_val = int_num
max_val = int_num

for elements in range(2, 7):
    int_num = int(input(f'enter input {elements}'))
    if min_val >= int_num:
        min_val = int_num
    if max_val <= int_num:
        max_val = int_num
print(min_val)
print(f"{max_val} is the highest input")
