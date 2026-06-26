from loader import load_file
from profiler import profile_data
from cleaner import clean_data
from visualizer import create_missing_chart, create_profit_chart
from insights import generate_insights
from report_generator import generate_pdf


def run(file_path):

    # Chargement
    df = load_file(file_path)

    # Analyse
    report = profile_data(df)

    # Nettoyage
    cleaned_df = clean_data(df)

    # =========================
    # BUSINESS STATISTICS
    # =========================

    if "Sales" in df.columns:
        total_sales = df["Sales"].sum()
    else:
        total_sales = None

    if "Profit" in df.columns:
        total_profit = df["Profit"].sum()
    else:
        total_profit = None

    if "Category" in df.columns and "Profit" in df.columns:
        category_profit = df.groupby("Category")["Profit"].sum()
    else:
        category_profit = None

    # =========================
    # GRAPHIQUES
    # =========================

    create_missing_chart(report)

    if "Category" in df.columns and "Profit" in df.columns:
        create_profit_chart(df)

    # Insights
    insights = generate_insights(report, df)

    # PDF
    generate_pdf(
    report,
    insights,
    total_sales,
    total_profit
)

    # Affichage
    print("\n===== DATASET REPORT =====")

    print(f"Lignes : {report['rows']}")
    print(f"Colonnes : {report['columns']}")

    print("\nValeurs manquantes :")
    print(report["missing_count"])

    print("\nPourcentages de valeurs manquantes :")
    print(report["missing_percent"])

    print("\nTypes :")
    print(report["types"])

    print("\nDoublons :")
    print(report["duplicates"])

    print("\n===== BUSINESS STATISTICS =====")

    if total_sales is not None:
        print(f"Total sales : {total_sales:.2f}")

    if total_profit is not None:
        print(f"Total profit : {total_profit:.2f}")

    if category_profit is not None:
        print("\nProfit by category :")
        print(category_profit)

    print("\n===== CLEANED DATA =====")
    print(cleaned_df)

    print("\n===== INSIGHTS =====")

    for insight in insights:
        print("-", insight)

    print("\nGraphiques enregistrés :")
    print("- missing_values.png")
    print("- profit_by_category.png")

    print("PDF enregistré : report.pdf")