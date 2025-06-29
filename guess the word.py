
word = 'espresso' 
lives = 6

m = []
for k in word:
    m.append(k)    

blank = []
for o in range(len(m)):
    blank.append('_')

check = []
for uu in m:
    check.append(uu)

vv = -1

l = []
tryp = 1
ym = 1
crl = [0]
cr = 0
cc = 0
cv = []
while lives >= 0:
    qq = True
    guess = str(input('guess one alphabet for one of the letters in the word:--  '))
    print('\n\n')
    if len(guess) > 1 or len(guess) < 1:
        print('less or more than one alphabets guessed , try again ')
        continue

    for n in check:
        if guess == n:
            qq = True
            if guess in blank:
                ncount = m.count(n)
                vv = m.index(check.pop(check.index(n)))
                if 'crl_dict' not in locals():
                    crl_dict = {}
                if n not in crl_dict:
                    crl_dict[n] = [vv]
                if ncount <= 2:
                    try:
                        cc = m.index(n, vv + 1)
                        blank[cc] = n
                        print(' '.join(blank))
                        print('\n\n')
                    except ValueError:
                        pass
                    break
                elif ncount > 2:
                    for yy in range(1, ncount):
                        if yy < 2 and ym < 2:
                            try:
                                cc = m.index(n, vv + 1)
                                cv.append(str(cc))
                                blank[cc] = n
                                crl_dict[n].append(cc)
                                print(' '.join(blank))
                                print('\n\n')
                                ym += 1
                            except ValueError:
                                break
                            break
                        elif yy >= 2 and ym >= 2:
                            try:
                                last_idx = crl_dict[n][-1]
                                cr = m.index(n, last_idx + 1)
                                crl_dict[n].append(cr)
                                cv.append(cr)
                                blank[cr] = n
                                print(' '.join(blank))
                                print('\n\n')
                                ym += 1
                            except ValueError:
                                break
                            break
                    break

            else:
                cc = m.index(n)
                blank[cc] = n
                print(' '.join(blank))
                print('\n\n')
                m.index(check.pop(check.index(n)))
                break

        else:
            qq = False

    if qq == True:
        pass

    elif qq == False:
        lives -= 1
        if lives >= 1:
            print(f'wrong guess , one live lost , {lives} lives left \n\n\n')

        elif lives == 0:
            print('last live left !!')    

    answer = ''.join(m)
    guessl = ''.join(blank)
    tryp += 1
    if answer == guessl:
        print('you won!!!!!')
        break

answer = ''.join(m)    
guessl = ''.join(blank)    

if answer != guessl:
    print('unfortunatly you lost , better luck next time : ) ')