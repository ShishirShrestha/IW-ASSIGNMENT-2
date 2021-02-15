def func_compute(n):
 return lambda x : x * n
result = func_compute(2)
print("Twice the number of 15 =", result(15))