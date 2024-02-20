# WAP to write a binary data into a file.

binarydata = b'\x48\x65\x6C\x6C\x6F\x20\x57\x6F\x72\x6C\x64'
with open("sample.bin", "wb") as file:
    file.write(binarydata)
    file.close()
