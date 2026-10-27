# vezerlőszerkezetek

def korszamlalas(kor):
    while kor < 65:
        kor += 1
        if kor == 52:
            continue
        print(kor)
        if kor == 55:
            break
    else:
        print('Nyugger')
    print('Vége')
    return kor


# programfutás
kor = 56
print('Nyugdíj: ', korszamlalas(kor))

felhasznalo_kora = 20  # int(input('Hány éves vagy: '))
if felhasznalo_kora < 18:
    print('gyerek')
elif felhasznalo_kora < 30:
    print('Ijfú')
elif felhasznalo_kora < 65:
    print('Felnőtt')
else:
    print('Nyugger')



