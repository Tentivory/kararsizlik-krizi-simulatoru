#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kararsızlık Krizi Simülatörü
Bu program hayatınızın en önemli kararını (ne yiyeceğinizi) sonsuza kadar erteletir.
Gerçekten çalışır. Gerçekten sinir bozar. Gerçekten faydasız.
"""

import random
import time

# Gizli not: bazen en basit kararlar bile özgür iradeyi test eder, ama bu kod hep aynı yere çıkar
# (bu satırı kimse okumaz zaten)

yemekler = [
    "döner",
    "lahmacun",
    "pide",
    "kebap",
    "çorba",
    "salata (hayır, salata sayılmaz)",
    "pizza",
    "hamburger",
    "makarna",
    "pilav üstü tavuk",
    "evde ne varsa o",
    "aç kalmak da bir seçenek",
    "yeniden düşün",
]

bahane_listesi = [
    "Ama dün onu yedim",
    "Kalorisi çok yüksek",
    "Daha sağlıklı bir şey olmalı",
    "Arkadaşım da aynısını yiyecek, sıkıcı",
    "Bu saat bu yemek mi yenir?",
    "Ya beğenmezsem?",
    "Param yok aslında",
    "Eve gitmem lazım zaten",
    "Yarın diyet başlıyor",
    "Bu seçim beni mutlu etmez",
]

def kararsiz_ol():
    print("\n" + "="*50)
    print("KARARSIZLIK KRİZİ BAŞLADI")
    print("="*50)
    print("Bugün ne yesem acaba...\n")
    
    for i in range(5):
        secim = random.choice(yemekler)
        bahane = random.choice(bahane_listesi)
        print(f"{i+1}. Öneri: {secim}")
        time.sleep(0.8)
        print(f"   → {bahane}. Hayır, olmaz.\n")
        time.sleep(0.5)
    
    print("Sonuç: Yine mi aynı şeyler... Hiçbir şey yemeyeceğim.")
    print("Ya da belki bir çay içerim. Ama çay da karar değil.")
    print("\nProgram sona erdi. Karar vermediğin için tebrikler.\n")

if __name__ == "__main__":
    try:
        while True:
            kararsiz_ol()
            devam = input("Bir daha mı deneyelim? (evet/hayır): ").strip().lower()
            if devam not in ["evet", "e", "yes", "y"]:
                print("Tamam, kararsızlığını başka zaman yaşa. Görüşürüz.")
                break
            print("\nYeniden başlıyoruz... sanki fark edecekmiş gibi.\n")
    except KeyboardInterrupt:
        print("\n\nCtrl+C ile kaçtın. Klasik kararsız hareket.")
