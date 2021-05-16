import sys 

# the input is cominng from STDIN 
for line in sys.stdin:
    line = line.strip() 
    # split the lines into words 
    words = line.split() 

    for word in words: 
        print(f"{word}\t{1}")

# the output format of mapper.py and expected format of reducer.py should match 
# sum the occurance of each word to final output and output its results to STDOUT 


