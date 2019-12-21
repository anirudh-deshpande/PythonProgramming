def hanoi_rc_end_must(num_rings, start, end, aux):
    if num_rings > 0:
        hanoi_rc_end_must(num_rings- 1, start, end, aux)
        print("Moving from {} to {}".format(start, end))
        hanoi_rc_end_must(num_rings - 1, end, aux, start)
        print("Moving from {} to {}".format(start, end))
        hanoi_rc_end_must(num_rings - 1, aux, end, start)

hanoi_rc_end_must(3, 0, 2, 1)

