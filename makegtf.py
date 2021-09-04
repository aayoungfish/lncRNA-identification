import sys
import argparse
import os


def MakeGTF(input_file,output_dir,ref_file):
    a = []
    with open (input_file) as f_in:
        for line in f_in:
            s = line.split('\t')[3]   #提取文件第三列
            a.append(s)
        #print(a)
    
    out_dir = os.getcwd()
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)	
    f_out = open('filter.gtf', mode ='w', encoding ='utf-8')
	
    with open(ref_file) as f_ref:
        for line in f_ref:
            line = line.replace('\n',"")
            line1 = line.strip().split("\"") #分成9列
			
            try:
                gene_Name = line1[1]
            except:
                continue
            #print(gene_Name)
			
            if gene_Name in a:
                #print(line)
                f_out.write(line + '\n')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This is the script for tmap annotation file to the gtf file \
                                                  which gffcompare need")
    parser.add_argument('-i', '--input_file', required=True,
                        help='<filepath>  The tmap annotation file')
    parser.add_argument('-r', '--ref_file', required=True,
                        help='<filepath>  The  ref_merged.gtf file')					
    parser.add_argument('-o', '--output_dir', required=True,
                        help='<dirpath>  the directory for results')
    args = parser.parse_args()
    MakeGTF(args.input_file,args.output_dir,args.ref_file)        
