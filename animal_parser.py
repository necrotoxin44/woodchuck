import csv
import argparse
import sys
import queue
import pathlib

parser = argparse.ArgumentParser()
parser.add_argument("animals", help="a directory or file of ITIS animal taxonomy csv files")
parser.add_argument("output", help="output file to append to")
args = parser.parse_args()

#extracts only the vernacular names from ITIS csv file
def parse_and_append(input_path, output_file):
    try:
        with input_path.open(newline='') as file, open(output_file, "a") as output:
            reader = csv.reader(file, delimiter='|')
            previous = " "
            for str_list in reader:
                #check is an English vernacular name
                if(("[VR]" in str_list[0]) and ("English" in str_list[5])):
                    print(str_list[3])
                    output.write(str(str_list[3]) + '\n')
    except OSError:
        sys.exit("file not found")

q = queue.Queue()
path = pathlib.Path(args.animals)
q.put(path)

#empty the file for appending
with open(args.output, 'w'):
    pass

while(not q.empty()):
    curr = q.get_nowait()
    #if dir, add to queue to be explored
    if(curr.is_dir()):
        #enqueue its children
        for child in curr.iterdir():
            q.put(child)
    #if file, append vernacular names to output
    elif(curr.is_file()):
        parse_and_append(curr, args.output)
