import joblib
from src.preprocessing import preprocess_input

# Load the trained model once when this module is imported
# (not inside the function — loading from disk is slow, we only want to do it once)
MODEL = joblib.load('model/model.pkl')


def predict_loan_status(form_data):
    """
    Takes raw form input, preprocesses it, and returns a prediction
    with a confidence score.

    Returns a dictionary:
    {
        'prediction': 'Approved' or 'Rejected',
        'confidence': float (e.g. 87.3, meaning 87.3% confident),
        'approved_probability': float,
        'rejected_probability': float
    }
    """
    # Transform raw input into the model's expected format
    processed_df = preprocess_input(form_data)

    # predict() gives the class (0 or 1)
    prediction = MODEL.predict(processed_df)[0]

    # predict_proba() gives probability for each class: [P(class=0), P(class=1)]
    probabilities = MODEL.predict_proba(processed_df)[0]
    rejected_prob = probabilities[0]
    approved_prob = probabilities[1]

    # The confidence score is the probability of whichever class was predicted
    confidence = max(rejected_prob, approved_prob) * 100

    result = {
        'prediction': 'Approved' if prediction == 1 else 'Rejected',
        'confidence': round(confidence, 2),
        'approved_probability': round(approved_prob * 100, 2),
        'rejected_probability': round(rejected_prob * 100, 2)
    }

    return result