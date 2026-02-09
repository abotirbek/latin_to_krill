text_latin = input("Lotinchadagi matn kiriting (w=ш, c=ч): ")
# sh, ch, g', Ketdik Ayiq Ovlashga
def latin_to_krill(data):
    letters = {
        'a':'а','b':'б','c':'с','d':'д','e':'е','f':'ф','g':'г','h':'х','i':'и','j':'ж','k':'к','l':'л','m':'м','n':'н',
        'o':'о','p':'п','q':'қ','r':'р','s':'с','t':'т','u':'у','v':'в','x':'х','y':'й','z':'з','w':'ш'
    }
    text_krill = ''
    for d in data:
        for k,v in letters.items():
            if not d in letters.keys():
                krill = d
            elif d == ' ':
                krill = d
            elif d == k:
                krill = d.replace(d,v)
            elif d == k.upper():
                krill = d.replace(d,v.upper())
        text_krill += krill

    return text_krill
print(latin_to_krill(text_latin))