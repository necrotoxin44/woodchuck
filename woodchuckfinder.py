import argparse


parser = argparse.ArgumentParser()
parser.add_argument("animal_file", help="file of animal names")
parser.add_argument("noun_file", help="file of nouns")
parser.add_argument("verb_file", help="file of verbs")
args=parser.parse_args()

try: #receive input files from command line
    with open(args.animal_file) as animal_file, open(args.noun_file) as noun_file, open(args.verb_file) as verb_file:
        #TODO: Ascertain that this code works by printing out first lines of each file
        #read each file into a list?
        for line in animal_file:
            print(line)
        for line in noun_file:
            print(line)
        for line in verb_file:
            print(line)
except OSError:
    sys.exit("file not found")

#for each line of animal_names, which is assumed to be a single name
    #search for noun in line
        #if noun found, sound for a following verbs
            #if verb also found, write line to woodchuck_animals.txt
