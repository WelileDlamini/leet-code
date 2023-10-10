def total_values():
    user_input = input("enter the value: ")

    if user_input == '':
        return 0.0
    
    else:
        return int(user_input)+ total_values()
    
total = total_values()

print(total)