from Crypto.Util.number import bytes_to_long
flag= b"dam{dat_was_ez}"
hidden = b"https://youtu.be/dQw4w9WgXcQ"
ha = b""
def bruh(hidden):
 aa=[]
 for i in hidden:
    if i%2!=0:
        aa+=[i^42]
    else:
        aa+=[i^68]
 return aa
ch = bruh(hidden)
ct = bruh(flag)
print(20*3,31*3)
mail = b"thrypuro@sigint.mx"
print(hex(bytes_to_long(mail))[2:])