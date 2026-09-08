# WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)
# [1, 2, 3, 2, 1]
# [1, “abc”, “abc”, 1

list1=[1,2,3,2,1]
copy_list=list1.copy()
copy_list.reverse()

if list1 == copy_list:
    print("list is palindrome")
else:
    print("list is not palindrome")