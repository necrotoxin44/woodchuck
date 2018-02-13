import sys

try: #receive input files from command line

except OSError:
    sys.exit("files perhaps not found, format: py woodchuckfinder.py [animal_names].txt [nouns].txt [verbs].txt")

#for each line of animal_names, which is assumed to be a single name
    #search for noun in line
        #if noun found, sound for a following verbs
            #if verb also found, write line to woodchuck_animals.txt
