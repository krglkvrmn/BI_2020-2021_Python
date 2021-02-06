def generate_dna(size, prefix=""):
    if prefix:
        yield prefix
    for s in "ATGC":
        if size == 0:
            break
        yield from generate_dna(size - 1, prefix + s)


if __name__ == "__main__":
    print(list(generate_dna(4)))
