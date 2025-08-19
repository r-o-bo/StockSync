import pandas as pd
from datetime import datetime, timezone


# ngl minimal transformation cuz json was already part clean
def transform_data(summary):
    # Coordinated Universal Time (UTC) and format it into an ISO 8601 string
    summary["transformed_at"] = datetime.now(timezone.utc).isoformat()
    df = pd.DataFrame([summary])

    return df


if __name__ == "__main__":
    from extract import my_crypto_summary

    summary = my_crypto_summary()
    if summary:
        df = transform_data(summary)
        print(df)



