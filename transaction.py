import pandas as pd
class Transaksi(): #Objek class 
    def __init__(self, nama):
        '''Fungsi inisialisasi awal untuk inputan attribusi dari class.
        
        Attribute/Parameters:

        nama (string): nama user
        keranjang (dict): nantinya akan berisikan item -item yang akan diinput oleh user melalui fungsi add_item
        harga_belanja (dict): berisikan kalkulasi harga jumlah masing-masing item. Attribute ini dimanfaatkan untuk kalkulasi total akhir (total price dan total cost)

        '''
        self.nama = nama
        self.keranjang = {}
        self.harga_belanja = {}

    def add_item(self, nama_item, quantity, harga_item):
        '''Fungsi yang digunakan untuk menambahkan item-item yang ingin diinputkan oleh user.

        Attribute/Parameters:

        nama_item (string): nama item yang akan dimasukkan ke keranjang belanja
        quantitiy (int): jumlah item 
        harga_item (int): harga per item
        total (int): hasil kali quantity dan harga item. Attribute ini dimanfaatkan untuk tampil nantinya pada tabel melalui fungsi check_order
       
        Print:
        Tampilkan informasi bahwa item telah diinput ke keranjang
        '''
        self.total = quantity*harga_item
        self.keranjang.update({nama_item:[quantity,harga_item,self.total]})
        self.harga_belanja.update({nama_item:quantity*harga_item})
        print(f'Anda telah memasukkan {nama_item} sejumlah {quantity} ke keranjang dengan harga per item Rp. {harga_item} ')

    def update_item_name(self, nama_item, new_item_name):
        '''Fungsi yang digunakan untuk memperbarui nama item.

        Attribute/Parameters:

        nama_item (string): nama item yang telah dimasukan sebelumnya. Pastikan nama item yang ingin diganti sama persis dinputkan pada parameters ini
        new_item_name (string): nama item baru yang akan menggantikan nama item sebelumnya
        
        Print:
        Tampilkan informasi bahwa nama item berhasil diperbarui
        '''
        temp = self.keranjang[nama_item]
        self.keranjang.pop(nama_item)
        self.keranjang.update({new_item_name: temp})
        self.harga_belanja.pop(nama_item)
        self.harga_belanja.update({new_item_name:self.keranjang[new_item_name][0]*self.keranjang[new_item_name][1] })
        print(f'Nama item berhasil diperbarui menjadi {new_item_name}')

    def update_item_qty(self,nama_item,qty_new):
        '''Fungsi yang digunakan untuk memperbarui jumlah item.

        Attribute/Parameters:

        nama_item (string): nama item yang telah dimasukan sebelumnya atau yang telah diperbarui (latest)
        qty_new (int): jumlah item baru yang akan menggantikan jumlah item sebelumnya

        Print:
        Tampilkan informasi jumlah item berhasil diperbarui sesuai item masing-masing
        '''
        self.keranjang[nama_item][0] = qty_new
        self.keranjang[nama_item][2] = qty_new*self.keranjang[nama_item][1]
        self.harga_belanja[nama_item] = self.keranjang[nama_item][0]*self.keranjang[nama_item][1]
        print(f'Jumlah {nama_item} berhasil diperbarui menjadi {qty_new}')

        
    def update_item_price(self,nama_item,new_price):
        '''Fungsi yang digunakan untuk memperbarui harga item.

        Attribute/Parameters:
        nama_item (string): nama item yang telah dimasukan sebelumnya atau yang telah diperbarui (latest)
        new_price (int): harga item yang akan menggantikan harga item sebelumnya

        Print:
        Tampilkan informasi harga item berhasil diperbarui sesuai item masing-masing
        '''
        self.keranjang[nama_item][1] = new_price
        self.keranjang[nama_item][2] = self.keranjang[nama_item][0]*new_price
        self.harga_belanja[nama_item] = self.keranjang[nama_item][0]*self.keranjang[nama_item][1]
        print(f'Harga {nama_item} berhasil diperbarui menjadi Rp. {new_price}')

    
    def delete_item(self, nama_item):
        ''' Fungsi untuk mengeluarkan salah satu item dari dalam keranjang.

        Attribute/Parameters:
        nama_item (string): nama item yang akan dihapus dari keranjang

        Print:
        Tampilkan bahwa item telah berhasil dikeluarkan dari keranjang
        '''
        self.keranjang.pop(nama_item)
        print(f'{nama_item} telah dihapus dari keranjang')

    def reset_transaction(self):
        ''' Fungsi untuk mengeluarkan/ menghapus seluruh item di dalam keranjang.

        Print:
        Tampilkan reset telah berhasil dilakukan
        '''
        self.keranjang.clear()
        print(f'Reset berhasil dilakukan, semua item anda telah dihapus dari keranjang')

    def check_order(self):
        ''' Fungsi untuk memeriksa apakah masing-masing item telah memiliki value yang benar.

        Untuk tampilkan table pastikan telah install "to_markdown" (pip install tabluate)

        Print:
        1. Terdapat 3 kondisi:
            - Jika terdapat value yang masih bernilai nol, Infokan nama item yang belum benar tersebut
            - Jika value sudah benar, tampilkan informasi bahwa item sudah benar
            - Jika belum ada item yang dimasukkan maka infokan keranjang masih kosong
        2. Tabel order dan beberapa keterangannya
        '''
        try:
            keranjang_belanja = pd.DataFrame(self.keranjang).T # untuk create table order
            keranjang_belanja.columns = ['Jumlah Item','Harga per Item','Harga Belanjaan']
            print('Pastikan seluruh item anda sudah benar sebelum melanjutkan transaksi!')
            print('Silahkan cek dibawah ini:') 
            for item, value in self.keranjang.items():
                if value[0] == 0 or value[1] == 0:
                    print(f'============> Terdapat Kesalahan input pada Item {item}!')
                    print('Note: Harga dan Jumlah Item tidak boleh = 0')
               
                else:
                    print(f'============> Item {item} Sudah Benar')
            
            print(f'Pesanan {self.nama} sebagai berikut:')       
            print(keranjang_belanja.to_markdown())
            
        except ValueError:
            print('Keranjang Anda Masih Kosong')

    def total_price(self):
        ''' Fungsi untuk menghitung total price dari item yang telah ditambahkan di keranjang

        Print:
        1. Ketika item belum ditambahakn infokan keranjang masih kosong
        2. Ketika item telah ditambahkan tampilkan total price 
        '''
        self.total_belanja = sum(self.harga_belanja.values())
        if self.total_belanja == 0:
            print('Keranjang Anda Masih Kosong')
        else:
            print(f'Total Belanja seluruh item anda adalah Rp {self.total_belanja}')

    def total_cost(self):
        ''' Fungsi untuk menghitung total bayar dari item yang telah ditambahkan di keranjang dengan mengurangi total price dengan diskon.

        Diskon rules:
        5% jika total belanja lebih dari 20000
        8% jika total belanja lebih dari 30000
        10% jika total belanja lebih dari 50000
        Selain dari rules diatas tidak mendapatkan diskon

        Print:
        Tampilkan diskon yang diperoleh dan total bayar setelah diskon
        '''
        self.total_belanja = sum(self.harga_belanja.values())
        if self.total_belanja > 200000 and self.total_belanja <= 300000:
            discount = (5/100)
            print(f'Anda mendapatkan diskon sebesar 5%')
        elif self.total_belanja > 300000 and self.total_belanja <= 500000:
            discount = (8/100)
            print(f'Anda mendapatkan diskon sebesar 8%')
        elif self.total_belanja > 500000:
            discount = (10/100)
            print(f'Anda mendapatkan diskon sebesar 10%')
        else:
            discount = 0
            print(f'Anda belum mendapatkan diskon')

        bayar = self.total_belanja - (self.total_belanja*discount)
        print(f'Total yang perlu anda bayar adalah Rp. {bayar}')
