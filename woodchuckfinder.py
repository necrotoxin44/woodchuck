import argparse
import sys
import time

parser = argparse.ArgumentParser()
parser.add_argument("animal_file", help="file of animal names")
parser.add_argument("noun_file", help="file of nouns")
parser.add_argument("verb_file", help="file of verbs")
parser.add_argument("output_file", help="file to output 'woodchuck' names to")
args=parser.parse_args()

#progress display function courtesy of vladignatyev
def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
sys.stdout.flush()

try:
    total = 0
    #get animal_file's line count
    with open(args.animal_file) as animal_file:
        for animal in animal_file:
            total += 1

    start = time.time()
    with open(args.animal_file) as animal_file, open(args.noun_file) as noun_file, open(args.verb_file) as verb_file, open(args.output_file, "w+") as output:
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
                #break before found again and duplicates added
                if(found):
                    break
            noun_file.seek(0)
            count += 1
            progress(count,total, 'search progress')
    end = time.time()
    print("Total elapsed time: " + str(end - start) + " seconds")


except OSError:
    sys.exit("file not found")
