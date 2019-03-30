# woodchuck

Contains a Python program to search for 'woodchuck' animals, and the datasets I used.
Essentially it uses files of nouns and verbs to search through a file of animal names
in order to find animal names containing a noun + verb combination (Hence, wood + chuck names).

I have lost the original source of my dictionary, but the animal names were gained from animals' English vernacular names in files from the [Integrated Taxinomic Information System](https://www.itis.gov/). The compiled list of animal names includes everything remotely interesting (almost the entire subphyllum Vertebrata, if I remember correctly).

## Setup

To set up locally, clone the repo with: `$ git clone https://github.com/necrotoxin44/woodchuck.git`

## Usage

It can be run right away with: `py woodchuckfinder.py animals.txt nouns.txt verbs.txt output.txt`

If you wish to supply your own lists, they should be text files formatted so the each each unit (an animal name or a word) is delimited by a newline. The noun and verb lists will be complete enough, so for these that should not be necessary.

In order to construct a new list of animal names from ITIS files, run: `py animal_parser.py input output` where input is a file or directory path containing ITIS files, and output is the name of the desired output text file. You could do this to see if there are any interesting woodchuck names in other taxonomies, such as in Plantae—I will warn you though, exploring taxonomies can open up a new world of unsettling creatures.
