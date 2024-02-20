# WAP to append new content to an existing one.

with open("sample.txt", "a") as file:
    file.write("\nWelcome")

with open("sample.txt", "r") as file1:
    print(file1.read())
file.close()
file1.close()