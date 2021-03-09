import time

benar = ["B", "s", "benar", "Benar"]
salah = ["S", "b", "salah", "Salah"]
correct = 0 #Storing dari jawaban benar

nama = input ("Oke kawan, Siapa nama kamu: ")

print ("\nOke " +  nama +", mari kita mulai, Ingat, jawablah soal berikut dengan kata-kata Benar atau Salah.")
time.sleep(2)#memberikan jeda waktu 2 menit

print ("\n1+1=2")
pilih = input("Benar atau Salah?  ")
if pilih in benar:
  correct += 1 #jika memilih benar, user mendapatkan poin
else:
  correct += 0
  
print ("\nIbu kota dari indonesia adalah Jember.")
pilih = input("Benar atau Salah? ")
if pilih in salah:
  correct += 1
else:
  correct += 0  

print ("\nMakanan khas jawa timur ialah soto padang.")
pilih = input("Benar atau Salah?  ")
if pilih in salah:
  correct += 1
else:
  correct += 0 
  
print ("\nAplikasi VTube adalah aplikasi yang menjanjikan")
pilih = input("Benar atau Salah? ")
if pilih in benar:
  print ("\nGooo, Diamond")
  correct += 1
else:
  correct += 0  
    
print ("\nYeyyy dah selesai, " + nama +" Kamu benar", correct, "dari 4 pertanyaan.")