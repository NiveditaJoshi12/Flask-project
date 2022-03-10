text='''heloo

nxjcnod'''

analyzed1=text
for char in text:
    if char == "\n" :
        analyzed1.replace(char," ")
    text= analyzed1
    print(analyzed1)