t1 = ("Ayush", "Tripathi")
t2 = ("Sakshi", "Shete")
list1 = []
for i in range(0, 2):
    list1.append(t1[i])

for i in range(0, 2):
    list1.append((t2[i]))


def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct


print(Convert(list1))
