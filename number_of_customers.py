def process(sequence, capacity):
    if not sequence:
        return 0
    unattended = 0
    visited = set()
    alloted = set()

    for c in sequence:
        if c not in visited:
            visited.add(c)

            if len(alloted) < capacity:
                alloted.add(c)
            else:
                unattended += 1
        else:
            visited.remove(c)
            if c in alloted:
                alloted.remove(c)
        
    return unattended


if __name__ == "__main__":
    sequence = "ABCDDCEFFEBGAG"
    capacity = 3

    print(process(sequence, capacity))
