import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from datetime import timedelta

from pygame import mixer
import time
from tkcalendar import DateEntry
import codecs
import sys
import threading

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
olaylar_list = []

class Olay:
    def __init__(self, kullanici_adi, islem_zamani, olay_baslangic_zamani, olay_saat, olay_tanimi, olay_tipi, olay_aciklamasi):
        self.kullanici_adi = kullanici_adi
        self.islem_zamani = islem_zamani
        self.olay_baslangic_zamani = olay_baslangic_zamani
        self.olay_saat = olay_saat
        self.olay_tanimi = olay_tanimi
        self.olay_tipi = olay_tipi
        self.olay_aciklamasi = olay_aciklamasi

def giris_yap():
    kullanici_adi = kullanici_adi_field.get()
    sifre = sifre_field.get()
    with open("users.txt", "r") as file:
        for line in file:
            kullanici_bilgileri = line.strip().split(";")
            kayitli_kullanici_adi = kullanici_bilgileri[2]
            kayitli_sifre = kullanici_bilgileri[3]
            if kayitli_kullanici_adi == kullanici_adi and kayitli_sifre == sifre:
                messagebox.showinfo("Başarılı", "Giriş başarılı!")
                giris_ekran.destroy()
                ana_ekran()
                return
    messagebox.showerror("Hata", "Geçersiz kullanıcı adı veya şifre!")

def kayit_ol():
    ad = ad_field.get()
    soyad = soyad_field.get()
    kullanici_adi = kullanici_adi_field2.get()
    sifre = sifre_field2.get()
    tc_kimlik_no = tc_kimlik_no_field.get()
    telefon = telefon_field.get()
    email = email_field.get()
    adres = adres_field.get()
    kullanici_tipi = kullanici_tipi_combobox.get()
    with open("users.txt", "a") as file:
        file.write(f"{ad};{soyad};{kullanici_adi};{sifre};{tc_kimlik_no};{telefon};{email};{adres};{kullanici_tipi}\n")
    messagebox.showinfo("Başarılı", "Kayıt başarıyla tamamlandı!")
    kayit_ekran.destroy()

def olay_ekle_ekran():
    olay_ekle_ekran = tk.Toplevel()
    olay_ekle_ekran.title("Olay Ekle")

    checkbox_durumu = tk.BooleanVar()
    erken_uyari_suresi = tk.StringVar()

    def olay_ekle():
        islem_zamani = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        olay_baslangic_zamani = olay_baslangic_zamani_picker.get_date().strftime("%Y-%m-%d")
        olay_saat = olay_saat_picker.get()
        olay_tanimi = olay_tanimi_field.get()
        olay_tipi = olay_tipi_field.get()
        olay_aciklamasi = olay_aciklamasi_field.get()

        kullanici_adi = "userTemp"

        with open("olaylar.txt", "a", encoding="utf-8") as file:
            file.write(
                f"{kullanici_adi};{islem_zamani};{olay_baslangic_zamani} {olay_saat};{olay_tanimi};{olay_tipi};{olay_aciklamasi}\n")

        olay = Olay(kullanici_adi, islem_zamani, olay_baslangic_zamani, olay_saat, olay_tanimi, olay_tipi, olay_aciklamasi)
        olaylar_list.append(olay)
        olaylar_table.insert("", tk.END, values=(islem_zamani, olay_baslangic_zamani + " " + olay_saat, olay_tanimi, olay_tipi, olay_aciklamasi))

        if checkbox_durumu.get() and olay_saat:
            if erken_uyari_suresi.get():
                erken_uyari_saniye = int(erken_uyari_suresi.get())
                erken_uyari_zamani = (datetime.strptime(olay_saat, "%H:%M") - timedelta(seconds=erken_uyari_saniye)).strftime("%H:%M")
                alarm_cal(erken_uyari_zamani)
            else:
                alarm_cal(olay_saat)

        olay_ekle_ekran.destroy()

    def alarm_cal(saat):
        alarm_ses = r"alarm.mp3"
        alarm_zamani = datetime.strptime(saat, "%H:%M")

        simdi = datetime.now().strftime("%H:%M")
        simdi_zamani = datetime.strptime(simdi, "%H:%M")

        if simdi_zamani >= alarm_zamani:
            alarm_zamani += timedelta(days=1)

        bekleme_suresi = (alarm_zamani - simdi_zamani).total_seconds()

        def cal():
            mixer.init()
            mixer.music.load("alarm.mp3")
            mixer.music.play()
            while mixer.music.get_busy():
                time.sleep(1)

        threading.Timer(bekleme_suresi, cal).start()

        olay_ekle_ekran.after(int(bekleme_suresi * 1000), cal)

    checkbox = tk.Checkbutton(olay_ekle_ekran, text="Alarm Ayarla", variable=checkbox_durumu)
    checkbox.pack()

    erken_uyari_label = tk.Label(olay_ekle_ekran, text="Erken Alarm (sn):")
    erken_uyari_label.pack()

    erken_uyari_entry = tk.Entry(olay_ekle_ekran, textvariable=erken_uyari_suresi)
    erken_uyari_entry.pack()

    olay_baslangic_zamani_label = tk.Label(olay_ekle_ekran, text="Olay Başlangıç Zamanı:")
    olay_baslangic_zamani_label.pack()
    olay_baslangic_zamani_picker = DateEntry(olay_ekle_ekran, width=12, background='darkblue',
                                             foreground='white', borderwidth=2)
    olay_baslangic_zamani_picker.pack()

    olay_saat_label = tk.Label(olay_ekle_ekran, text="Saat (HH:mm):")
    olay_saat_label.pack()
    olay_saat_picker = tk.Entry(olay_ekle_ekran)
    olay_saat_picker.pack()

    olay_tanimi_label = tk.Label(olay_ekle_ekran, text="Olay Tanımı:")
    olay_tanimi_label.pack()
    olay_tanimi_field = tk.Entry(olay_ekle_ekran)
    olay_tanimi_field.pack()

    olay_tipi_label = tk.Label(olay_ekle_ekran, text="Olay Tipi:")
    olay_tipi_label.pack()
    olay_tipi_field = tk.Entry(olay_ekle_ekran)
    olay_tipi_field.pack()

    olay_aciklamasi_label = tk.Label(olay_ekle_ekran, text="Olay Açıklaması:")
    olay_aciklamasi_label.pack()
    olay_aciklamasi_field = tk.Entry(olay_ekle_ekran)
    olay_aciklamasi_field.pack()

    olay_ekle_button = tk.Button(olay_ekle_ekran, text="Olayı Ekle", command=olay_ekle)
    olay_ekle_button.pack(pady=10)

    olay_ekle_ekran.mainloop()

