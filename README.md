# AD49F — Group 6: Unsupervised ML1 Applications

**"20 hisse, kaç bahis?"** — BIST'te PCA ve kümeleme ile gizli risk faktörleri

AD 49F: Data and Decisions — Building Your Own Investing Algorithms with AI · Boğaziçi Üniversitesi

## Ekip

| Üye | Sahnede | Sorumluluk | Kod |
| --- | --- | --- | --- |
| Elif Sude Cengiz (A) | Açılış, Perde 1: PCA, soru-cevap moderatörü | Hikâye + PCA uzmanı; demo programı | `src/config.py`, `src/pca.py`, `grup6_demo.py`, `tests/helpers.py` |
| Üye B (isim) | Perde 2: Kümeleme, Kapanış | Kümeleme + canlı Claude Code demosu; slaytlar | `src/plotting.py`, `src/clustering.py`, `tests/run_all.py` |
| Üye C (isim) | Veri bölümü, Perde 3: Dürüst test | Veri hattı, dürüst test, dürüstlük sözleşmesi | `src/data.py`, `src/backtest.py`, `docs/decisions.md` |

Ekip: Elif Sude Cengiz, Esat Çankaya, Ahmet Çevik.

## Hipotez

20 likit BIST hissesi tutan bir yatırımcı 20 bağımsız bahis yaptığını sanır. PCA ve kümeleme, gerçek bağımsız
risk kaynağı sayısının çok daha az olduğunu ve stres dönemlerinde daha da azaldığını gösterir. Bu bilgiyle kurulan
küme-dengeli portföyü eşit ağırlıklı portföye karşı, sızıntısız bir walk-forward testle karşılaştırıyoruz.

## Kurulum

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Çalıştırma

```bash
python grup6_demo.py --act 0       # veri ve temizlik kontrolleri
python grup6_demo.py --act 1       # PCA
python grup6_demo.py --act 2       # kümeleme
python grup6_demo.py --act 3       # walk-forward backtest + absorption ratio
python grup6_demo.py --act all --synthetic    # internetsiz prova
python tests/run_all.py            # veya: pytest tests/
```

İlk çalıştırma veriyi `data/` klasörüne kaydeder; sonraki çalıştırmalar internetsiz çalışır.
Grafikler `figs/` klasörüne yazılır.

## Proje yapısı

```text
grup6_demo.py        sunumda çalıştırılan giriş noktası
src/config.py        tarihler, hisseler, sabitlenmiş parametreler (dürüstlük sözleşmesi)
src/data.py          indirme, önbellek, temizlik (tatil günleri, ±%10 kontrolü)
src/pca.py           PCA, Marchenko–Pastur gürültü sınırı, efektif bahis sayısı
src/clustering.py    korelasyon mesafesi, hiyerarşik kümeleme, k seçimi, kararlılık
src/backtest.py      walk-forward backtest, katkı analizi, absorption ratio
src/plotting.py      ortak grafik stili
tests/               23 sanity testi
docs/                kararlar, sonuçlar, yapay zeka kullanım logu
```

## Dürüstlük sözleşmesi

Parametreler sonuçlar görülmeden `src/config.py` ve `docs/decisions.md` içinde sabitlenmiştir:
eğitim/test kesimi 2025-06-30, 250 günlük geçmiş pencere, aylık yeniden dengeleme, 10 bp/yön işlem maliyeti,
k yalnızca eğitim verisiyle seçilir.

## Yapay zeka kullanımı

Kodun bir kısmı Claude ile yazıldı; her parçası `tests/` altındaki testlerle doğrulandı.
Prompt'lar, çıktılar ve yakalanan hatalar `docs/ai_log.md` dosyasındadır.
