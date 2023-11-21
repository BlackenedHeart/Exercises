import easygui

integer_list = [10, 20, 30, 40, 50]

user_integer1 = easygui.integerbox("Enter an integer:")

for num in integer_list:
    if num == user_integer1:
        easygui.msgbox(f"The entered integer {user_integer1} belongs to the list.")
        break
else:
    easygui.msgbox("The entered integer is not in the list.")

user_integer2 = easygui.integerbox("Enter a positive integer:")

divisor = 2
while divisor < user_integer2:
    if user_integer2 % divisor == 0:
        easygui.msgbox(f"The first divisor found is: {divisor}.")
        break
    divisor += 1
else:
    easygui.msgbox(f"The integer {user_integer2} is prime.")