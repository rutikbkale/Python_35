 # WAP  to read text file & create a new file with reverse the content.

with open("sample.txt", "w") as file:
    file.write("hello world")

with open("sample.txt", "r") as file1:
    content = file1.read()
    print("Original content:", content)
    reverse = content[::-1]
    print("Reversed content:", reverse)

# with open("reversed_sample.txt", "w") as reversed_file:
#     reversed_file.write(reverse)
