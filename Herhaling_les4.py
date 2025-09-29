def p_dubbel(x):
    print(f"het dubbel van{x} is {x*2}")

def r_dubbel(x):
    return (f"het dubbel van{x} is {x*2}\n"
            f"--------------------")

for _ in range(1,11):
    print(r_dubbel(_))

