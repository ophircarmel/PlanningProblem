import sys

def top(i):
    return "top-" + i
def empty(k):
    return "empty-" + k
def on(i, k):
    return "on-" + i + "-" + k
def ontop(i, j):
    return "ontop-" + i + "-" + j
def righton(i, k):
    return "righton-" + i + "-" + k

def move_i_j_h_k_l(i, j, h, k, l):
    """
    pre: top_i, on_i_k, on_j_k, ontop_i_j, top_h, on_h_l
    add: top_j, on_i_l, ontop_i_h
    delete: on_i_k, ontop_i_j, top_h
    """
    Name = "Name: Move-" + i + "-" + j + "-" + h + "-" + k + "-" + l + "\n"
    pre = "pre: " + " ".join([top(i), on(i, k), on(j, k), ontop(i, j), top(h), on(h, l)]) + "\n"
    add = "add: " + " ".join([top(j), on(i, l), ontop(i, h)]) + "\n"
    delete = "delete: " + " ".join([on(i, k), ontop(i, j), top(h)]) + "\n"
    return Name + pre + add + delete

def move_i_null_h_k_l(i, h, k, l):
    """
    pre: top_i, righton_i_k, top_h, on_h_l, on_i_k
    add: empty_k, on_i_l, ontop_i_h
    delete: right_on_i_k, top_h, on_i_k
    """
    Name = "Name: Move-" + i + "-null-" + h + "-" + k + "-" + l + "\n"
    pre = "pre: " + " ".join([top(i), righton(i, k), top(h), on(h, l), on(i, k)]) + "\n"
    add = "add: " + " ".join([empty(k), on(i, l), ontop(i, h)]) + "\n"
    delete = "delete: " + " ".join([righton(i, k), top(h), on(i, k)]) + "\n"
    return Name + pre + add + delete

def move_i_j_null_k_l(i, j, k, l):
    """
    pre: top_i, on_i_k, on_j_k, ontop_i_j, empty_l
    add: top_j, righton_i_l, on_i_l
    delete: on_i_k, ontop_i_j, empty_l
    """
    Name = "Name: Move-" + i + "-" + j + "-null-" + k + "-" + l + "\n"
    pre = "pre: " + " ".join([top(i), on(i, k), on(j, k), ontop(i, j), empty(l)]) + "\n"
    add = "add: " + " ".join([top(j), righton(i, l), on(i, l)]) + "\n"
    delete = "delete: " + " ".join([on(i, k), ontop(i, j), empty(l)]) + "\n"
    return Name + pre + add + delete

def move_i_null_null_k_l(i, k, l):
    """
    pre: top_i, righton_i_k, on_i_k, empty_l
    add: empty_k, righton_i_l, on_i_l
    delete: righton_i_k, empty_l
    """
    Name = "Name: Move-" + i + "-null-null-" + k + "-" + l + "\n"
    pre = "pre: " + " ".join([top(i), righton(i, k), on(i, k), empty(l)]) + "\n"
    add = "add: " + " ".join([empty(k), righton(i, l), on(i, l)]) + "\n"
    delete = "delete: " + " ".join([righton(i, k), empty(l), on(i, k)]) + "\n"
    return Name + pre + add + delete

# def pickup_i_j_k(i, j, k):
#     pre = "pre: noup top-" + i + " on-" + i + "-" + k + " on-" + j + "-" + k + " ontop-" + i + "-" + j
#     add = "add: up-" + i + " top-" + j
#     delete = "delete: noup top-" + i + " on-" + i + "-" + k + " ontop-" + i + "-" + j
#     return "Name: " + "Pickup-" + i + "-" + j + "-" + k + "\n" + pre + "\n" + add + "\n" + delete + "\n"
#
# def putdown_i_j_k(i, j, k):
#     """
#     pre: up_i, top_j, on_j_k
#     add: non_up top_i, on_i_k, ontop_i_j
#     delete: up_i, top_j
#     """
#     pre = "pre: up-" + i + " top-" + j + " on-" + j + "-" + k
#     add = "add: noup top-" + i + " on-" + i + "-" + k + " ontop-" + i + "-" + j
#     delete = "delete: up-" + i + " top-" + j
#     return "Name: " + "Putdown-" + i + "-" + j + "-" + k + "\n" + pre + "\n" + add + "\n" + delete + "\n"
#
# def pickup_i_null_k(i, k):
#     """
#     pre: non_up, top_i, righton_i_k
#     add: up_i, empty_p_k
#     delete: non_up, top_i, righton_i_k
#     """
#     pre = "pre: noup top-" + i + " righton-" + i + "-" + k
#     add = "add: up-" + i + " empty-" + k
#     delete = "delete: noup top-" + i + " righton-" + i + "-" + k
#     return "Name: " + "Pickup-" + i + "-null-" + k + "\n" + pre + "\n" + add + "\n" + delete + "\n"
#
# def putdown_i_null_k(i, k):
#     """
#     pre: up_i, empty_p_k
#     add: non_up, top_i, righton_i_k
#     delete: up_i, empty_p_k
#     """
#     pre = "pre: up-" + i + " empty-" + k
#     add = "add: noup top-" + i + " righton-" + i + "-" + k
#     delete = "delete: up-" + i + " empty-" + k
#     return "Name: " + "Pickup-" + i + "-null-" + k + "\n" + pre + "\n" + add + "\n" + delete + "\n"