def olay_duzenle_ekran():
    selected_item = olaylar_table.focus()
    selected_item_data = olaylar_table.item(selected_item)
    if selected_item:
        olay_duzenle_ekran = tk.Toplevel()
        olay_duzenle_ekran.title("Olay Düzenle")
        selected_values = selected_item_data['values']

        secilenSatir2 = f"userTemp;{selected_values[0]};{selected_values[1]};{selected_values[2]};{selected_values[3]};{selected_values[4]}\n"
        print(secilenSatir2)

        def olay_duzenle():
            yeni_veri = []
            for entry in entry_list:
                yeni_veri.append(entry.get())

            with open("olaylar.txt", "r") as file:
                rows = file.readlines()

            secilenSatir = f"userTemp;{yeni_veri[0]};{yeni_veri[1]};{yeni_veri[2]};{yeni_veri[3]};{yeni_veri[4]}\n"
            print(secilenSatir)

            for i, row in enumerate(rows):
                if row.startswith(secilenSatir2):
                    rows[i] = secilenSatir
                    break

            with open("olaylar.txt", "w") as file:
                file.writelines(rows)

            olay_duzenle_ekran.destroy()
            verileri_yukle()

        selected_item_data = olaylar_table.item(selected_item)
        eski_veri = selected_item_data['values'][0:]

        entry_list = []

        for i, veri in enumerate(eski_veri):
            label = tk.Label(olay_duzenle_ekran, text=f"Veri {i+1}:")
            label.pack()
            entry = tk.Entry(olay_duzenle_ekran)
            entry.insert(tk.END, veri)
            entry.pack()
            entry_list.append(entry)

        kaydet_btn = tk.Button(olay_duzenle_ekran, text="Kaydet", command=olay_duzenle)
        kaydet_btn.pack()

    else:
        messagebox.showerror("Hata", "Lütfen düzenlemek istediğiniz olayı seçin!")

def verileri_yukle():
    olaylar_table.delete(*olaylar_table.get_children())

    with open("olaylar.txt", "r") as file:
        rows = file.readlines()

    for row in rows:
        veri = row.strip().split(';')[1:]
        olaylar_table.insert("", tk.END, values=veri)

def olay_sil():
    selected_items = olaylar_table.selection()
    if selected_items:
        for item in selected_items:
            index = olaylar_table.index(item)
            olaylar_table.delete(item)
            if len(olaylar_list) > 0:
                olaylar_list.pop(index)
            else:
                pass
        with open("olaylar.txt", "w", encoding="utf-8") as file:
            for olay in olaylar_list:
                file.write(f"{olay.kullanici_adi};{olay.islem_zamani};{olay.olay_baslangic_zamani} {olay.olay_saat};{olay.olay_tanimi};{olay.olay_tipi};{olay.olay_aciklamasi}\n")
    else:
        messagebox.showerror("Hata", "Lütfen silmek istediğiniz olayları seçin!")

