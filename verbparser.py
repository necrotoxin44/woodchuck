import csv

try:
    with open("dictionary.csv", newline='') as file, open("verbs.txt", "w+") as output:
        reader = csv.reader(file)
        previous = " "
        for str_list in reader:
            if ("v." in str_list[1] and "adv." not in str_list[1]):
                if(str_list[0] != previous):
                    output.write(str_list[0] + '\n')
                    previous = str_list[0]
except OSError:
    sys.exit("file not found")
