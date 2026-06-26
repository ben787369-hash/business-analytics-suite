def generate_insights(report, df):

    insights = []

    # Dataset size
    insights.append(
        f"The dataset contains {report['rows']} rows and {report['columns']} columns."
    )

    # Missing values
    missing = report["missing_percent"]

    for column, percent in missing.items():

        if percent > 50:
            insights.append(
                f"Column '{column}' contains {percent:.2f}% missing values (critical issue)."
            )

        elif percent > 0:
            insights.append(
                f"Column '{column}' contains {percent:.2f}% missing values."
            )

    # Duplicates
    if report["duplicates"] == 0:
        insights.append(
            "No duplicate records were detected."
        )
    else:
        insights.append(
            f"{report['duplicates']} duplicate record(s) were detected."
        )

    # Negative profits
    if "Profit" in df.columns:

        negative_profit = (df["Profit"] < 0).sum()

        if negative_profit > 0:
            insights.append(
                f"{negative_profit} transactions generated a negative profit."
            )

    # High discounts
    if "Discount" in df.columns:

        high_discount = (df["Discount"] > 0.50).sum()

        if high_discount > 0:
            insights.append(
                f"{high_discount} transactions have discounts greater than 50%."
            )

    return insights