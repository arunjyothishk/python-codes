
def translate(strs):
    vowels="AEIOUaeiou"
    trans=""
    for c in strs:
        for v in vowels:
            if c==v:
                l='q'
                if c.isupper():
                    c=l.upper()
                else:
                    c=l
                break
        trans+=c
    return trans

print(translate(input("Enter a Word:  ")))

