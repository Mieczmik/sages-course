# ZADANIE 17: napisz funkcję, która będzie przyjmowała napis,
# a zwracała jego elementy w odwrotnej kolejności np
# "pies je kiełbase'-> 'kiełbase je pies’

moj_napis = "pies je kiełbase"
# moj_napis.split() -> lista słow
# łączenie elementow listy w string -> " ".join()

#print(moj_napis.split())

def f(moj_napis):
    moj_napis = ' '.join(moj_napis.split()[::-1])
    return moj_napis

print(f(moj_napis))