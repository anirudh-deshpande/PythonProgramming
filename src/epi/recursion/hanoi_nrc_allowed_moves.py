import collections

NUM_PEGS = 3

def hanoi_nrc_allowed_moves(num_rings):

    StackState = collections.namedtuple("StackState", ("from_peg", "to_peg", "remaining_rings"))
    Move = collections.namedtuple("Move", ("from_peg", "to_peg"))

    allowed_moves = [(0, 1), (1, 2), (2, 0)]

    other_moves = {
        (1, 0): [(1, 2), (2, 0)],
        (2, 1): [(2, 0), (0, 1)],
        (0, 2): [(0, 1), (1, 2)]
    }

    def get_aux_peg(from_peg, to_peg):
        return [num for num in range(NUM_PEGS) if num not in [from_peg, to_peg]][0]

    def hanoi(n, from_p, to_p):
        stack = [StackState(from_p, to_p, n)]
        moves = []
        pegs = [[] for _ in range(NUM_PEGS)]
        pegs[from_p] = list(reversed(range(1, n+1)))

        print('Initial state {}'.format(pegs))

        while stack:
            state = stack.pop()
            cur_move = (state.from_peg, state.to_peg)

            if cur_move in allowed_moves:
                if state.remaining_rings == 1:
                    moves.append(Move(state.from_peg, state.to_peg))
                    pegs[state.to_peg].append(pegs[state.from_peg].pop())
                elif state.remaining_rings > 1:
                    aux_peg = get_aux_peg(state.from_peg, state.to_peg)

                    stack.append(StackState(aux_peg, state.to_peg, state.remaining_rings-1))
                    stack.append(StackState(state.from_peg, state.to_peg, 1))
                    stack.append(StackState(state.from_peg, aux_peg, state.remaining_rings-1))
            else:
                for move in list(reversed(other_moves[cur_move])):
                    f, t = move
                    stack.append(StackState(f, t, state.remaining_rings))

        print('Final state  {}'.format(pegs))
        return moves

    return hanoi(num_rings, 0, 2)


all_moves = hanoi_nrc_allowed_moves(5)
for moved in all_moves:
    print("Moving from {} to {}".format(moved.from_peg, moved.to_peg))
print(len(all_moves))
