def test_range(n):
    if n in range(100,999):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(666)