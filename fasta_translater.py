from Bio import SeqIO


def translated_fasta_reader(path, codon_table="Standard"):
    yield from map(lambda x: x.seq.translate(codon_table), SeqIO.parse(path, "fasta"))


if __name__ == "__main__":
    path = input("Enter path to nucleotide fasta file: ")
    for prot in translated_fasta_reader(path):
        print(prot)

