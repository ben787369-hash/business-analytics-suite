import pandas as pd
import os


def load_file(file_path: str) -> pd.DataFrame:
    """
    Charge un fichier CSV ou Excel de manière robuste.
    """

    # 1. Vérifier existence
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"[ERROR] Fichier introuvable: {file_path}")

    _, ext = os.path.splitext(file_path)
    ext = ext.lower()

    # 2. Excel
    if ext in [".xlsx", ".xls"]:
        try:
            df = pd.read_excel(file_path, engine="openpyxl")
        except Exception as e:
            raise ValueError(f"[ERROR] Impossible de lire Excel: {e}")

    # 3. CSV (cas complexe)
    elif ext == ".csv":
        df = None

        # tentative UTF-8 + virgule
        try:
            df = pd.read_csv(file_path, encoding="utf-8")
        except:
            pass

        # fallback Latin-1
        if df is None:
            try:
                df = pd.read_csv(file_path, encoding="latin1")
            except:
                pass

        # dernier fallback : détection automatique séparateur
        if df is None:
            try:
                df = pd.read_csv(file_path, sep=None, engine="python")
            except Exception as e:
                raise ValueError(f"[ERROR] Impossible de lire CSV: {e}")

    else:
        raise ValueError("[ERROR] Format non supporté (CSV / Excel uniquement)")

    # 4. Vérifier fichier vide
    if df is None or df.empty:
        raise ValueError("[ERROR] Fichier vide ou illisible")

    # 5. Log simple (valeur pro)
    print(f"[OK] Fichier chargé: {file_path}")
    print(f"[INFO] Lignes: {df.shape[0]} | Colonnes: {df.shape[1]}")

    return df