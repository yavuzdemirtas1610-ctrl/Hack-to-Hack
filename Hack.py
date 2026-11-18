import time
import sys
import random
import os

YESIL = '\033[92m'
CYAN = '\033[96m'
SARI = '\033[93m'
MOR = '\033[95m'
KIRMIZI = '\033[91m'
BEYAZ = '\033[97m'
SIFIRLA = '\033[0m'
KALIN = '\033[1m'

def temizle():
    os.system('clear')

def yukleme_ekrani():
    temizle()
    print(f"{KIRMIZI}{KALIN}==========================================")
    print("       ⚡ CYBER-PULSE v4.0 BAŞLATILIYOR ⚡")
    print(f"=========================================={SIFIRLA}\n")
    
    asamalar = [
        "Güvenlik protokolleri test ediliyor...",
        "Şifreli veritabanı bağlantısı kuruluyor...",
        "Algoritmalar optimize ediliyor...",
        "Sistem kararlılığı doğrulanıyor...",
        "Oyun motoru aktif hale getirildi!"
    ]
    
    toplam = 35
    for i in range(toplam + 1):
        yuzde = int((i / toplam) * 100)
        dolu = '█' * i
        bos = '░' * (toplam - i)
        asama = asamalar[min(i // 7, len(asamalar) - 1)]
        
        sys.stdout.write(f"\r{CYAN}[{dolu}{bos}] {YESIL}%{yuzde}{SIFIRLA} - {SARI}{asama:<38}{SIFIRLA}")
        sys.stdout.flush()
        time.sleep(random.uniform(0.03, 0.1))
        
    print(f"\n\n{YESIL}{KALIN}[✓] Sistem hazır!{SIFIRLA}")
    time.sleep(1)

def trojan_sakasini_baslat():
    temizle()
    print(f"{KIRMIZI}{KALIN}[!] 5 HAKKIN BİTTİ! SİSTEM AÇIĞI TESPİT EDİLDİ [!]{SIFIRLA}\n")
    time.sleep(1.5)
    
    # Korkutucu kod akışı şakası
    komutlar = [
        "ROOT yetkileri zorlanıyor...",
        "Bypass firewall success...",
        "Payload /system/bin/trojan.sh indiriliyor...",
        "Ana dizin şifreleniyor: AES-256...",
        "Kamera erişimi açılıyor [ON]...",
        "Kişiler listesi sunucuya aktarılıyor...",
        "Galeri dosyaları buluta kopyalanıyor...",
        "Cihaz uzaktan kontrol moduna geçirildi...",
        "Kritik hata: Çekirdek ele geçirildi!"
    ]
    
    for _ in range(2):
        for komut in komutlar:
            print(f"{KIRMIZI}[KOD] {random.randint(1000,9999)} -> {komut}{SIFIRLA}")
            time.sleep(0.15)
            
    # Matrix tarzı hızlıca akan kodlar
    try:
        for _ in range(35):
            kod_satiri = "".join(random.choice(["0", "1", "X", "A", "F", "!", "#", "$", "ERR", "TRJ"]) for _ in range(40))
            print(f"{YESIL}{kod_satiri}{SIFIRLA}")
            time.sleep(0.04)
    except KeyboardInterrupt:
        pass
        
    temizle()
    print(f"\n{KIRMIZI}{KALIN}==========================================")
    print("      ⚠️ KRİTİK SİSTEM UYARISI ⚠️")
    print(f"=========================================={SIFIRLA}\n")
    print(f"{BEYAZ}Cihazınıza harici bir payload enjekte edildi.")
    print(f"Tüm verileriniz şifrelendi ve dış sunucuya gönderildi.")
    print(f"Yetkisiz erişim tespit edildi.{SIFIRLA}\n")
    print(f"{SARI}Şaka şaka la! 😂 Kendine gel, alt tarafı alt alta 5 sayı bilemedin, donanımın sağlam merak etme!{SIFIRLA}\n")
    sys.exit()

def ana_program():
    temizle()
    print(f"{CYAN}{KALIN}╔════════════════════════════════════════╗")
    print("║        🎯 5 HAKKIN VAR: SAYI TAHMİNİ   ║")
    print(f"╚════════════════════════════════════════╝{SIFIRLA}\n")
    
    print(f"{BEYAZ}1 ile 50 arasında bir sayı tuttum.")
    print(f"Bulmak için sadece {KIRMIZI}5 hakkın var{BEYAZ}. Bilemezsen sistem çökecek!\n{SIFIRLA}")
    
    hedef = random.randint(1, 50)
    hak = 5
    
    while hak > 0:
        print(f"{SARI}Kalan Hak: {hak}{SIFIRLA}")
        tahmin_str = input(f"{CYAN}Tahminin nedir?: {SIFIRLA}")
        
        try:
            tahmin = int(tahmin_str)
        except ValueError:
            print(f"{KIRMIZI}Lütfen geçerli bir sayı gir!{SIFIRLA}\n")
            continue
            
        if tahmin == hedef:
            print(f"\n{YESIL}{KALIN}🎉 Helal olsun! Sayıyı bildin ve sistemi kurtardın!{SIFIRLA}\n")
            sys.exit()
        elif tahmin < hedef:
            print(f"{MOR}Daha BÜYÜK bir sayı söyle ⬆️\n{SIFIRLA}")
        else:
            print(f"{MOR}Daha KÜÇÜK bir sayı söyle ⬇️\n{SIFIRLA}")
            
        hak -= 1
        
    # 5 hak bittiğinde şaka başlar
    trojan_sakasini_baslat()

if __name__ == "__main__":
    yukleme_ekrani()
    ana_program()
  
