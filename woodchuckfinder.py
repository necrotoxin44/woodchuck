import argparse


parser = argparse.ArgumentParser()
parser.add_argument("animal_file", help="file of animal names")
parser.add_argument("noun_file", help="file of nouns")
parser.add_argument("verb_file", help="file of verbs")
args=parser.parse_args()
#optional argument for output file?
try: #receive input files from command line
    with open(args.animal_file) as animal_file, open(args.noun_file) as noun_file, open(args.verb_file) as verb_file, open("woodchuckoutput.txt", "w+") as output:
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

except OSError:
    sys.exit("file not found")
