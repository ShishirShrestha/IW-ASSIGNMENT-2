is_num = lambda q: q.replace('.','',1).isdigit()
is_num1 = lambda r: is_num(r[1:]) if r[0]=='-' else is_num(r)
n = input('enter number or string:- ')
print(is_num1(n))