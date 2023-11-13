
import os
os.system("cls")
def select(operator,kuota, price):
    if operator == "indosat":
        if kuota == "3gb":
            harga_bayar = price - 25000
            print(harga_bayar)
        elif kuota == "5gb":
            harga_bayar = price - 30000
            print(harga_bayar)
        elif kuota == "7gb":
            harga_bayar = price - 50000
            print(harga_bayar)
        elif kuota == "10gb":
            harga_bayar = price - 100000
            print(harga_bayar)
        else:
            print("juota tidak ada")
    elif operator == "telkomsel":
        if kuota == "3gb":
            harga_bayar = price - 35000
            print(harga_bayar)
        elif kuota == "5gb":
            harga_bayar = price - 40000
            print(harga_bayar)
        elif kuota == "7gb":
            harga_bayar = price - 60000
            print(harga_bayar)
        elif kuota == "10gb":
            harga_bayar = price - 120000
            print(harga_bayar)
        else:
            print("juota tidak ada")
    return harga_bayar

namaKonter = input("nama konter : ")
alamat = input("alamat")
print("-"*50)
nomor_hp = input("masukan nomor hp ")

while True:
    operator = input("masukan operator ")
    kuota = input("masukan kuota ")
    bayar = int(input("masukan nominal bayar "))

    select(operator, kuota, bayar)

    stop  = input("apakah ingin membeli lagib ?")
    if stop == "n":
        break