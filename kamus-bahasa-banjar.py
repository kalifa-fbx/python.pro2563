banjar = {"cantik":"bungas", "kamu":"ikam", "aku":"ulun", "ikan":""}
word = input()

if word in banjar.keys():
    print(banjar[word]) 

else:
    print("kata ini tidak ada di kamus kami")
