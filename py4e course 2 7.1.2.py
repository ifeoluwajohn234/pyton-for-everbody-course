# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0 
for line in fh:
    if  line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        number = line.find("0")
        full_num = line[number:]
        new_nums = float(full_num)
        total = total + new_nums
        calc_avg = total/count
        
        
print("Average spam confidence:",calc_a)
