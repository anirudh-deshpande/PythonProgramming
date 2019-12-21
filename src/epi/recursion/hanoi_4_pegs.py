NUM_PEGS = 4

def hanoi_4_pegs(num_rings):

    def hanoi(num_rings, from_peg, to_peg, aux1, aux2, movements, pegs):
        if num_rings > 0:
            hanoi(num_rings-2, from_peg, aux1, aux2, to_peg, movements, pegs)

            # last but 1
            movements.append([from_peg, aux2])
            print('Moving from {} to {}'.format(from_peg, aux2))
            pegs[aux2].append(pegs[from_peg].pop())

            # last
            movements.append([from_peg, to_peg])
            print('Moving from {} to {}'.format(from_peg, to_peg))
            pegs[to_peg].append(pegs[from_peg].pop())

            # last but 1
            movements.append([aux2, to_peg])
            print('Moving from {} to {}'.format(aux2, to_peg))
            pegs[to_peg].append(pegs[aux2].pop())

            hanoi(num_rings-2, aux1, to_peg, aux2, from_peg, movements, pegs)

    movements = []
    pegs = [list(reversed(range(1, num_rings+1)))] + [[] for _ in range(1, NUM_PEGS)]
    hanoi(num_rings, 0, 3, 1, 2, movements, pegs)
    print(len(movements))
    print(pegs)


if __name__ == "__main__":
    hanoi_4_pegs(10)




