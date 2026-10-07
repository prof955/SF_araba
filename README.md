# 🕹️ Street Fighter II — Bonus Stage: Car Smash 🚗💥

[![Street Fighter II Tribute](https://img.shields.io/badge/Capcom-Street%20Fighter%20II-E52521?style=for-the-badge&logo=retroarch&logoColor=white)](https://github.com/prof955/SF_araba)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://github.com/prof955/SF_araba)
[![HTML5 Canvas](https://img.shields.io/badge/Canvas-HTML5%202D-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://github.com/prof955/SF_araba)
[![Web Audio API](https://img.shields.io/badge/Audio-Procedural%2016--Bit%20Synth-9cf?style=for-the-badge&logo=soundcharts&logoColor=black)](https://github.com/prof955/SF_araba)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero%20(Pure%20Vanilla)-brightgreen?style=for-the-badge)](https://github.com/prof955/SF_araba)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)

> **Efsanevi Street Fighter II arcade "Bonus Stage" araba parçalama bölümünün web tarayıcıları için piksel piksel, sıfır harici kütüphane bağımlılığı ve prosedürel 16-bit Web Audio sentezleyicisi ile yeniden canlandırılmış sürümü!**

---

## 📸 Görseller & Sprite Anatomisi

Orijinal Capcom CPS-1 arcade sprite'larından titizlikle ayrıştırılmış gövde, kapılar, tavan, tampon, dökülen cam/metal parçaları ve patlama animasyonları:

![Sprite Kataloğu](sprite_catalog.png)

---

## ✨ Öne Çıkan Özellikler

- 🎯 **Piksel Hassasiyetinde Arcade Deneyimi:**
  - Orijinal Street Fighter II liman iskelesi arka planı (`bg_stage.png`).
  - CRT Monitör hissi veren tarama çizgisi (scanline) kaplaması ve arcade kabin bezel çerçevesi.
  - Piksel ölçeklendirmeli (crisp pixelated) 60 FPS akıcı Canvas motoru.

- 🚗 **9+ Aşamalı Dinamik Hasar & Parçalanma Fiziği:**
  - **Bölgesel Hasar Algılama:** Sol kapı, sağ cam, tavan veya kaput bölgelerine vurulduğunda farklı parçalanma reaksiyonları.
  - **Kırılan Camlar:** Cam kırıldığında etrafa sadece şeffaf cam parçacıkları fırlar.
  - **Kopan Tavan & Uçan Kaput:** Belli bir hasar eşiğinde tavan ve kaput parçaları fizik kurallarına göre havalanır.
  - **Fırlayan Tekerlek & Plaka:** Araç pert olduğunda sağ ön tekerlek kopup iskele üzerinde zıplayarak yuvarlanır!
  - **Kalıcı Duman, Alev ve Buhar:** Radyatör parçalandığında tıslayan buhar; motor patladığında yükselen persistent alev ve duman sütunları.

- 🔊 **Prosedürel 16-Bit Web Audio Synthesizer (Harici Ses Dosyası GEREKTİRMEZ!):**
  - Tüm vuruş sesleri, metal çarpışmaları, cam kırılmaları, patlamalar ve Perfect zafer jingle'ı doğrudan tarayıcının Web Audio API osilatörleri ve frekans rampalarıyla anlık olarak sentezlenir.
  - Boyut tasarrufu ve sıfır gecikmeli (zero-latency) anlık ses çalma.
  - Ses Açma/Kapama (SFX Toggle) butonu.

- 🥊 **Otantik Dövüşçü Hissi:**
  - CPS-1 tarzı yatay darbe titremesi (shudder vibration — araba gerçekteki gibi tek yöne sarsılır, doğal olmayan sallantı yapmaz).
  - Güçlü darbelerde Hit-Stop (darbe donması) ve travma bazlı ekran sarsıntısı (screen shake).
  - 8 köşeli retro arcade vuruş kıvılcımları (Hit Sparks) ve yükselen skor baloncukları.

- 🏆 **Retro Arcade HUD:**
  - 1P Skor Sayacı.
  - 40 saniyelik bonus stage geri sayım sayacı.
  - Dinamik renk değiştiren Car Integrity (sağlık) çubuğu.
  - Kombo Sayacı (`💥 X HITS!`).
  - Araba tamamen parçalandığında **PERFECT! BONUS 30000 PTS** zafer anonsu.

---

## 🎮 Kontroller & Tuş Takımı

Oyunu ister klavye ile, ister fare/dokunmatik ekranla doğrudan arabanın parçalarına tıklayarak oynayabilirsiniz:

| Tuş | Alternatif | Aksiyon | Hasar | Skor | Özel Efekt |
| :---: | :---: | :--- | :---: | :---: | :--- |
| `1` | `Q` | **Light Punch (Hafif Yumruk)** | 1 | +100 | Hızlı vuruş |
| `2` | `W` | **Heavy Punch (Ağır Yumruk)** | 2 | +300 | Hit-stop ve orta sarsıntı |
| `3` | `E` | **Fierce Kick (Sert Tekme)** | 3 | +500 | Yüksek ekran titreşimi |
| `4` | `R` | **Special Smash (Özel Vuruş)** | 5 | +1000 | Maksimum kıvılcım & metal ezilmesi |
| `Space` / `Enter` | — | **Hızlı Vur** | Seçili | Seçili | Arabaya rastgele noktadan saldırı |
| `Sol Tık` / `Dokunmatik` | — | **Noktasal Darbe** | Seçili | Seçili | Tıklanan kapı/cam/kaput/tavana hasar |

---

## 🛠️ Teknoloji Yığını

- **HTML5 Canvas 2D:** Çizim ve parçacık fizik motoru.
- **Modern JavaScript (ES6+):** Sıfır kütüphane bağımlılığı (Pure Vanilla JS).
- **Web Audio API:** Prosedürel 16-bit retro arcade ses sentezi.
- **CSS3:** Retro kabin gölgelemesi ve CRT scanline efektleri.
- **Tipografi:** Google Fonts — Press Start 2P.

---

## 🚀 Kurulum & Çalıştırma

Projeyi çalıştırmak için hiçbir paket yöneticisi (`npm`, `yarn`, `pip` vb.) kurmanıza gerek yoktur!

### 1. Repoyu Klonlayın
```bash
git clone https://github.com/prof955/SF_araba.git
cd SF_araba
```

### 2. Oyunu Başlatın
Aşağıdaki yöntemlerden herhangi birini seçebilirsiniz:

- **Doğrudan Tarayıcıda Açın:**
  `index.html` dosyasını çift tıklayarak herhangi bir modern web tarayıcısında (Chrome, Firefox, Edge, Safari) açın.

- **veya Yerel Geliştirici Sunucusu ile (Önerilen):**
  ```bash
  # Python 3 yüklüyse:
  python -m http.server 8000
  ```
  Ardından tarayıcınızdan `http://localhost:8000` adresine gidin.

- **veya VS Code Live Server ile:**
  `index.html` dosyasına sağ tıklayıp **"Open with Live Server"** seçeneğini kullanın.

---

## 📁 Proje Dosya Yapısı

```
SF_araba/
├── sprites/              # Ayrıştırılmış 53 adet PNG sprite (parçalar, duman, alev vb.)
├── bg_stage.png          # Liman iskelesi arka plan görseli (384x224 CPS-1 ölçekli)
├── background.png        # Alternatif arka plan kaynağı
├── car.png               # Orijinal ham sprite sheet
├── sprite_catalog.png    # Sprite indeks ve parça kataloğu
├── index.html            # Oyun motoru, ses sentezleyici ve kullanıcı arayüzü
├── debug.html            # Sprite koordinat tespit aracı
├── gen_debug.py          # Sprite kutu oluşturucu yardımcı betik
└── README.md             # Proje dokümantasyonu
```

---

## ⚖️ Yasal Uyarı / Disclaimer

Street Fighter ve ilgili karakterler/grafikler **Capcom Co., Ltd.**'ye aittir. Bu proje ticari amaç gütmeyen, nostalji ve retro oyun geliştirme tekniklerini inceleme amacıyla hazırlanmış açık kaynaklı bir saygı/hayran (fan-made tribute) projesidir.

---

## 📄 Lisans

Bu proje [MIT](LICENSE) lisansı altında sunulmaktadır.
Dilediğiniz gibi inceleyebilir, geliştirebilir ve kombo yapmaya devam edebilirsiniz! 🥊💥
