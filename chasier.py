from transaction import *
import pandas as pd

print('Hi Pelanggan! Selamat Datang di Kasir Otomatis')
print('==============================================')

nama = input('Silahkan Masukkan Nama Anda: ')
transaksi = Transaksi(nama)

while(True): # Pilihan untuk action users
    print('Silahkan pilih proses transaksi anda')
    print('1. Tambahkan Item')
    print('2. Memperbarui Item')
    print('3. Menghapus Item')
    print('4. Check Item')
    print('5. Total Belanja')

    process = input('Masukkan nomor proses yang ingin anda lakukan:')

    if process == '1':
        #proses add item
        while(True):
                nama_item = input('Masukan Nama Item = ')
                if nama_item.strip():
                    break
                print('Pastikan item anda telah diinput dan tidak kosong')
        while(True):
            try:
                quantity = int(input('Masukkan Jumlah Item dalam format number = '))
                break
            except ValueError:
                print('Pastikan Jumlah Item diinput menggunakan format Number')
        while(True):
            try:
                harga_item = int(input('Masukkan Harga per Item dalam format number (cth: 5000) = '))
                break
            except ValueError:
                print('Pastikan Harga per Item diinput menggunakan format Number')
        transaksi.add_item(nama_item, quantity, harga_item)

    elif process == '2':
        #proses update item
        while(True):
            update = input('Apa yang ingin anda update? Masukkan nomor pilihan anda (1.Nama Item/2.Jumlah Item/3.Harga Item/4.Stop)')

            if update == '1':
                #update item name
                while(True):
                    try:
                        nama_item = input('Masukkan nama item yang ingin diupdate:')
                        new_item_name = input('Masukkan nama item yang baru:')
                        if new_item_name.strip():
                            transaksi.update_item_name(nama_item, new_item_name)
                            break
                    except KeyError:
                        print('Pastikan item yang ingin anda update tersedia dikeranjang atau inputan baru tidak boleh kosong') 
                    break

            elif update == '2':
                #update quantity
                while(True):
                    try:
                        nama_item = input('Masukkan nama item yang ingin diupdate:')
                        while(True):
                            try:
                                new_qty = int(input('Masukkan jumlah item yang baru:'))
                                break
                            except ValueError:
                                print('Anda belum memasukkan jumlah item yang baru, pastikan masukkan tidak kosong')
                        transaksi.update_item_qty(nama_item, new_qty)
                        break
                    except KeyError:
                        print('Nama item yang anda input salah, Pastikan format nama item sesuai atau tambahkan item anda terlebih dahulu')
                    break


            elif update == '3':
                #update harga item
                while(True):
                    try:
                        nama_item = input('Masukkan nama item yang ingin diupdate:')
                        while(True):
                            try:
                                new_harga_item = int(input('Masukkan harga item yang baru:'))
                                break
                            except ValueError:
                                print('Anda belum memasukkan harga item yang baru, pastikan masukkan tidak kosong')
                        transaksi.update_item_price(nama_item, new_harga_item)
                        break
                    except KeyError:
                        print('Nama item yang anda input salah, Pastikan format nama item sesuai atau tambahkan item anda terlebih dahulu')
                    break

            elif update == '4':
                # stop proses update
                jawab = input('Apakah anda yakin untuk menghentikan proses update? (Yes/No)') 
                if jawab == 'No':
                    print('Kembali ke proses update')
                elif jawab == 'Yes':
                    break
                else:
                    print('Masukan anda tidak sesuai!, Proses update berhenti secara paksa')
                    break
            else:
                #Stop apabila user masukkan value yang lain
                print('Masukkan anda tidak sesuai!, pastikan memasukkan pilihan sesuai petunjuk jawaban')
    elif process == '3':
        #proses menghapus item
        while(True):
            hapus = input('Apakah Anda ingin menghapus semua item? (Yes/No/Batal Menghapus)')
            if hapus == 'No':
                #delete per item
                try:
                    hapus_item = input('Masukkan item yang ingin anda hapus: ') 
                    transaksi.delete_item(hapus_item)
                    break
                except KeyError:
                    print('Item yang ingin anda hapus tidak tersedia di keranjang anda!')
                    break
                break
            elif hapus == 'Yes':
                #reset semua item
                transaksi.reset_transaction()
                break
            elif hapus == 'Batal Menghapus':
                #User tidak jadi menghapus
                print('Anda kembali ke menu utama')
                break
            else:
                #Ulangi jika user salah masukkan
                print('Masukan anda tidak sesuai!, pastikan memasukkan pilihan sesuai petunjuk jawaban ')

    elif process == '4':
        #proses check order
        transaksi.check_order() 

    elif process == '5':
        #proses untuk liat total belanja dan total cost
        transaksi.total_price()
        
        answ = input('Apakah Anda masih ingin menambahkan Item? (Yes/No)')
        if answ == 'Yes':
            print('Silahkan tambahkan item anda mengikuti petunjuk')
        elif answ == 'No':
            transaksi.total_cost()
            print('Silahkan Lakukan Pembayaran')
            print('Terima Kasih!')
            break
        else:
            print('Masukan anda tidak sesuai!, Kembali ke menu awal')

    else:
        #Jika user salah masukkan kembali ke pilihan awal
        print('Permintaan anda tidak dapat diproses!, Silahkan masukkan nomor proses yang anda inginkan dengan benar')
        


