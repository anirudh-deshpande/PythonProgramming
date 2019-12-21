import collections

"""
0 -> 1  ==> 0 -> 2 and 2 -> 1
0 -> 2
1 -> 0  ==> 1 -> 2 and 2 -> 0
1 -> 2
2 -> 0
2 -> 1
"""

NUM_PEGS = 3

def hanoi_nrc_1_const_peg(num_rings):

    StackState = collections.namedtuple("StackState", ("from_p", "to_p", "num_rings"))
    Movement = collections.namedtuple("Movement", ("from_p", "to_p"))

    def get_aux(from_p, to_p):
        aux = [num for num in range(num_rings) if num not in [from_p, to_p]][0]
        # print("from {} to {} aux {}".format(from_p, to_p, aux))
        return aux

    def hanoi(n, from_peg, to_peg, req_peg):

        stack = [StackState(from_peg, to_peg, n)]
        moves = []

        while stack:
            state = stack.pop()

            if state.from_p != req_peg and state.to_p != req_peg:
                stack.append(StackState(req_peg, state.to_p, state.num_rings))
                stack.append(StackState(state.from_p, req_peg, state.num_rings))

            elif state.num_rings == 1:
                moves.append(Movement(state.from_p, state.to_p))
            elif state.num_rings > 1:
                aux_peg = get_aux(state.from_p, state.to_p)

                stack.append(StackState(aux_peg, state.to_p, state.num_rings-1))
                stack.append(StackState(state.from_p, state.to_p, 1))
                stack.append(StackState(state.from_p, aux_peg, state.num_rings-1))

        return moves

    return hanoi(num_rings, 0, 2, 1)

for move in hanoi_nrc_1_const_peg(3):
    print("Move from {} to {}".format(move.from_p, move.to_p))

print(len(hanoi_nrc_1_const_peg(3)))

