# my_list = [10, "Hello", 20]
# print(len(my_list))
# my_list = [1, 5, =10, 4.5]
# for i in range(len(my_list)) :
#     print(i)
# my_list_vars = [a, b, c, d, e, f]
# print(len(my_list_vars))
# my_list_vars = [v_a, v_b, v_c]
# print(len(my_list_vars))


r_ac = []
r_ab = [1.099, 0.766, 1.423]
r_bc = [1.079, 1.418, 0.789]
for i in range (len(min(r_ab, r_bc))) :
    r_ac[i] = r_ab[i] + r_bc[i]
print(r_ac)