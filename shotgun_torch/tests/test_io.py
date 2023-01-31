from shotgun_torch._io import parse_sequence_file, parse_fasta, parse_fastq
import unittest
import io
import tempfile


class IOTests(unittest.TestCase):
    def test_parse_fasta(self):
        data = io.StringIO(">foo\nAATTGG\n>bar\nGGCC")
        exp = ['AATTGG', 'GGCC']
        obs = list(parse_fasta(data))

    def test_parse_fastq(self):
        data = io.StringIO("@foo\nAATTGG\n+\nIIIIII\n@bar\nGGCC\n+\nHHHH")
        exp = ['AATTGG', 'GGCC']
        obs = list(parse_fastq(data))

    def test_parse_sequence_file(self):
        with tempfile.TemporaryDirectory() as d:
            with open(d + '/foo.fasta', 'w') as fp:
                fp.write(">foo\nAATTGG\n>bar\nGGCC")
            exp = ['AATTGG', 'GGCC']
            obs = list(parse_sequence_file(d + '/foo.fasta'))


if __name__ == '__main__':
    unittest.main()
