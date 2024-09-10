first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
ID = input("Please enter your ID: ")

verify = False
f_name_v = False
l_name_v = False
digit_v = False
numerical_portion = ID[4:]
odd_num = []
even_num = []
if ID[:2].casefold() == first_name[:2].casefold():
    f_name_v = True
if ID[2:4].casefold() == last_name[:2].casefold():
    l_name_v = True

char_count = 1
for char in numerical_portion:
    current_char = numerical_portion[char_count-1:char_count]

    if char_count != len(numerical_portion):
        if  char_count % 2 == 0:
            even_num.append(current_char)
        else:
            odd_num.append(current_char)

    char_count+=1

even_total = 0
for num in even_num:
    even_total += int(num)

odd_total = 0
for num in odd_num:
    odd_total += int(num)

input_validate = abs(even_total - odd_total)
if input_validate > 10:
    input_validate = input_validate%10

if input_validate == int(numerical_portion[len(numerical_portion)-1:]):
    digit_v = True

if f_name_v and l_name_v and digit_v:
    print("PASS")
else:
    print("INVESTIGATE")

