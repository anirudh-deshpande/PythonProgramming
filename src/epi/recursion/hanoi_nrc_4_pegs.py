import collections

NUM_PEGS = 4

def hanoi_4_pegs(num_rings):

    StackState = collections.namedtuple("StackState", ("from_peg", "to_peg", "remaining_rings"))
    Move = collections.namedtuple("Move", ("from_peg", "to_peg"))

    def get_aux_pegs(from_peg,  to_peg):
        return [num for num in range(NUM_PEGS) if num not in [from_peg, to_peg]]

    def hanoi(n, from_p, to_p):
        stack = [StackState(from_p, to_p, n)]
        moves = []
        pegs = [[] for _ in range(NUM_PEGS)]
        pegs[from_p] = list(reversed(range(1, n+1)))

        print("Start state {}".format(pegs))
        while stack:
            state = stack.pop()

            if state.remaining_rings == 1:
                pegs[state.to_peg].append(pegs[state.from_peg].pop())
                moves.append(Move(state.from_peg, state.to_peg))
            elif state.remaining_rings > 1:
                aux_peg_1, aux_peg_2 = get_aux_pegs(state.from_peg, state.to_peg)

                stack.append(StackState(aux_peg_1, state.to_peg, state.remaining_rings-2))
                stack.append(StackState(aux_peg_2, state.to_peg, 1))
                stack.append(StackState(state.from_peg, state.to_peg, 1))
                stack.append(StackState(state.from_peg, aux_peg_2, 1))
                stack.append(StackState(state.from_peg, aux_peg_1, state.remaining_rings-2))

        print("End state {}".format(pegs))
        return moves

    return hanoi(num_rings, 0, 3)

moves = hanoi_4_pegs(10)
for move in moves:
    print("Moving from {} to {}".format(move.from_peg, move.to_peg))

print(len(moves))
