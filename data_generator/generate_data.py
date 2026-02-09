import numpy as np
import pandas as pd

np.random.seed(42)

n = 500

data = {
    "daily_riyaz_hours": np.round(np.random.uniform(0.5, 6, n), 2),
    "taal_discipline_score": np.random.randint(1, 11, n),
    "swara_accuracy": np.random.randint(1, 11, n),
    "bandish_repertoire": np.random.randint(1, 25, n),
    "alaap_consistency": np.random.randint(1, 11, n),
    "layakari_comfort": np.random.randint(1, 11, n),
    "past_jury_marks": np.random.randint(40, 100, n)
}

df = pd.DataFrame(data)

readiness_score = (
    df["daily_riyaz_hours"] * 2 +
    df["swara_accuracy"] +
    df["taal_discipline_score"] +
    df["alaap_consistency"] +
    df["layakari_comfort"] +
    df["past_jury_marks"] / 20
)

df["ready"] = (readiness_score > np.median(readiness_score)).astype(int)

print(df.head())
