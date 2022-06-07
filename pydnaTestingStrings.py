import sys

#f = open(sys.argv[1],"r")

starts = set( [ "atg", "gtg" ])

test = "0_33    AtG___________________________TaG"
test1 = "seq01  xxxatgxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxtagxxx"
test2 = "myseq   xgtgxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxtagxxxxxxxx"
x = test.rstrip().lower()
id, str = x.split()
for i in range(len(str)):
    if str[i:i+3] in starts:
        for j in range(len(str)):
            if str[j:j+3] == "tag":
                if(j+3-i >=33 and j+3-i <= 99 and ((j+3-i) %3 == 0) ):
                    print(id, i, j+3-i, str[i:i+3], str[j:j+3])
                    break
                    
x = test1.rstrip().lower()
id, str = x.split()
for i in range(len(str)):
    if str[i:i+3] in starts:
        for j in range(len(str)):
            if str[j:j+3] == "tag":
                if(j+3-i >=33 and j+3-i <= 99 and ((j+3-i) %3 == 0) ):
                    print(id, i, j+3-i, str[i:i+3], str[j:j+3])
                    break
                    
x = test2.rstrip().lower()
id, str = x.split()
for i in range(len(str)):
    if str[i:i+3] in starts:
        for j in range(len(str)):
            if str[j:j+3] == "tag":
                if(j+3-i >=33 and j+3-i <= 99 and ((j+3-i) %3 == 0) ):
                    print(id, i, j+3-i, str[i:i+3], str[j:j+3])
                    break
