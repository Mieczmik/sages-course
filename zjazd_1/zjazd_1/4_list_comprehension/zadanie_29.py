# Znajdź wszystkie słowa,
# które sa krótsze niz 4 w napisie:
napis = "to jest moj super napis"

def f1(napis):
    return [x for x in napis.split() if len(x) < 4]

print(f1(napis))


