# array = [0, [[1,2,3,[4,5]],6,7,[8,[9]]]]
# temp = []

# def unpack_array(array, temp):

#     for i in range(len(array)):

#         elem = array[i]
#         if type(elem) == type([]):
#             unpack_array(elem, temp)
#         else:
#             temp.append(elem)

# unpack_array(array, temp)
# print(temp)

# array = [[1,2,3,4],[1,2,3,4]] 
# array2 = array.copy()

# array[0] = 5
# array2[0] = 6
# print(array, array2)

# temp = [1,4,3,2]
# print(sorted(temp), temp)

# a = [[0] * 4] * 5
# a[0][1] = 1
# print(a[0][1], a)

# print(5**2)

# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex

# a = float(x)
# b = int(y)
# c = complex(x)

# def get_sum(num1, num2):
#     print(num1+num2)

# get_sum(3, 4)



# def get_sum(num1, num2):
#     return num1+num2

# result = get_sum(3,4)
# print(result)

p = 'ecom_project/insights/csv_files/avg_events/part-00000-tid-5163453846133384237-510475b7-65c9-4096-b4c0-6908195a14cf-221-1-c000.csv'

print(len(p.split('/')))
