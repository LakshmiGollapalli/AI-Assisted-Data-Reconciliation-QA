# Data Reconciliation Test Scenarios

## TS_01 – Validate successful reconciliation for matching transactions
Verify that Source A PROCESSED transactions with matching records in Source B are marked as MATCHED.

## TS_02 – Validate amount mismatch handling
Verify that transactions with different amounts in Source A and Source B are flagged as AMOUNT_MISMATCH.

## TS_03 – Validate missing ledger transactions
Verify that PROCESSED transactions present in Source A but missing in Source B are flagged as MISSING_IN_LEDGER.

## TS_04 – Validate extra ledger transactions
Verify that transactions present in Source B but missing in Source A are flagged as EXTRA_IN_LEDGER.

## TS_05 – Validate exclusion of FAILED transactions
Verify that FAILED transactions in Source A are excluded from reconciliation.

## TS_06 – Validate currency consistency
Verify that transactions with mismatched currency values are flagged correctly.

## TS_07 – Validate transaction type mapping
Verify that DEBIT transactions in Source A are mapped to CREDIT transactions in Source B.

## TS_08 – Validate reconciliation result summary
Verify that reconciliation output provides correct counts for matched and exception records.

