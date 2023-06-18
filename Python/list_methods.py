l = [11, 45, 1, 2, 5, 6, 1]
# print(l)
# l.reverse()
# l.append(7)
# l.sort(reverse=True)
# print(l.index(1))
# print(l.count(1))

# if m is equal to l, then both are linked realtime
# changing m will change l too!
# to avoid this, copy list by:
# # m = l.copy()
# m = l
# print(l)
# m[0] = 0
# l.insert(1, 899)
# print(l)

m = [900, 1000, 1100]
l.extend(m)

# to concatenate contents of both lists
k = l + m
