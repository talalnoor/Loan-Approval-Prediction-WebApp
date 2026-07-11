import pandas as pd
import joblib

# Load the exact column structure the model expects (order matters!)
MODEL_COLUMNS = joblib.load('model/model_columns.pkl')


def credit_band(score):
    """Bucket a numeric credit score into a category, same logic as training."""
    if score < 500:
        return 'Poor'
    elif score < 650:
        return 'Fair'
    elif score < 750:
        return 'Good'
    else:
        return 'Excellent'


def preprocess_input(form_data):
    """
    Takes a dictionary of raw form input and transforms it into the
    exact encoded dataframe format the trained model expects.

    form_data example:
    {
        'age': 35, 'gender': 'Male', 'marital_status': 'Married',
        'education': 'Graduate', 'self_employed': 'No',
        'num_dependents': 2, 'employment_years': 5,
        'income_annual': 60000, 'loan_amount': 200000,
        'loan_term_months': 120, 'loan_purpose': 'Home',
        'credit_score': 720, 'existing_loans': 1,
        'residential_assets': 300000, 'commercial_assets': 0,
        'bank_balance': 50000, 'monthly_expenses': 3000,
        'property_area': 'Urban'
    }
    """
    df = pd.DataFrame([form_data])

    # Feature engineering (identical formulas to training)
    df['debt_to_income'] = df['loan_amount'] / df['income_annual']
    df['total_assets'] = (df['residential_assets'] +
                           df['commercial_assets'] +
                           df['bank_balance'])
    df['asset_to_loan_ratio'] = df['total_assets'] / df['loan_amount']
    df['monthly_income'] = df['income_annual'] / 12
    df['expense_ratio'] = df['monthly_expenses'] / df['monthly_income']
    df['credit_score_band'] = df['credit_score'].apply(credit_band)

    # Ordinal encode education
    education_order = {'Not Graduate': 0, 'Graduate': 1, 'Post Graduate': 2}
    df['education_encoded'] = df['education'].map(education_order)

    # One-hot encode nominal categoricals (same columns as training)
    nominal_cols = ['gender', 'marital_status', 'self_employed', 'loan_purpose',
                     'property_area', 'credit_score_band']
    df_encoded = pd.get_dummies(df, columns=nominal_cols)

    # Drop the original education column (we kept the encoded version)
    df_encoded = df_encoded.drop(columns=['education'])

    # CRITICAL STEP: force the dataframe to have exactly the columns
    # the model was trained on, in the right order. Any column missing
    # from this single-row input (e.g. gender_Female wasn't created because
    # this user is Male) gets added and filled with 0.
    df_final = df_encoded.reindex(columns=MODEL_COLUMNS, fill_value=0)

    return df_final