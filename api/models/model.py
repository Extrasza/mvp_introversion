import pickle
import pandas as pd

class Model:
    def __init__(self):
        with open("models/model.pkl", "rb") as f:
            self.clf = pickle.load(f)

        with open("scalers/scaler.pkl", "rb") as f:
            self.scaler = pickle.load(f)

        self.expected_columns = [
            'Time_spent_Alone',
            'Social_event_attendance',
            'Going_outside',
            'Friends_circle_size',
            'Post_frequency',
            'Stage_fear',
            'Drained_after_socializing'
        ]

    def predict_personality(self, data_dict):
        df = pd.DataFrame([data_dict])

        for col in ['Stage_fear', 'Drained_after_socializing']:
            val = df[col].iloc[0]
            if isinstance(val, str):
                df[col] = 1 if val.strip().lower() in ['true', '1', 'yes', 'sim'] else 0
            else:
                df[col] = int(val)

        df = df[self.expected_columns]

        scaled_array = self.scaler.transform(df)
        scaled_df = pd.DataFrame(scaled_array, columns=self.expected_columns)
        prediction = self.clf.predict(scaled_df)[0]

        return "Introvertido" if prediction == 0 else "Extrovertido"