from tkinter import *
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import webbrowser

# Pendefinisian fungsi gui dimana membuat UI Aplikasi dengan Main Window, Label, Image dan Button
def gui():
    global root
    root = Tk()
    root.title("AngForm | UTS ALPRO PRAKTIKUM")
    root.geometry("450x450")
    root.resizable(False, False)
    root.configure(bg='lightblue')

    # Label Header Aplikasi
    header = Label(root, text="Welcome to AngForm, Automation Programming Form", font=("Poppins", 11), bg='lightblue')
    header.place(x=225, y=50, anchor=CENTER)

    # Image Main Aplikasi
    image = PhotoImage(file="rksa.png")
    image_label = Label(root, image=image)
    image_label.place(x=225, y=175, anchor=CENTER)

    # Start Button Aplikasi untuk masuk ke frame automation
    start_button = Button(root, text="Start", command=start, width=9, height=2)
    start_button.place(x=125, y=300)

    # Exit button Aplikasi untuk keluar aplikasi dan menghentikan kerja aplikasi
    exit_button = Button(root, text="Exit", command=exit, width=9, height=2, bg="red")
    exit_button.place(x=250, y=300)
    
    # Label Detail Penjelasan Aplikasi
    detail = Label(root, text="AngForm adalah Automation Python tools yang dibuat untuk memenuhi", font=("Roboto", 10), bg='lightblue')
    detail.place(x=225, y=375, anchor=CENTER)
    
    # Label Detail Penjelasan Aplikasi
    detail2 = Label(root, text="Praktikum UTS Mata Kuliah Algoritma dan Pemrograman", font=("Roboto", 10), bg='lightblue')
    detail2.place(x=225, y=400, anchor=CENTER)
    
    # Credit dan Hyperlink ke GitHub
    credit = Label(root, text="For more details, click here", font=("Roboto", 10), bg="lightblue", fg="blue")
    credit.place(x=225, y=425, anchor=CENTER)
    credit.bind("<Button-1>", lambda e: github("https://github.com/ArchK1tsune-IX"))

    root.mainloop()

# Pendefinisian Fungsi Start Button ketika ditekan akan membuat frame baru
def start():
    frame_new = Frame()
    frame_new.pack(fill=BOTH, expand=True)
    
    # Label meminta Nama dari user
    nama_gform = Label(frame_new, text="Masukkan Nama anda: ", font=('Poppins', 11))
    nama_gform.pack(pady=10)
    
    # Entry atau tempat inputan nama dari user
    entry_nama = Entry(frame_new, width=30)
    entry_nama.pack(pady=10)
    
    # Label meminta NIM dari user
    nim_gform = Label(frame_new, text="Masukkan NIM anda: ", font=('Poppins', 11))
    nim_gform.pack(pady=10)
    
    # Entry atau tempat inputan NIM dari user
    entry_nim = Entry(frame_new, width=30)
    entry_nim.pack(pady=10)
    
    # Label meminta inputan Total Pengisian Form dari user
    input_gform = Label(frame_new, text="Total Pengisian Form: ", font=('Poppins', 11))
    input_gform.pack(pady=10)
    
    # Entry atau tempat inputan Total Pengisian Form dari user
    entry_gform = Entry(frame_new, width=30)
    entry_gform.pack(pady=10)
    
    # Submit Button untuk memulai automation dengan mengirimkan input nama, nim dan total pengisian form dari user
    mulai_button = Button(frame_new, text="Submit", command=lambda: auto_form(entry_nama.get(), entry_nim.get() ,entry_gform.get(), frame_new), width=20, height=2, bg="green")
    mulai_button.pack(pady=10)
    
    # Back Button untuk kembali ke Main Window (function gui)
    back_button = Button(frame_new, text="Back", command=lambda: back_to_gui(frame_new), width=20, height=2)
    back_button.pack(pady=10)
    
    # Label Details/Credit seperti di function gui
    detail = Label(frame_new, text="For more details please see", font=("Poppins", 10), fg="blue")
    detail.place(x=225, y=425, anchor=CENTER)
    detail.bind("<Button-1>", lambda e: github("https://github.com/ArchK1tsune-IX"))

# Pendefinisian Fungsi auto_form
def auto_form(nama, nim, input_value, window):
    pengulangan = int(input_value) # Mengbuah tipe data dari input pengisian form ke integer
    driver = webdriver.Chrome() # membuka google chrome
    driver.get('https://forms.gle/gUNAfgqb7znZCLCFA') # membuka link google form UTS Alpro Praktikum
 
#   
    for i in range(pengulangan):
        time.sleep(1)
        kelas_dropdown = driver.find_element(By.XPATH, "//div[@role='listbox']") # XPATH listbox "Pilih"
        kelas_dropdown.click()

        time.sleep(1)

        # mengambil xpath dari RKS 2022 Regular A dan mengkliknya
        rksa = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[3]')
        rksa.click()
        
        time.sleep(1)

        # memasukkan inputan Nama dari user sebelumnya ke XPATH input Nama pada link Google Form
        nama_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        nama_input.send_keys(nama)
        
        time.sleep(0.1)
        
        # memasukkan inputan NIM dari user sebelumnya ke XPATH input Nama pada link Google Form 
        nim_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        nim_input.send_keys(nim)
        
        time.sleep(0.1)

        # Memilih skala berdasrkan XPATH yang sesuai, conth skala mendapat ilmu baru
        skala = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div')
        skala.click()

        # Submit form menggunakan xpath yang sesuai
        submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        submit.click()

        # Refresh Link Gform untuk menghindari Crash Network, Overheat CPU, lag, dll
        refresh = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        refresh.click()
     
    # Quit browser apabila proses looping selesai
    driver.quit()
    # Message kalau form selesai dilakukan  
    messagebox.showinfo("Status", "Pengisian Form telah berhasil dilakukan sebanyak {} kali".format(pengulangan))

# Pendefinisian fungsi button back untuk kembali ke Main Window dengan menghapus frame start
def back_to_gui(frame):
    # Hapus frame baru
    frame.pack_forget()   
 
# Pendefinsian fungsi untuk Link Github    
def github(url):
    webbrowser.open_new_tab(url)
 
# Pemanggilan Fungsi gui untuk menjalankan seluruh aplikasi   
gui()