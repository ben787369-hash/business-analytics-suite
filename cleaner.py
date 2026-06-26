def clean_data(df):
    # Copier le DataFrame pour préserver l'original
    cleaned_df = df.copy()

    # Remplacement des valeurs manquantes
    for column in cleaned_df.columns:

        # Colonnes numériques
        if cleaned_df[column].dtype in ["int64", "float64"]:
            mean_value = cleaned_df[column].mean()
            cleaned_df[column] = cleaned_df[column].fillna(mean_value)

        # Colonnes texte
        else:
            cleaned_df[column] = cleaned_df[column].fillna("Unknown")

    # Suppression des doublons
    cleaned_df = cleaned_df.drop_duplicates()

    return cleaned_df