def read(list):
    n = int(input("Dimensiune lista: "))
    for i in range(0, n, 1):
        list.append(int(input("Itroduceti un element: ")))


def numara_elementele_pare(list):
    k = 0
    for i in range(0,len(list),1):
        if list[i] % 2 == 0:
            k = k + 1
    return k

def intersectia_listelor(list1,list2):
    list_intersectie = []
    for i in range(0,len(list1),1):
        for j in range(0,len(list2),1):
            if list1[i] == list2[j]:
                list_intersectie.append(list1[i])
    return list_intersectie
def concatenare_elemente_palindrom(list1,list2):
    list_con = []
    palindrom = []
    if len(list1) > len(list2):
        k = len(list1)
    else:
        k = len(list2)
    for i in range(0,k,1):
        a = list1[i]
        b = list2[i]
        x = 0
        while b != 0:
            b = b // 10
            x = x + 1
        for j in range(1,x,1):
            a = a * 10
        a = a + list2[i]
        list_con.append(a)
    for i in range(0,len(list_con),1):
        oglindit = oglindit_element(list_con[i])
        if oglindit == list_con[i]:
            palindrom.append(list_con[i]
    )
    return palindrom
def oglindit_element(x):
    while x != 0:
        c = x % 10
        oglindit = oglindit * 10 + c
        x = x // 10
    return oglindit
def inlocuire_elemente_cu_oglinditul(list,list3):
    for i in range(0,len(list),1):
        k = 1
        for j in range(0,len(list3),1):
            if list[i] % list3[j] != 0:
                k = 0
        if k == 1:
            list[i] = oglindit_element(list[i])
    return list
def print_lista(list):
    for i in range(0, len(list), 1):
        print(list[i])
def main():
    list1 = []
    list2 = []
    list3 =[]
    while True:
        print('1. Citirea a două mulțimi de numere întregi de la tastatura sub forma a două liste.')
        print('2. Afișați dacă cele două liste au același număr de elemente pare.')
        print('3. Intersecția listelor.')
        print('4. Afișați toate palindroamele obținute prin concatenarea elementelor de pe aceleași poziții în cele două liste.')
        print('5. Oglinditul elementelor')
        print('6. Exit')
        opt = input('Alegeti optiunea: ')
        if opt == '1':
            read(list1)
            read(list2)
        elif opt == '2':
            if numara_elementele_pare(list1) == numara_elementele_pare(list2):
                print('Listele au acelasi numar de elemente pare')
            else:
                print('Listele nu au acelasi numar de elemente pare')
        elif opt == '3':
            print_lista(intersectia_listelor(list1,list2))
        elif opt == '4':
            print_lista(concatenare_elemente_palindrom(list1,list2))
        elif opt == '5':
            read(list3)
            print(inlocuire_elemente_cu_oglinditul(list1,list3))
            print(inlocuire_elemente_cu_oglinditul(list2,list3))
        elif opt == '6':
            break
        else:
            print('Optiune invalida. Incercati din nou.')
main()