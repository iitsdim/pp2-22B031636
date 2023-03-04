import os
import string

# 1
# path = input()
# directories = []
# files = []
# for name in os.listdir(path):
#     if os.path.isdir(os.path.join(path, name)):
#         directories.append(name)
#     else:
#         files.append(name)
#
# print("only dir: " + ' '.join(directories))
# print("only files: " + ' '.join(files))
# print("both: " + ' '.join(directories) + ' ' + ' '.join(files))

# 2
# path = input()
# print(os.path.exists(path)) # EXISTS
# print(os.access(path, os.R_OK)) # READ
# print(os.access(path, os.W_OK)) # WRITE
# print(os.access(path, os.X_OK)) # EXECUTABLE

# 3
# path = input()
# if os.path.exists(path):
#     parts = path.split('\\')
#     print(parts[-2], parts[-1])
# else:
#     print("DOES NOT EXISTS")

# 4
# with open("4task.txt", 'r') as fp:
#     print(len(fp.readlines()))

#5
# L = ['line1', 'line2', 'line3']
# with open("4task.txt", "w") as fp:
#     for x in L:
#         fp.write(x + "\n")

#6
# letters = string.ascii_uppercase
# for letter in letters:
#     with open(f"{letter}.txt", "w") as f:
#         f.write("")
#7
# with open('4task.txt', 'r') as from_this_file, open('A.txt', 'a') as to_that_file:
#     for line in from_this_file:
#         to_that_file.write(line)
# 8
path = input()
if os.path.exists(path):
    os.remove(path)

# letters = string.ascii_uppercase
# for letter in letters:
#     path = f"C:\\Users\\User\\PycharmProjects\\pp2-22B031636\\tsis6\\{letter}.txt"
#     if os.path.exists(path):
#         os.remove(path)