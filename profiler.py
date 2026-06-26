def profile_data(df):
    report = {}

    # Nombre de lignes et colonnes
    report["rows"] = df.shape[0]
    report["columns"] = df.shape[1]

    # Valeurs manquantes (nombre)
    report["missing_count"] = df.isnull().sum()

    # Valeurs manquantes (pourcentage)
    report["missing_percent"] = (
        (df.isnull().sum() / len(df)) * 100
    ).round(2)

    # Types des colonnes
    report["types"] = df.dtypes

    # Doublons
    report["duplicates"] = df.duplicated().sum()

    return report