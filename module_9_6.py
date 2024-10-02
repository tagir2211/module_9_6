def all_variants(text):
    for i in range(len(text)):
        for j in range(len(text)):
            if i+j >= (len(text)):
                continue
            yield text[j:i+j+1]

f = all_variants('123')
for i in f:
    print(i)

