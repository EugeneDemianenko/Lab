
values = input()[0:8]

ddnf = ""
dknf = ""
print("\t a \t b \t c   |   f")
for i in range(8):
    a = (i & 4) >> 2
    b = (i & 2) >> 1
    c = (i & 1)

    if values[i] == '1':
        ddnf += " v " if ddnf != "" else ""
        ddnf += f"{'' if a == 1 else '!'}a^{'' if b == 1 else '!'}b^{'' if c == 1 else '!'}c"
    else:
        dknf += " ^ " if dknf != "" else ""
        dknf += f"({'' if a == 0 else '!'}av{'' if b == 0 else '!'}bv{'' if c == 0 else '!'}c)"

    print(f"\t {a} \t {b} \t {c}   |   {values[i]}")

print(f"DDNF: {ddnf}")
print(f"DKNF: {dknf}")