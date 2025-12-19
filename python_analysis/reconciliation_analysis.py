# -*- coding: utf-8 -*-
"""reconciliation_analysis.ipynb

Load Source A & Source B
"""

import pandas as pd

# Load Excel file
file_path = "Data_Reconciliation_Test_Data.xlsx"

source_a = pd.read_excel(file_path, sheet_name="SourceA_Bank_Transactions")
source_b = pd.read_excel(file_path, sheet_name="SourceB_Ledger_Transactions")

print("Source A Records:", len(source_a))
print("Source B Records:", len(source_b))

"""Eligibility rule:

Only SUCCESS transactions participate
"""

eligible_a = source_a[source_a["Status"] == "PROCESSED"]
eligible_b = source_b[source_b["Status"] == "POSTED"]

print("Eligible Source A:", len(eligible_a))
print("Eligible Source B:", len(eligible_b))

"""Merge datasets on Transaction ID"""

recon = eligible_a.merge(
    eligible_b,
    on="Transaction_ID",
    how="outer",
    indicator=True,
    suffixes=("_A", "_B")
)
print("Number of reconciliation records is ",len(recon))
print("Few sample records ",recon.head())

"""Reconciliation Breaks - Missing / Extra Transactions"""

missing_in_ledger = recon[recon["_merge"] == "left_only"]
extra_in_ledger = recon[recon["_merge"] == "right_only"]

print("Missing in Ledger:", len(missing_in_ledger))
print("Extra in Ledger:", len(extra_in_ledger))

"""Amount Mismatch"""

amount_mismatch = recon[
    (recon["_merge"] == "both") &
    (recon["Amount_A"] != recon["Amount_B"])
]

print("Amount Mismatches:", len(amount_mismatch))

"""Summary Metrics"""

summary = {
    "Total Source A": len(source_a),
    "Total Source B": len(source_b),
    "Eligible Source A": len(eligible_a),
    "Eligible Source B": len(eligible_b),
    "Missing in Ledger": len(missing_in_ledger),
    "Extra in Ledger": len(extra_in_ledger),
    "Amount Mismatch": len(amount_mismatch)
}

summary_df = pd.DataFrame(summary.items(), columns=["Metric", "Value"])
print(summary_df)
