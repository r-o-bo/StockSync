import pandas as pd
from datetime import datetime, timezone


# ngl minimal transformation cuz json was already part clean 
def transform_data(summary):
    # Coordinated Universal Time (UTC) and format it into an ISO 8601 string
    summary["transformed_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    summary["price"] = float(summary.get("price", 0))
    summary["price_change"] = float(summary.get("price_change", 0))
    summary["volume"] = int(summary.get("volume", 0))
    summary["market_cap"] = int(summary.get("market_cap", 0))
    summary["week_high"] = float(summary.get("week_high", 0))
    summary["week_low"] = float(summary.get("week_low", 0))

    # Order columns exactly as in eth_prices
    columns = [
        "symbol", "name", "price", "price_change", "percent_change",
        "volume", "market_cap", "week_high", "week_low",
        "logo", "last_updated", "transformed_at"
    ]
    df = pd.DataFrame([summary], columns=columns)

    return df



if __name__ == "__main__":
    from extract import my_crypto_summary

    summary = my_crypto_summary()
    if summary:
        df = transform_data(summary)
        print(df)