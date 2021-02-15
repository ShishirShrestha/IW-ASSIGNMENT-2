def char_mix(a, b):
  a1 = b[:2] + a[2:]
  b1 = a[:2] + b[2:]

  return a1 + ' ' + b1

print(char_mix('abc', 'xyz'))