import sys


def create_domain_file(domain_file_name, n_, m_):
    disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
    pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
    domain_file = open(domain_file_name, 'w')  # use domain_file.write(str) to write to domain_file
    "*** YOUR CODE HERE ***"

    domain_file.write("Propositions:\n")
    props = set()
    for p in pegs:
        props.add(f"empty_in_{p}")

    for i, d in enumerate(disks):
        for p in pegs:
            props.add(f"{d}_bottom_in_{p}")
            props.add(f"{d}_top_in_{p}")
            for j in range(i + 1, len(disks)):
                props.add(f"{d}_on_{disks[j]}_in_{p}")

    for p in props:
        domain_file.write(p + ' ')

    domain_file.write('\nActions:\n')

    for i in range(len(disks)):
        for j in range(i + 1, len(disks)):
            for k in range(i + 1, len(disks)):
                if k != j :
                    for p1 in pegs:
                        for p2 in pegs:
                            if p1 != p2:
                                d1 = disks[i]
                                d2 = disks[j]
                                d3 = disks[k]

                                action = f"m_{d1}_from_{d2}_in_{p1}_to_{d3}_in_{p2}"
                                preconditions = [f"{d1}_on_{d2}_in_{p1}",
                                                 f"{d1}_top_in_{p1}",
                                                 f"{d3}_top_in_{p2}"]
                                add_effects = [f"{d1}_on_{d3}_in_{p2}",
                                               f"{d2}_top_in_{p1}",
                                               f"{d1}_top_in_{p2}"]

                                domain_file.write(f"Name: {action}\n")
                                domain_file.write("pre: " + " ".join(preconditions) + '\n')
                                domain_file.write("add: " + " ".join(add_effects) + '\n')
                                domain_file.write("delete: " + " ".join(preconditions) + '\n')

    for i in range(len(disks)):
        for p1 in pegs:
            for p2 in pegs:
                if p1 != p2:
                    d1 = disks[i]

                    action = f"m_{d1}_in_{p1}_to_{p2}"
                    preconditions = [f"{d1}_top_in_{p1}",
                                     f"{d1}_bottom_in_{p1}",
                                     f"empty_in_{p2}"]
                    add_effects = [f"{d1}_top_in_{p2}",
                                     f"{d1}_bottom_in_{p2}",
                                     f"empty_in_{p1}"]

                    domain_file.write(f"Name: {action}\n")
                    domain_file.write(
                        "pre: " + " ".join(preconditions) + '\n')
                    domain_file.write(
                        "add: " + " ".join(add_effects) + '\n')
                    domain_file.write(
                        "delete: " + " ".join(preconditions) + '\n')

    # Disk on empty to on disk
    for i in range(len(disks)):
        for j in range(i + 1, len(disks)):
            for p1 in pegs:
                for p2 in pegs:
                    if p1 != p2:
                        d1 = disks[i]
                        d2 = disks[j]

                        action = f"m_{d1}_in_{p1}_to_{d2}_in_{p2}"
                        preconditions = [f"{d1}_bottom_in_{p1}",
                                         f"{d1}_top_in_{p1}",
                                         f"{d2}_top_in_{p2}"]
                        add_effects = [f"{d1}_on_{d2}_in_{p2}",
                                       f"empty_in_{p1}",
                                       f"{d1}_top_in_{p2}"]

                        domain_file.write(f"Name: {action}\n")
                        domain_file.write(
                            "pre: " + " ".join(preconditions) + '\n')
                        domain_file.write(
                            "add: " + " ".join(add_effects) + '\n')
                        domain_file.write(
                            "delete: " + " ".join(preconditions) + '\n')

        # Disk on disk to empty
        for i in range(len(disks)):
            for j in range(i + 1, len(disks)):
                for p1 in pegs:
                    for p2 in pegs:
                        if p1 != p2:
                            d1 = disks[i]
                            d2 = disks[j]

                            action = f"m_{d1}_on_{d2}_in_{p1}_to_{p2}"
                            preconditions = [f"{d1}_on_{d2}_in_{p1}",
                                             f"{d1}_top_in_{p1}",
                                             f"empty_in_{p2}"]
                            add_effects = [f"{d1}_top_in_{p2}",
                                           f"{d1}_bottom_in_{p1}",
                                           f"{d2}_top_in_{p1}"]

                            domain_file.write(f"Name: {action}\n")
                            domain_file.write(
                                "pre: " + " ".join(preconditions) + '\n')
                            domain_file.write(
                                "add: " + " ".join(add_effects) + '\n')
                            domain_file.write(
                                "delete: " + " ".join(preconditions) + '\n')

    domain_file.close()


def create_problem_file(problem_file_name_, n_, m_):
    disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
    pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
    problem_file = open(problem_file_name_, 'w')  # use problem_file.write(str) to write to problem_file
    "*** YOUR CODE HERE ***"
    problem_file.write("Initial state: ")

    for p in pegs[1:]:
        problem_file.write(f"empty_in_{p} ")

    problem_file.write(f"{disks[n - 1]}_bottom_in_{pegs[0]} ")
    for i in range(n - 1):
        problem_file.write(f"{disks[i]}_on_{disks[i + 1]}_in_{pegs[0]} ")
    problem_file.write(f"{disks[0]}_top_in_{pegs[0]} \n")

    problem_file.write("Goal state: ")

    problem_file.write(f"{disks[n - 1]}_bottom_in_{pegs[-1]} ")
    for i in range(n - 1):
        problem_file.write(f"{disks[i]}_on_{disks[i + 1]}_in_{pegs[-1]} ")
    problem_file.write(f"{disks[0]}_top_in_{pegs[0]} ")

    for p in pegs[0: m - 1]:
        problem_file.write(f"empty_in_{p} ")

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
