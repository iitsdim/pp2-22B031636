import re


def read_file(fpath: str):
    with open(fpath, mode='r', encoding='utf8') as f:
        return f.read()


txt = read_file('row.txt')
# 1
# print(re.findall('ab?', txt)[0])
# 2
# print(re.findall('ab{2,3}', txt)[0])
# 3
# print(re.findall('[a-z]_[a-z]', txt)[0]) # single underscore
# print(re.findall('[a-z]_+[a-z]', txt)[0]) # single underscore
# 4
# print(re.findall('[A-Z][a-z][a-z]+', txt)[0]) # single underscore
# 5
# print(re.findall('a.*b$', txt)[0])
# 6
# print(re.sub('[ ,.]', ':', txt))
# 7
# txt = "snake_case"
# x = re.split("_", txt)
# print(''.join(y.capitalize() for y in x))
# 8
# txt = 'aaaAbb'
# x = re.sub("([A-Z])", r" \1", txt).split()
# print(' '.join(x))
# 9
# txt = 'aaaABb'
# x = re.sub("([A-Z][a-b]*)", r" \1", txt).split()
# print(' '.join(x))
# 10
txt = 'aaaABb'
x = re.sub("([A-Z][a-b]*)", r" \1", txt).split()
print('_'.join(y.lower() for y in x))
