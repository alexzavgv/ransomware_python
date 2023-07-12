list1 = []
file = open('/Users/alexzavgorodnev/PycharmProjects/lists/txt', 'r')
list2 = [list1.append(word) for word in file]
print(list2)