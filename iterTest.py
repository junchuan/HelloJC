def integers():
    i=1
    while True:
        yield i
        i=i+1

def squares():
    for i in integers():
        yield i*i


def taken(n,seq):
    seq=iter(seq)
    result=[]
    try:
        for i in range(n):
            result.append(seq.next())
    except StopIteration:
        pass
    return result

if __name__=="__main__":
	taken(5,[1,2,3,4,5])
