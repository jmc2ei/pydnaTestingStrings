def find_starts(n):
    starts = set(["atg", "gtg"])
    while True:
        line = yield
        t =()
        l=list(t)
        for i in range(len(line)):
            if line[i:i+3] in starts:
                l.append((line[i:i+3], i))
        t=tuple(l)
        print(t)
        yield t

    

seq = 'catgccccgtgaaaa'
seqid = 's1'


gen = find_starts('hi')
print(gen)
gen.send(None)

startsAndLocs=gen.send(seq)

print("startAndLocs is : ",startsAndLocs)
print(seqid, ' '.join( (str(sal) for sal in startsAndLocs) ) )
gen.close()
#import sys

#import p3mod

#gen = p3mod.find_starts()
#gen.send(None)   # prime the generator

#with open(sys.argv[1]) as f:
#   for line in f:
#       (seqid,seq) = line.strip().lower().split()
#       startsAndLocs = gen.send(seq)   ### all vals for one line are returned at once
#       print(seqid, ' '.join( (str(sal) for sal in startsAndLocs) ) )

#gen.close()
