
# file_size

import os

size = os.path.getsize("cat.jpeg")
print(size)

def byte_to_kb(byte):
    kb = byte / 1000
    return kb

print("{}kB".format(byte_to_kb(size)))
