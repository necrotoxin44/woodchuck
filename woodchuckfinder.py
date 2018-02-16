import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("animal_file", help="file of animal names")
parser.add_argument("noun_file", help="file of nouns")
parser.add_argument("verb_file", help="file of verbs")
args=parser.parse_args()
#optional argument for output file?
#print progress percentage?

def file_len(file):
    file.seek(0)
    line_count = 0
    for line in file:
        line_count += 1
    file.seek(0)
    return line_count

try:
    with open(args.animal_file) as animal_file, open(args.noun_file) as noun_file, open(args.verb_file) as verb_file, open("woodchuckoutput.txt", "w+") as output:
        perc_per_loop = 100 * (1 / file_len(noun_file))
        curr_count = 0
        start = time.time()
        for noun in noun_file:
            n = (noun.strip()).lower()
            for verb in verb_file:
                v = (verb.strip()).lower()
                for animal in animal_file:
                    a = animal.strip()
                    if(((n + v) in a.lower()) or ((n + ' ' + v) in a.lower())):
                        print(a)
                        output.write(a + '\n')
                animal_file.seek(0)
            verb_file.seek(0)
            curr_count += 1
            end = time.time()
            print(str(perc_per_loop / (end - start)) + " %/sec")
            start = time.time()

except OSError:
    sys.exit("file not found")
