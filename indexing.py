word='artificial intelligence'
print(word[:10])
print(word[11:])

print(word[:-13])
print(word[-12:])

print(word[0].upper() + word[1:-1] + word[-1].upper())

source=input('write ur text:\n')
fix=int(input('type the number of letter u wanna change:\n'))
new=input('type the new leter u wanna put:\n')
#i put fix-1 because the user will not start the counting from 0
print(source[:fix-1] + new + source[fix:])

for i in range(1,len(source), 2):
    print(source[i])
for i in range(0,len(source), 2):
    print(source[i])
print(source[-3:])