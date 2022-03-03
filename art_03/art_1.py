with open("test.py") as file_obj:
    list_str = file_obj.readlines()
remove_list = []
for i in list_str:
    for j in i:
        if j == "#":
            remove_list.append(i)
for i in remove_list:
    list_str.remove(i)
with open("test.py", "w") as write_obj:
    for i in list_str:
        write_obj.write(i)
print("Complete")
