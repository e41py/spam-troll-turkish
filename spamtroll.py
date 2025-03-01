import pyautogui
import time
import keyboard
import customtkinter as ctk
from tkinter import messagebox

# CustomTkinter Ayarları
ctk.set_appearance_mode("dark")  # Koyu Tema
ctk.set_default_color_theme("green")  # Yeşil vurgular

# Mesaj Gönderme Fonksiyonu
def baslat():
    global mesaj
    mesaj = mesaj_entry.get()
    messagebox.showinfo("Bilgi", "10 saniye sonra mesajlarınız gönderilecek.\nDurdurmak için 'q' tuşuna basın.")
    time.sleep(10)
    
    while True:
        if keyboard.is_pressed('q'):
            print("Döngü durduruldu.")
            messagebox.showinfo("Bilgi", "Mesaj gönderme işlemi durduruldu!")
            break
        pyautogui.write(mesaj)
        pyautogui.press("enter")
        time.sleep(0.1)

# Kapanış Animasyonu
def animasyon_kapat():
    for i in range(100, 0, -5):  # Opaklığı azalt
        root.attributes("-alpha", i / 100)
        root.update()
        time.sleep(0.02)
    root.destroy()

# Açılış Animasyonu
def animasyon_ac():
    root.attributes("-alpha", 0)
    for i in range(0, 101, 5):  # Opaklığı artır
        root.attributes("-alpha", i / 100)
        root.update()
        time.sleep(0.02)

# Ana Pencere
root = ctk.CTk()
root.title("Otomatik Mesaj Spam Botu")
root.attributes("-fullscreen", True)  # Otomatik Fullscreen
root.bind("<Escape>", lambda e: animasyon_kapat())  # ESC ile kapanış

# Açılış animasyonu başlat
animasyon_ac()

# Ana Çerçeve
frame = ctk.CTkFrame(root, corner_radius=20)
frame.pack(expand=True, padx=40, pady=40)

# Başlık
title_label = ctk.CTkLabel(frame, text="Mesaj Spam Botu", font=("Arial", 26, "bold"))
title_label.pack(pady=20)

# Mesaj giriş kutusu
mesaj_entry = ctk.CTkEntry(frame, placeholder_text="Mesajınızı girin...", font=("Arial", 20), width=400, height=50)
mesaj_entry.pack(pady=10)

# Başlat Butonu
gonder_buton = ctk.CTkButton(frame, text="Başlat", command=baslat, font=("Arial", 20), width=250, height=50, corner_radius=10)
gonder_buton.pack(pady=20)

# Çıkış Butonu
cikis_buton = ctk.CTkButton(frame, text="Çıkış", command=animasyon_kapat, font=("Arial", 20), fg_color="red", width=250, height=50, corner_radius=10)
cikis_buton.pack(pady=10)

# Footer (Made by em41py)
footer_label = ctk.CTkLabel(root, text="Made by em41py", font=("Arial", 24), text_color="gray")
footer_label.place(relx=0.5, rely=0.95, anchor="center")

root.mainloop()
