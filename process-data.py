import glob
import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import pandas as pd

#input_dir = "YELL_052-M-23-7-20180711-GEN-DNA1_16S_20211117T003043.csv"
input_dir = "/work/adina/millican/neon/comm-16s"
test_file = "/work/adina/millican/neon/comm-16s/YELL_052-M-23-7-20180711-GEN-DNA1_16S_20211117T003043.csv"
asv_dict = {}
tax_dict = {}
seq_rec = []
with open(test_file, 'r') as f:
    for line in f:
        if line.startswith("dnaSampleID"):
            continue
        line = line.strip().split(",")
        sampleID = line[0]
        seqName = line[2]
        asv = line[3]
        domain = line[5]
        phylum = line[7]
        _class = line[8]
        order = line[9]
        family = line[10]
        genus = line[11]
        species = line[12]
        org_name = line[13]
        count = line[14]
        asv_dict[sampleID] = {asv: count}
        tax_dict[asv] = {'domain': domain, 'phylum': phylum, 'class': _class, 'order': order, 'family': family, 'genus': genus, 'species': species, 'organism': org_name}
        seq_rec.append(SeqRecord(Seq(asv), id=f"{sampleID}|{seqName}", description=""))
