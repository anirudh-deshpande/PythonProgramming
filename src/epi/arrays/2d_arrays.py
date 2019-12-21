
num_rings = 3
NUM_PEGS = 3

pegs = [list(reversed(range(1, num_rings + 1)))]
pegs += [[] for _ in range(1, NUM_PEGS)]

print(pegs)

print(-1%3)