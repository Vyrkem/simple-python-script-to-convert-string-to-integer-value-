string = "ast15605.ced.clo"

string = string.upper();
arr= []
stringAscii = ""
print("int      HEX \n")

for i in string:
    print("%i       0x%x"%(ord(i), ord(i)))
    arr.append(ord(i))
for i in arr:
    stringAscii+=(str(i)+".")
    
stringAscii= stringAscii[:-1]
print("\n")
print("raw")
print(string+"\n")
print("ascii")
print(stringAscii+"\n")

print( "string lenght: %i"%len(string))