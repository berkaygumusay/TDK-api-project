import requests
def searchWord(Word):
    response = requests.get("https://sozluk.gov.tr/gts?ara="+Word,headers={
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br"
    })
    if response.status_code == 200:
        content = response.json()
        anlamlar = content[0].get("anlamlarListe")
        return {
            "found" : True,
            "anlamlar" : list(map(lambda anlam : anlam.get("anlam"),anlamlar))
        }
    return {
        "found" : False
    }
Word = input("Enter A Word : ")
result = searchWord(Word)
for i in result.values():
    if i != True and i != False:
        for j in i:
            print("-" + j)