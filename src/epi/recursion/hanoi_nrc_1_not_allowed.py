import collections

NUM_PEGS = 3

def hanoi_1_not_allowded(num_rings, from_peg, to_peg):

    StackState = collections.namedtuple("StackState", ("num_rings", "from_peg", "to_peg"))
    Move = collections.namedtuple("Move", ("from_peg", "to_peg"))

    not_allowed = {
        (2, 1): [(2, 0), (0, 1)]
    }

    def get_aux_peg(from_peg, to_peg):
        aux = [num for num in range(NUM_PEGS) if num not in [from_peg, to_peg]][0]
        print('From {} to {} aux {}'.format(from_peg, to_peg, aux))
        return aux

    def hanoi(num_rings, from_peg, to_peg):

        stack = [StackState(num_rings, from_peg, to_peg)]
        moves = []
        pegs = [list(reversed(range(1, num_rings+1)))] + [[] for _ in range(1, NUM_PEGS)]

        while stack:
            state = stack.pop()

            if (state.from_peg, state.to_peg) in not_allowed:
                for f, t in reversed(list(not_allowed[(state.from_peg, state.to_peg)])):
                    stack.append(StackState(state.num_rings, f, t))

            elif state.num_rings == 1:
                moves.append(Move(state.from_peg, state.to_peg))
                pegs[state.to_peg].append(pegs[state.from_peg].pop())

            elif state.num_rings > 1:
                aux_peg = get_aux_peg(state.from_peg, state.to_peg)

                stack.append(StackState(state.num_rings - 1, aux_peg, state.to_peg))
                stack.append(StackState(1, state.from_peg, state.to_peg))
                stack.append(StackState(state.num_rings - 1, state.from_peg, aux_peg))

        return moves, pegs

    return hanoi(num_rings, from_peg, to_peg)


moves, pegs = hanoi_1_not_allowded(10, 0, 2)
for move in moves:
    print('Moving from {} to {}'.format(move.from_peg, move.to_peg))

print(pegs)
print(len(moves))



