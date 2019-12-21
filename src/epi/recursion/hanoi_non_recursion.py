import collections

NUM_PEGS = 3

def hanoi_non_recursion(num_rings, start, end):
    State = collections.namedtuple("State", ("from_p", "to_p", "num_rings"))
    Move = collections.namedtuple("Move", ("from_p", "to_p"))

    def get_extra_peg(from_peg, to_peg):
        extra = [num for num in range(NUM_PEGS) if num not in [from_peg, to_peg]][0]
        # print("From {} to {} extra {}".format(from_peg, to_peg, extra))
        return extra


    def hanoi(num_rings, from_p, to_p):
        stack = [State(from_p, to_p, num_rings)]
        moves = []
        pegs = [[] for _ in range(NUM_PEGS)]
        pegs[from_p] = list(reversed(range(1, num_rings+1)))

        print("Start state {}".format(pegs))

        while stack:
            state = stack.pop()

            if state.num_rings == 1:
                moves.append(Move(state.from_p, state.to_p))
                # print(pegs, state.from_p, state.to_p)
                pegs[state.to_p].append(pegs[state.from_p].pop())

            elif state.num_rings > 1:
                extra_peg = get_extra_peg(state.from_p, state.to_p)

                stack.append(State(extra_peg, state.to_p, state.num_rings - 1))
                stack.append(State(state.from_p, state.to_p, 1))
                stack.append(State(state.from_p, extra_peg, state.num_rings - 1))

        print("End state {}".format(pegs))
        return moves

    return hanoi(num_rings, start, end)


moves = hanoi_non_recursion(3, 0, 2)
for move in moves:
    print("Moving from {} to {}".format(move.from_p, move.to_p))
print(len(moves))