def is_first_smaller(d1, d2):
    one = int(d1[d1.find("_")+1:])
    two = int(d2[d2.find("_")+1:])
    return one < two

def create_domain_file(domain_file_name, n_, m_):
    disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
    pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
    domain_file = open(domain_file_name, 'w')  # use domain_file.write(str) to write to domain_file
    "*** YOUR CODE HERE ***"
    propositions = ["empty-" + peg for peg in pegs] +\
                   ["top-" + disk for disk in disks] + \
                   ["righton-" + disk + "-" + peg for disk in disks for peg in pegs] + \
                   ["on-" + disk + "-" + peg for disk in disks for peg in pegs] + \
                   ["ontop-" + disk1 + "-" + disk2 for disk2 in disks for disk1 in disks] + \
                   ["up-" + disk for disk in disks] + ["noup"]

    domain_file.write("Propositions:\n")
    domain_file.write(" ".join(propositions) + "\n")

    domain_file.write("Actions:\n")
    for peg1 in pegs:
        for peg2 in pegs:
            if peg1 == peg2:
                continue
            for disk1 in disks:
                domain_file.write(move_i_null_null_k_l(disk1, peg1, peg2))
                for disk2 in disks:
                    if not is_first_smaller(disk1, disk2):
                        continue
                    domain_file.write(move_i_null_h_k_l(disk1, disk2, peg1, peg2))
                    domain_file.write(move_i_j_null_k_l(disk1, disk2, peg1, peg2))
                    for disk3 in disks:
                        if not is_first_smaller(disk1, disk3) or disk3 == disk2:
                            continue
                        domain_file.write(move_i_j_h_k_l(disk1, disk2, disk3, peg1, peg2))

    domain_file.close()


def create_problem_file(problem_file_name_, n_, m_):
    disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
    pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
    problem_file = open(problem_file_name_, 'w')  # use problem_file.write(str) to write to problem_file
    "*** YOUR CODE HERE ***"

    """
    top(0), 
    """
    initial_state = [on(disk, pegs[0]) for disk in disks] +\
                    [empty(peg) for peg in pegs[1:]] +\
                    [top(disks[0]), righton(disks[-1], pegs[0])] +\
                    [ontop(disks[i], disks[i+1]) for i in range(0,len(disks)-1)]

    goal_state =    [on(disk, pegs[-1]) for disk in disks] + \
                    [empty(peg) for peg in pegs[:-1]] + \
                    [top(disks[0]), righton(disks[-1], pegs[-1])] + \
                    [ontop(disks[i], disks[i + 1]) for i in range(0, len(disks) - 1)]
    initial_state = "Initial state: " + " ".join(initial_state) + "\n"
    goal_state = "Goal state: " + " ".join(goal_state) + "\n"

    problem_file.write(initial_state)
    problem_file.write(goal_state)

    problem_file.close()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: hanoi.py n m')
        sys.exit(2)

    n = int(float(sys.argv[1]))  # number of disks
    m = int(float(sys.argv[2]))  # number of pegs

    domain_file_name = 'hanoi_%s_%s_domain.txt' % (n, m)
    problem_file_name = 'hanoi_%s_%s_problem.txt' % (n, m)

    create_domain_file(domain_file_name, n, m)
    create_problem_file(problem_file_name, n, m)
