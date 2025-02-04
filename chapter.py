# list_to_tuple function goes here
def list_to_tuple(a_list):
    the_variable = 0
    for i in range(len(a_list)):
        variable = a_list[i]
        try:
            a_list[i] = int(variable)
        except:
            print("Error. Please enter only integers.")
            the_variable = 1
            break
    if the_variable != 1:
        print(tuple(a_list))


def main():
    # DO NOT MODIFY THIS FUNCTION
    a_list = input("Enter elements of list separated by commas: \n").strip().split(',')
    list_to_tuple(a_list)


main()