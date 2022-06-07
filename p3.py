import sys

f = open(sys.argv[1],"r")

starts = set( [ "atg", "gtg" ])

for line in f:
    x = line.rstrip().lower
    id, str = x.split()
    for i in range(len(str)):
        if str[i:i+3] in starts:
            for j in range(len(str)):
                if str[j:j+3] == "tag":
                    if(j+3-i >=33 and j+3-i <= 99 and ((j+3-i) %3 == 0) ):
                        print(id, i, j+3-i, str[i:i+3], str[j:j+3])
                        break
