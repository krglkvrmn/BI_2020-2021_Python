class Sequence:
    """Class represents biological sequence"""
    def __init__(self, seq):
        if isinstance(seq, str):
            self._seq = seq.upper()
        else:
            raise TypeError("Sequence must be initialized with str like object")

    def gc_content(self):
        if type(self) == Sequence:
            raise NotImplementedError("Sequence object does not support gc_content")
        gc_set = {"G", "C"}
        gc_count = 0
        for nucl in self:
            if nucl in gc_set:
                gc_count += 1
        return gc_count / len(self)

    def complement(self):
        if type(self) == Sequence:
            raise NotImplementedError("Sequence object does not support complement")
        return type(self)(self._seq.translate(str.maketrans(self.COMPLEMENT_TABLE)))

    def reverse_complement(self):
        if type(self) == Sequence:
            raise NotImplementedError("Sequence object does not support reverse_complement")
        return self.complement()[::-1]

    def __iter__(self):
        for elem in self._seq:
            yield elem

    def __getitem__(self, slc):
        return type(self)(self._seq[slc])

    def __len__(self):
        return len(self._seq)

    def __hash__(self):
        return hash(self._seq)

    def __eq__(self, other):
        if self._seq == other._seq:
            return True
        else:
            return False

    def __add__(self, other):
        return type(self)(self._seq + other._seq)

    def __str__(self):
        return self._seq

    def __repr__(self):
        return f"{type(self).__name__}({self._seq})"


class DNA(Sequence):
    COMPLEMENT_TABLE = {"A": "T",
                        "T": "A",
                        "G": "C",
                        "C": "G"}
    ALPHABET = {"A", "T", "G", "C"}

    def __init__(self, seq):
        if set(seq.upper()) <= self.ALPHABET:
            super().__init__(seq)
        else:
            raise TypeError("Invalid alphabet for DNA")

    def transcribe(self):
        return RNA(self._seq.replace("T", "U")).complement()


class RNA(Sequence):
    COMPLEMENT_TABLE = {"A": "U",
                        "U": "A",
                        "G": "C",
                        "C": "G"}
    ALPHABET = {"A", "U", "G", "C"}

    def __init__(self, seq):
        if set(seq.upper()) <= self.ALPHABET:
            super().__init__(seq)
        else:
            raise TypeError("Invalid alphabet for RNA")
