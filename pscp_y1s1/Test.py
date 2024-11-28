temp = [[100, 50], [100, 4], [5, 6]]
temp.sort(key=lambda x: ( -x[0], x[1] ))
print(temp)