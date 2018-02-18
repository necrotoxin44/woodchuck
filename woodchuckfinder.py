import argparse
import sys
import time

parser = argparse.ArgumentParser()
parser.add_argument("animal_file", help="file of animal names")
parser.add_argument("noun_file", help="file of nouns")
parser.add_argument("verb_file", help="file of verbs")
args=parser.parse_args()
#optional argument for output file?
#print progress percentage?

try:
    total = 0
    with open(args.animal_file) as animal_file:#get animal_file length
        for animal in animal_file:
            total += 1

    start = time.time()
    with open(args.animal_file) as animal_file, open(args.noun_file) as noun_file, open(args.verb_file) as verb_file, open("woodchuckoutput.txt", "w+") as output:
        count = 0
        for animal in animal_file:
            a = (animal.strip()).lower()
            found = False
            for noun in noun_file:
                n = (noun.strip()).lower()
                if(n in a):
                    for verb in verb_file:
                        v = (verb.strip()).lower()
                        if(((n + v) in a.lower()) or ((n + ' ' + v) in a.lower())):
                            output.write(animal.strip() + '\n')
                            found = True
                            break
                    verb_file.seek(0)
                if(found):
                    break
            noun_file.seek(0)
            count += 1
            print("Progress: " + str(100 * (count/total)))
    end = time.time()
    print("Total elapsed time: " + str(end - start) + " seconds")


except OSError:
    sys.exit("file not found")