def ana_ekran():
    global olaylar_table
    def cikis_yap():
        ana_ekran.destroy()

    ana_ekran = tk.Tk()
    ana_ekran.title("Ana Ekran")

    olaylar_table_frame = tk.Frame(ana_ekran)
    olaylar_table_frame.pack(pady=10)

    olaylar_table_columns = ("İşlem Zamanı", "Olay Başlangıç Zamanı", "Olay Tanımı", "Olay Tipi", "Olay Açıklaması")
    olaylar_table = ttk.Treeview(olaylar_table_frame, columns=olaylar_table_columns, show="headings")

    for column in olaylar_table_columns:
        olaylar_table.heading(column, text=column)

    olaylar_table.pack()

    verileri_yukle()

    olay_ekle_button = tk.Button(ana_ekran, text="Olay Ekle", command=olay_ekle_ekran)
    olay_ekle_button.pack(pady=10)

    olay_duzenle_button = tk.Button(ana_ekran, text="Olay Düzenle", command=olay_duzenle_ekran)
    olay_duzenle_button.pack(pady=5)

    olay_sil_button = tk.Button(ana_ekran, text="Olay Sil", command=olay_sil)
    olay_sil_button.pack(pady=5)

    cikis_button = tk.Button(ana_ekran, text="Çıkış Yap", command=cikis_yap)
    cikis_button.pack()

    ana_ekran.mainloop()

def kayit_sayfasi():
    global kayit_ekran
    kayit_ekran = tk.Tk()
    kayit_ekran.title("Kayıt Ol")

    ad_label = tk.Label(kayit_ekran, text="Ad:")
    ad_label.pack()
    global ad_field
    ad_field = tk.Entry(kayit_ekran)
    ad_field.pack()

    soyad_label = tk.Label(kayit_ekran, text="Soyad:")
    soyad_label.pack()
    global soyad_field
    soyad_field = tk.Entry(kayit_ekran)
    soyad_field.pack()

    kullanici_adi_label = tk.Label(kayit_ekran, text="Kullanıcı Adı:")
    kullanici_adi_label.pack()
    global kullanici_adi_field2
    kullanici_adi_field2 = tk.Entry(kayit_ekran)
    kullanici_adi_field2.pack()

    sifre_label = tk.Label(kayit_ekran, text="Şifre:")
    sifre_label.pack()
    global sifre_field2
    sifre_field2 = tk.Entry(kayit_ekran, show="*")
    sifre_field2.pack()

    tc_kimlik_no_label = tk.Label(kayit_ekran, text="TC Kimlik No:")
    tc_kimlik_no_label.pack()
    global tc_kimlik_no_field
    tc_kimlik_no_field = tk.Entry(kayit_ekran)
    tc_kimlik_no_field.pack()

    telefon_label = tk.Label(kayit_ekran, text="Telefon:")
    telefon_label.pack()
    global telefon_field
    telefon_field = tk.Entry(kayit_ekran)
    telefon_field.pack()

    email_label = tk.Label(kayit_ekran, text="E-mail:")
    email_label.pack()
    global email_field
    email_field = tk.Entry(kayit_ekran)
    email_field.pack()

    adres_label = tk.Label(kayit_ekran, text="Adres:")
    adres_label.pack()
    global adres_field
    adres_field = tk.Entry(kayit_ekran)
    adres_field.pack()

    kullanici_tipi_label = tk.Label(kayit_ekran, text="Kullanıcı Tipi:")
    kullanici_tipi_label.pack()
    global kullanici_tipi_combobox
    kullanici_tipi_combobox = ttk.Combobox(kayit_ekran, values=["Standart", "Admin"])
    kullanici_tipi_combobox.pack()

    kayit_ol_button = tk.Button(kayit_ekran, text="Kayıt Ol", command=kayit_ol)
    kayit_ol_button.pack()

    kayit_ekran.mainloop()

giris_ekran = tk.Tk()
giris_ekran.title("Giriş Yap")

kullanici_adi_label = tk.Label(giris_ekran, text="Kullanıcı Adı:")
kullanici_adi_label.pack()
kullanici_adi_field = tk.Entry(giris_ekran)
kullanici_adi_field.pack()

sifre_label = tk.Label(giris_ekran, text="Şifre:")
sifre_label.pack()
sifre_field = tk.Entry(giris_ekran, show="*")
sifre_field.pack()

giris_button = tk.Button(giris_ekran, text="Giriş Yap", command=giris_yap)
giris_button.pack()

kayit_button = tk.Button(giris_ekran, text="Kayıt Ol", command=kayit_sayfasi)
kayit_button.pack()

giris_ekran.mainloop()
