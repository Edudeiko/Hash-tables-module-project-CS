cach = {}


def expensive_seq(x, y, z):
    if x < 0 or y < 0 or z < 0:
        return f'Error, please enter a valid number'

    if 
    exps(x, y, z) =
    if x <= 0: y + z
    if x >  0: exps(x-1,y+1,z) + exps(x-2,y+2,z*2) + exps(x-3,y+3,z*3)

    # `x`, `y`, and `z` are all greater than or equal to zero.


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
