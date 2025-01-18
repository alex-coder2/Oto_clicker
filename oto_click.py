import pyautogui
import time

x = float(input("Her tıklama arasındaki süreyi (saniye cinsinden) yazınız: "))
z = int(input("Kaç saniye sürecek: "))
time.sleep(3)
k = pyautogui.position()
basma_sayisi = 0
y = time.time() + z
while time.time() < y:  
    pyautogui.click(k) 
    basma_sayisi += 1
    time.sleep(x)
    print("Basıldı")
print(f"toplam basma sayısı: {basma_sayisi}")
print(f"Ortalama: {basma_sayisi/z}")
# unutma - pyautogui.position() mouse'un bulunduğu konumu gösterir