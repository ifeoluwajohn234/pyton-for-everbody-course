#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the 
# string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
counts = dict()

for line in fh:
    if line.startswith('From ') :
        words = line.split()
        time = words[5]
        hours = time[:2]
        counts[hours] = counts.get(hours,0) + 1

for key, val in sorted(counts.items()):
    print (key, val)