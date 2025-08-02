import pandas as pd
from datetime import datetime, timezone


def transform_data(summary):
    # Coordinated Universal Time (UTC) and format it into an ISO 8601 string
    summary["transformed_at"] = datetime.now(timezone.utc).isoformat()
    df = pd.DataFrame([summary])

    return df



