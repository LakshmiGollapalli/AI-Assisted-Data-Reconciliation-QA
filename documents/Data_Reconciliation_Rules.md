# Data Reconciliation Rules

## Scope
This document defines the rules used to reconcile bank transaction data (Source A) with ledger data (Source B).

## Eligibility Criteria
- Only Source A transactions with Status = PROCESSED are eligible for reconciliation.
- FAILED transactions must not be considered.

## Matching Keys
- Transaction_ID
- Account_Number

## Validation Rules
1. Transaction_ID must exist in both sources.
2. Account_Number must match between Source A and Source B.
3. Amount must be equal in both sources.
4. Currency must be the same.
5. Source A Transaction_Type must be DEBIT.
6. Source B Transaction_Type must be CREDIT.

## Exception Handling
- Transactions present in Source A but missing in Source B should be flagged as **Missing in Ledger**.
- Transactions present in Source B but missing in Source A should be flagged as **Extra in Ledger**.
- Transactions with amount mismatch should be flagged as **Amount Mismatch**.

## Output
A reconciliation result report must categorize records as:
- MATCHED
- AMOUNT_MISMATCH
- MISSING_IN_LEDGER
- EXTRA_IN_LEDGER
