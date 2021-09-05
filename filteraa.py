import argparse
import os
import re

def filteraa(input_file,output_dir,ref_file):
    with open (input_file) as f_in:
        txt = f_in.read()
        m = re.findall(r'STRG\.\d+\.\d+',txt)
        n = set(m)
        l = list(n)
        #print (l)
	
    out_dir = os.getcwd()
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)	
    f_out = open('filteraa.fa', mode ='w', encoding ='utf-8')
	
    seq = {}
    sequence = ""
    with open(ref_file) as f_ref:
        for line in f_ref:
            if line.startswith(">"):
                name = line[1:].rstrip()
                seq[name] = ""
                continue
            seq[name] += line.rstrip().upper()
        for k,v in seq.items():
            if k in l:
                continue
            f_out.write('>' + k + '\n' + v + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This is the script for fa_file to filter \
                                                  which gffcompare need")
    parser.add_argument('-i', '--input_file', required=True,
                        help='<filepath>  The orf file which have been predited using getorf')
    parser.add_argument('-r', '--ref_file', required=True,
                        help='<filepath>  The original fa_file U choose to filter')
    parser.add_argument('-o', '--output_dir', required=True,
                        help='<dirpath>  the directory for results')
    args = parser.parse_args()
    filteraa(args.input_file,args.output_dir,args.ref_file)
	
