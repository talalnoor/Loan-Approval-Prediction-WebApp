from flask import Flask, render_template, request
from src.prediction import predict_loan_status

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    try:
        form_data = {
            'age': float(request.form['age']),
            'gender': request.form['gender'],
            'marital_status': request.form['marital_status'],
            'education': request.form['education'],
            'self_employed': request.form['self_employed'],
            'num_dependents': int(request.form['num_dependents']),
            'employment_years': float(request.form['employment_years']),
            'income_annual': float(request.form['income_annual']),
            'loan_amount': float(request.form['loan_amount']),
            'loan_term_months': int(request.form['loan_term_months']),
            'loan_purpose': request.form['loan_purpose'],
            'credit_score': float(request.form['credit_score']),
            'existing_loans': int(request.form['existing_loans']),
            'residential_assets': float(request.form['residential_assets']),
            'commercial_assets': float(request.form['commercial_assets']),
            'bank_balance': float(request.form['bank_balance']),
            'monthly_expenses': float(request.form['monthly_expenses']),
            'property_area': request.form['property_area'],
        }

        result = predict_loan_status(form_data)

        return render_template('result.html', result=result, form_data=form_data)

    except Exception as e:
        return render_template('index.html', error=f"Something went wrong: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True) 