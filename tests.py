from calculate_protein_mass import calculate_prot_mass
from compute_gc import compute_gc
from counting_dna_nucleotides import counting_dna_nucleotides
from counting_point_mutations import counting_point_mutations
from dna_complement import dna_complement
from dna_to_rna import dna_to_rna
from enumerate_gene_orders import enumerate_gene_orders
from finding_motif_in_dna import finding_motif_in_dna
from finding_spliced_motif import find_spliced_motif
from locating_restriction_sites import locate_restriction_sites
from open_reading_frames import open_reading_frames
from rna_splicing import splice_rna
from transitions_and_transversions import transitions_and_transversions
from translate_rna_to_protein import translate_rna_to_prot

def test_calculate_protein_mass():
    seq = 'SKADYEK'

    assert round(calculate_prot_mass(seq), 3) == 821.392

def test_compute_gc():
    path = 'test_data/compute_gc.txt'

    with open(path, 'r') as f:
        data = f.readlines()

    subject, value = compute_gc(data)
    assert subject == 'Rosalind_0808'
    assert round(value, 6) == 60.919540

def test_counting_dna_nucleotides():
    seq = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

    counts = counting_dna_nucleotides(seq)

    assert counts['A'] == 20
    assert counts['C'] == 12
    assert counts['G'] == 17
    assert counts['T'] == 21

def test_point_mutations():
    a = 'GAGCCTACTAACGGGAT'
    b = 'CATCGTAATGACGGCCT'   

    assert counting_point_mutations(a, b) == 7

def test_dna_complement():
    seq = 'AAAACCCGGT'

    assert dna_complement(seq) == 'ACCGGGTTTT'

def test_dna_to_rna():
    seq = 'GATGGAACTTGACTACGTAAATT'
    
    assert dna_to_rna(seq) == 'GAUGGAACUUGACUACGUAAAUU'

def test_enumerate_gene_orders():
    length, orders = enumerate_gene_orders(3)

    assert length == 6
    assert orders == [(1,2,3), (1,3,2), (2,1,3),(2,3,1),(3,1,2),(3,2,1)]
    
def test_finding_motif_in_dna():
    a = 'GATATATGCATATACTT'
    b = 'ATAT'

    assert finding_motif_in_dna(a, b) == [2, 4, 10]

def test_finding_spliced_motif():
    a = 'ACGTACGTGACG'
    b = 'GTA'

    assert find_spliced_motif(a, b) == [3, 4, 5]

def test_locating_restriction_sites():
    seq = 'TCAATGCATGCGGGTCTATATGCAT'

    assert locate_restriction_sites(seq) == [(4, 6), (5, 4), (6, 6), (7, 4), (17, 4), (18, 4), (21, 4)]
def test_open_reading_frames():
    seq = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'

    rna_seq = dna_to_rna(seq)
    reverse_complement = dna_to_rna(dna_complement(seq))

    forward = open_reading_frames(rna_seq)
    backward = open_reading_frames(reverse_complement)
    
    assert set(forward + backward) == set(['MLLGSFRLIPKETLIQVAGSSPCNLS','M','MGMTPRLGLESLLE', 'MTPRLGLESLLE'])

def test_rna_splicing():
    seq = 'ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG'
    introns = ['ATCGGTCGAA', 'ATCGGTCGAGCGTGT']

    assert splice_rna(seq, introns) == 'MVYIADKQHVASREAYGHMFKVCA'

def test_transitions_and_transversions():
    seq1 = 'GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT'
    seq2 = 'TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT'

    assert round(transitions_and_transversions(seq1, seq2), 3) == 1.214

def test_rna_to_protein():
    seq = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'

    assert translate_rna_to_prot(seq) == 'MAMAPRTEINSTRING'