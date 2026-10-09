"""
Honesty contract: the values in this file are fixed BEFORE looking at any results.
If you change one, record it in the "Later changes" table in docs/decisions.md.
"""

START_DATE = "2024-01-01"
# yfinance treats `end` as EXCLUSIVE: one day later so that the 2026-10-01 close is included.
END_DATE = "2026-10-02"
TRAIN_END = "2025-06-30"      # everything after this date is the test period; models never see it

LOOKBACK = 250                # look-back window for the walk-forward backtest (trading days)
AR_WINDOW = 120               # window length for the absorption ratio
COST_BPS = 10                 # one-way transaction cost (basis points)
K_RANGE = range(2, 9)         # numbers of clusters tried with the silhouette score
K_OVERRIDE = None             # e.g. 4: a k justified in advance instead of silhouette (log it in decisions.md)
MAX_MISSING = 0.05            # stocks with more missing data than this are dropped
PRICE_LIMIT = 0.10            # BIST daily price limit (±10%)

# The group's 20 stocks. Sector labels are used only for comparison (ARI).
TICKERS = {
    "THYAO.IS": "Transport", "PGSUS.IS": "Transport",
    "GARAN.IS": "Banking", "AKBNK.IS": "Banking", "ISCTR.IS": "Banking", "YKBNK.IS": "Banking",
    "KCHOL.IS": "Holding", "SAHOL.IS": "Holding",
    "SISE.IS": "Glass", "EREGL.IS": "Steel",
    "TUPRS.IS": "Energy", "PETKM.IS": "Chemicals",
    "ASELS.IS": "Defense", "ENKAI.IS": "Construction",
    "FROTO.IS": "Automotive", "TOASO.IS": "Automotive",
    "BIMAS.IS": "Retail", "MGROS.IS": "Retail",
    "TCELL.IS": "Telecom", "TTKOM.IS": "Telecom",
}
BENCH = "XU100.IS"
FX = "USDTRY=X"

DATA_DIR = "data"
FIG_DIR = "figs"
