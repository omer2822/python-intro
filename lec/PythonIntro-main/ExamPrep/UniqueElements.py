def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

v = [1, 2, 3, 3, 4, 7, 3, 3, 4, 5]
vp = unique_list(v)
print(vp)
print(type(vp))

vpp = list(set(v))
print(vpp)

print(type(vpp))