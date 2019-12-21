NUM_PEGS = 3

def hanoi_1_const_peg(num_rings):
    def get_aux_peg(from_peg, to_peg):
        return [num for num in range(NUM_PEGS) if num not in [from_peg, to_peg]][0]

    def hanoi(num_rings, from_p, to_p, const_peg, movements, pegs):
        if const_peg != from_p and const_peg != to_p:
            hanoi(num_rings, from_p, const_peg, const_peg, movements, pegs)
            hanoi(num_rings, const_peg, to_p, const_peg, movements, pegs)
        elif num_rings == 1:
            print("Moving from {} to {}".format(from_p, to_p))
        elif num_rings > 1:
            aux_peg = get_aux_peg(from_p, to_p)

            hanoi(num_rings - 1, from_p, aux_peg, const_peg, movements, pegs)
            hanoi(1, from_p, to_p, const_peg, movements, pegs)
            hanoi(num_rings - 1, aux_peg, to_p, const_peg, movements, pegs)

    movements = []
    pegs = [list(reversed(range(1, num_rings+1)))] + [[] for _ in range(1, NUM_PEGS)]

    to_peg = 1
    const_peg = 1
    from_peg = 0
    num_rings = 3

    hanoi(num_rings, from_peg, to_peg, const_peg, movements, pegs)

    print(movements)
    print(pegs)
    return pegs, movements


if __name__ == "__main__":
    pegs, movements = hanoi_1_const_peg(3)
