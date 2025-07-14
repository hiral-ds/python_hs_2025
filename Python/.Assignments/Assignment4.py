A = frozenset([10, 20, 30, 40])
B = frozenset([30, 40, 50, 60])

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference (A - B):", A - B)
print("Symmetric Difference:", A ^ B)
print("Is A a superset of {10, 20}?", A.issuperset({10, 20}))

try:
    A.add(70)
except AttributeError as e:
    print("Error adding to frozenset:", e)

print("Length of A:", len(A))
print("Length of B:", len(B))