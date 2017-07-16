#print only the words that start with 's'

def print_s(st):
    l = st.split()
    for wor in l:
        if wor[0]=='s':
            print(wor)

st = 'Print only the words that start with s in this sentence'
print_s(st)

