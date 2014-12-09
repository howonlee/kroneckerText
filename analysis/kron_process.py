with open("../truncated_graph.txt", "r") as kron_file:
    for line in kron_file:
        first, second = tuple(line.split())
        if first == "__none__" or second == "__none__": continue
        first, second= int(first), int(second)
        if first < 10000 and second < 10000:
            print first, second
