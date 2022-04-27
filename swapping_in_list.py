# Accepting user input for list
input_string = input('Enter elements of a list separated by space ')
user_list = input_string.split()

# convert each item to int type
for i in range(len(user_list)):
    # convert each item to int type
    user_list[i] = int(user_list[i])

pos1 = int(input("Enter location 1 for swap: "))
pos2 = int(input("Enter location 2 for swap: "))


def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


print(swapPositions(user_list, pos1 - 1, pos2 - 1))
