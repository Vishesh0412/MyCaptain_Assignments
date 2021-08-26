import operator
d = dict()
def most_frequent():
    str1 = input("Enter a string: ")
    for i in str1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
most_frequent()
des = dict(sorted(d.items(), key =operator.itemgetter(1), reverse=True))
print(des)
