import argparse

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
        total_animals = file_len(animal_file)
        count = 0
        for animal in animal_file:
            a = (animal.strip()).lower()
            for noun in noun_file:
                n = (noun.strip()).lower()
                if(n in a):
                    for verb in verb_file:
                        v = (verb.strip()).lower()
                        if(((n + v) in a.lower()) or ((n + ' ' + v) in a.lower())):
                            print(a)
                            output.write(a + '\n')
                    verb_file.seek(0)
            noun_file.seek(0)
            count += 1

            print("Percentage: " + str(round(100 * (count/total_animals))) + '\n')

except OSError:
    sys.exit("file not found")
