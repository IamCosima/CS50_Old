import csv
import sys
import re

#Redoing problem with regex due to seeing a discussion on it on the cs50 dna chat

def main():
# Handle command line arguments
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)


    # Stores names of the files
    database = sys.argv[1]
    Sequence = sys.argv[2]
    # lists
    STR_counter = {}
    # Sequence into mem
    with open(Sequence) as peoplefile:
        Seq = peoplefile.read()

    # Database into mem
    with open(database,newline='') as f:
        reader = csv.reader(f)
        headings = next(reader)

    counter = 0
    maxcount = 0

    #res = len(re.findall(headings,Seq ))
    res = seq.count(headings)
    #patterns = ['AGATC','TTTTTTCT','AATG','TCTAG','GATA','TATC','GAAA','TCTG']
    print(res)






# For each STR find the longest STR line using the sp
#for i in range(1, fieldname_length):
#    STR = reader.fieldnames[i]
#    max_counts.append(0)

    # Loop through sequence to find STR
#    for j in range(seq_length):
#        STR_count = 0

#        # If match found start counting repeats
#        if Seq[j:(j + len(STR))] == STR:
#            k = 0
#            while Seq[(j + k):(j + k + len(STR))] == STR:
#                STR_count += 1
#                k += len(STR)

                # If new maximum of repeats assign max_counts to new high
#            if STR_count > max_counts[i - 1]:
#                max_counts[i - 1] = STR_count

# Compare against data to see for match if faild no match is found
#for i in range(data_length):
#    matches = 0
#    for j in range(1, fieldname_length):
#        if int(max_counts[j - 1]) == int(data[i][reader.fieldnames[j]]):
#            matches += 1
#        if matches == (fieldname_length - 1):
#            print(data[i]['name'])
#   sys.exit(1)



print("No match")
main()

# note to self indentation breaks logic which leads to hours of debugging
# Use of better counter vars makes life easier(somehow it broken stuff)
# def main() figure out fix as to why it does not work