# Square
my_list = [5,4,3]

new_list = list(map(lambda num: num**2, my_list))
print(new_list)

# List Sorting Based on second number in pairs
a = [(0,2), (4,3), (9,9), (10,-1)]
a.sort(key = lambda x: x[1])

# a.sort = use sort function
# x = states that each pair is one
# x[1] = second value in each pair

print(a)