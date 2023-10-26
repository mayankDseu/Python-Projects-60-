user=input('Enter the Phrase: ')
txt= user.split()
let= " "

for i in txt:
    let= let +str(i[0]).upper()
print(let)