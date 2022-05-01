src1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
#легкое задание

def some_num(*src):
    for num in range(1, len(src)):
        if src[num] > src[num - 1]:
            yield src[num]


result = []
for i in some_num(*src1):
    result.append(i)
print(result)
#for i in some_num(*src1):
 #   print(i)
