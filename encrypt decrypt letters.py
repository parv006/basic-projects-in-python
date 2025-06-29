que=input('do you want to encrypt or decrypt? write e for encrypt and d for decrypt  : ')
def encrypt(word,shift):
    list1=[]
    for letters in word:
        letters=chr(ord(letters)+shift)
        list1.append(letters)
    shifted=''.join(list1)    
    print(shifted)
def decrypt(eword,eshift):
    list2=[]
    for eletters in eword:
        eletters=chr(ord(eletters)-eshift)
        list2.append(eletters)
    eshifted=''.join(list2)    
    print(eshifted)

if que=='e' or que=='E':
    word=input('type the word to be encrypted: ')
    shift=int(input('how much shift do you want : '))
    encrypt(word,shift)
elif que=='d' or que=='D':
    eword=input('input the encrypted word:  ')
    eshift=int(input('enter the shft : ' ))
    decrypt(eword,eshift)
else:
    print('invalid')    