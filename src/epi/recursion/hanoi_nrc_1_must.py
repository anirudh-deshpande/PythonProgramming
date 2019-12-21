import collections

NUM_PEGS = 3

def hanoi_nrc_1_must(num_rings, from_peg, to_peg, must_peg):

    StackState = collections.namedtuple("StackState", ("num_rings", "from_peg", "to_peg"))
    Move = collections.namedtuple("Move", ("from_peg", "to_peg"))

    def get_aux_peg(from_peg, to_peg):
        return [num for num in range(NUM_PEGS) if num not in [from_peg, to_peg]][0]

    def hanoi(num_rings, from_peg, to_peg, must_peg):

        stack = [StackState(num_rings, from_peg, to_peg)]
        moves = []

        while stack:
            state = stack.pop()

            if state.num_rings == 1:
                # if state.to_peg != must_peg and state.from_peg != must_peg:
                #     moves.append(Move(state.from_peg, must_peg))
                #     moves.append(Move(must_peg, state.to_peg))
                # else:
                moves.append(Move(state.from_peg, state.to_peg))

            if state.num_rings > 1:
                aux_peg = get_aux_peg(state.from_peg, state.to_peg)

                if state.from_peg != must_peg and state.to_peg != must_peg:
                    stack.append(StackState(state.num_rings, state.from_peg, must_peg))
                    stack.append(StackState(state.num_rings, must_peg, state.to_peg))

                stack.append(StackState(state.num_rings - 1, aux_peg, state.to_peg))
                stack.append(StackState(1, state.from_peg, state.to_peg))
                stack.append(StackState(state.num_rings - 1, state.from_peg, aux_peg))

        return moves

    return hanoi(num_rings, from_peg, to_peg, must_peg)


moves = hanoi_nrc_1_must(2, 0, 2, 1)
for move in moves:
    print("Moving from {} to {}".format(move.from_peg, move.to_peg))