#mutate_list function goes here
def mutate_list(list,index_num,val):
    list.insert(index_num,val)
    return list

#remove_index function goes here
def remove_index(list, index_num):
    print('Total elements in list =', len(list))
    list.remove(index_num)
    print('Total elements in list =', len(list))
    return list
#reverse_list function goes here
def reverse_list(list):
    list.reverse()
    return list

def main():
    #DO NOT MODIFY THIS FUNCTION
    user_list = input("Enter values in list separated by commas: \n")
    user_list = user_list.split(",")
    user_list = [int(i) for i in user_list]
    print(user_list)
    print("Menu: ")
    print("mutate list(m), remove (r), reverse_list (R)")
    user_choice = input("Enter choice (m,r,R): \n")
    if user_choice == 'm':
        index_num, v = input("\n").split(",")
        index_num = int(index_num)
        v = int(v)
        mutate_list(user_list, index_num, v)
        print(user_list)
    elif user_choice == 'r':
        index_num = int(input("\n"))
        remove_index(user_list, index_num)
        print(user_list)
    elif user_choice == 'R':
        new_list = reverse_list(user_list)
        print(new_list)
main()