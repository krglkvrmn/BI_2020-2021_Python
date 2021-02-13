# Functional programming homework

These tasks are mainly focused on creation and usage of generators.

## Description

#### DNA sequence generator (generate_sequence.py)

*generate_dna(n)* is a generator that yields all possible DNA sequences of size *n*.

Example:

```python
>>> list(generate_dna(3))
['A', 'AA', 'AAA', 'AAT', 'AAG', 'AAC', 'AT', 'ATA', 'ATT', 'ATG', 'ATC', 'AG', 'AGA', 'AGT', 'AGG', 'AGC', 'AC', 'ACA', 'ACT', 'ACG', 'ACC', 'T', 'TA', 'TAA', 'TAT', 'TAG', 'TAC', 'TT', 'TTA', 'TTT', 'TTG', 'TTC', 'TG', 'TGA', 'TGT', 'TGG', 'TGC', 'TC', 'TCA', 'TCT', 'TCG', 'TCC', 'G', 'GA', 'GAA', 'GAT', 'GAG', 'GAC', 'GT', 'GTA', 'GTT', 'GTG', 'GTC', 'GG', 'GGA', 'GGT', 'GGG', 'GGC', 'GC', 'GCA', 'GCT', 'GCG', 'GCC', 'C', 'CA', 'CAA', 'CAT', 'CAG', 'CAC', 'CT', 'CTA', 'CTT', 'CTG', 'CTC', 'CG', 'CGA', 'CGT', 'CGG', 'CGC', 'CC', 'CCA', 'CCT', 'CCG', 'CCC']
```

#### Fasta file translater  (fasta_translater.py)

*translated_fasta_reader(path, codon_table)* is a generator that reads fasta record from nucleotide fasta file and yields corresponding amino-acid Seq object.

Example:

```python
>>> list(translated_fasta_reader("example.fna"))
[Seq('MPTASLHRSIEST'), Seq('RPHSLIAIYLCT'), Seq('HISLLLHTGLSIY')]
```

## Usage

### Download source code and install dependencies

```bash
git clone https://github.com/krglkvrmn/BI_2020-2021_Python.git
cd BI_2020-2021_Python
git checkout functional_homework
pip install -r requirements.txt
```