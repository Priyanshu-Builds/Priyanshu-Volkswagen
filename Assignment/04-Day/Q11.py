key = {'a':'n','b':'o','c':'p','d':'q','e':'r','f':'s','g':'t','h':'u','i':'v','j':'w','k':'x','l':'y','m':'z',
'n':'a','o':'b','p':'c','q':'d','r':'e','s':'f','t':'g','u':'h','v':'i','w':'j','x':'k','y':'l','z':'m',
'A':'N','B':'O','C':'P','D':'Q','E':'R','F':'S','G':'T','H':'U','I':'V','J':'W','K':'X','L':'Y','M':'Z',
'N':'A','O':'B','P':'C','Q':'D','R':'E','S':'F','T':'G','U':'H','V':'I','W':'J','X':'K','Y':'L','Z':'M'}

message = input("Enter text to encode/decode using ROT-13: ")

converted = ""

for ch in message:
    if ch in key:
        converted += key[ch]
    else:
        converted += ch

print("Result after ROT-13 conversion:")
print(converted)

secret = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"
decoded = ""

for ch in secret:
    decoded += key.get(ch, ch)

print("\nDecoded secret message is:")
print(decoded)