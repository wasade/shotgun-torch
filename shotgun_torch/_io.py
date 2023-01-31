import skbio
import re


is_fasta = re.compile(r'.*\.fna\.gz$|.*\.fna$|.*\.fasta$|.*\.fasta.gz$')
is_fastq = re.compile(r'.*\.fq.gz$|.*\.fastq$|.*\.fq$|.*\.fastq.gz$')


def parse_sequence_file(fp):
    if is_fasta.match(fp):
        return parse_fasta(fp)
    elif is_fastq.match(fp):
        return parse_fastq(fp)
    else:
        raise ValueError("Unknown filetype")


def parse_fasta(fp):
    for rec in skbio.read(fp, format='fasta'):
        yield str(rec)


def parse_fastq(fp):
    for rec in skbio.read(fp, format='fastq', phred_offset=33):
        yield str(rec)
