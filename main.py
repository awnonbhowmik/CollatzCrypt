from time import time

def encrypt(msg):
    ascii_lst=[ord(c) for c in msg]
    print(ascii_lst)

    def collatz_sequence(n):
        seq=[n]
        if n<1:
            return []
        while n>1:
            if n%2==0:
                n//=2
            else:
                n=3*n+1
            seq.append(n)
        
        bin_seq=[]
        for i in range(len(seq)):
            if seq[i]%2==0:
                bin_seq.append(0)
            else:
                bin_seq.append(1)

        def bin2dec(bin_lst):
            print("Sequence: {}".format(bin_lst))
            bin_lst.reverse()
            print("Reversed: {}".format(bin_lst))
            s=int("".join(str(x) for x in bin_lst),2)
            return s

        return bin2dec(bin_seq)


    for i in range(len(ascii_lst)):
        print(collatz_sequence(ascii_lst[i]))
        print("\n")

msg=input("Enter message:")
t1=time()
encrypt(msg)
print("Time to encrypt: {} seconds".format(time()-t1))