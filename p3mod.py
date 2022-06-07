starts = set(["atg", "gtg"])

def find_starts():
    t=()
    l=[]
    while True:
        seq = yield t
        for i in range(len(seq)):
            if seq[i:i+3] in starts:
                l.append((seq[i:i+3],i))
        t =tuple(l)
        l.clear()
