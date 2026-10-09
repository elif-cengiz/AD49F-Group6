"""
Dürüstlük sözleşmesi: bu dosyadaki değerler sonuçlar görülmeden ÖNCE sabitlenir.
Değiştirirseniz docs/decisions.md içindeki "Sonradan yapılan değişiklikler" tablosuna yazın.
"""

START_DATE = "2024-01-01"
# yfinance'te `end` HARİÇTİR: 2026-10-01 kapanışını dahil etmek için bir gün sonrası.
END_DATE = "2026-10-02"
TRAIN_END = "2025-06-30"      # sonrası test; modeller test verisini hiç görmez

LOOKBACK = 250                # walk-forward'da kullanılan geçmiş pencere (işlem günü)
AR_WINDOW = 120               # absorption ratio pencere uzunluğu
COST_BPS = 10                 # tek yön işlem maliyeti (baz puan)
K_RANGE = range(2, 9)         # silhouette ile denenecek küme sayıları
K_OVERRIDE = None             # ör. 4: silhouette yerine önceden gerekçelendirilmiş k (decisions.md'ye yazın)
MAX_MISSING = 0.05            # bundan fazla eksik verisi olan hisse çıkarılır
PRICE_LIMIT = 0.10            # BIST günlük fiyat marjı (±%10)

# Grubun 20 hissesi. Sektör etiketleri yalnızca karşılaştırma (ARI) için kullanılır.
TICKERS = {
    "THYAO.IS": "Ulaşım", "PGSUS.IS": "Ulaşım",
    "GARAN.IS": "Banka", "AKBNK.IS": "Banka", "ISCTR.IS": "Banka", "YKBNK.IS": "Banka",
    "KCHOL.IS": "Holding", "SAHOL.IS": "Holding",
    "SISE.IS": "Cam", "EREGL.IS": "Metal",
    "TUPRS.IS": "Enerji", "PETKM.IS": "Kimya",
    "ASELS.IS": "Savunma", "ENKAI.IS": "İnşaat",
    "FROTO.IS": "Otomotiv", "TOASO.IS": "Otomotiv",
    "BIMAS.IS": "Perakende", "MGROS.IS": "Perakende",
    "TCELL.IS": "Telekom", "TTKOM.IS": "Telekom",
}
BENCH = "XU100.IS"
FX = "USDTRY=X"

DATA_DIR = "data"
FIG_DIR = "figs"
