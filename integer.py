first=1
second=2
third=3
fourth=4
fifth=5
print(type(first), type(fifth))
print(f'{first} {second} {third} {fourth} {fifth}')









action=float(input('type the number of action u need:\n1.multiply\n2.devide\n3.add\n4.deduct\n'))

if action==1:
    num_1=int(input("type in first number u wanna multiply:\n"))
    num_2=int(input("type in second number u wanna multiply:\n"))
    print('result u r desperately seeking is ', num_1 * num_2)

elif action==2:
    num_1=int(input("type in first number u wanna devide:\n"))
    num_2=int(input("type in second number u wanna devide:\n"))
    print('result u r desperately seeking is ', num_1 / num_2)

elif action==3:
    num_1=int(input("type in first number u wanna add:\n"))
    num_2=int(input("type in second number u wanna add:\n"))
    print('result u r desperately seeking is ', num_1 + num_2)

elif action==4:
    num_1=int(input("type in first number u wanna deduct:\n"))
    num_2=int(input("type in second number u wanna deduct:\n"))
    print('result u r desperately seeking is ', num_1 / num_2)