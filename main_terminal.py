import os

a = input("Enter anything associated with the package you want to search: ")
print("--------------------------------------------------------------------------------------")
print("                               apt searcher has been started                          ")
print("--------------------------------------------------------------------------------------\n")
search_command = "apt-cache search " + a
search_result = os.popen(search_command).read()

if not search_result.strip():
    if a:
        print("No results found for package:", a)
else:
    print(search_result)
