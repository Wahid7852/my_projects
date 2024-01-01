def common_member(list1, list2):
    for i in list1:
        if i in list2:
            return True
    return False

list1 = input("Enter the first list: ").split()
list2 = input("Enter the second list: ").split()
print(common_member(list1, list2))