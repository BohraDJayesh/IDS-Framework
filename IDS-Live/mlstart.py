import joblib
import sklearn
import sys
import sklearn
from sklearn.preprocessing import _data
import Preprocessing
import pandas as pd
import numpy as np

model = joblib.load('/Users/jayeshduttbohra/Desktop/JD/Projects/IDS-Framework/Model Traning/Model/webattack_detection_rf_model.pkl')


#Same steps for pre-processing as it was for ml-training.

def colPreprocessing(dfo):
    #Deleting blank records
    #dfo = dfo.drop(dfo[pd.isnull(dfo['Flow ID'])].index)

    #Replace the non-numeric values.
    dfo.replace('infinity', -1, inplace=True)
    dfo[["flow bytes/s", "flow packets/s"]] = dfo[["flow bytes/s", "flow packets/s"]].apply(pd.to_numeric)

    # Replacing NAN and infity values with -1.
    dfo.replace([np.inf, -np.inf, np.nan], -1, inplace=True)

    # Converting String character to numericals.
    string_features = list(dfo.select_dtypes(include=['object']).columns)

    excluded = ['source ip', 'destination ip', 'source port', 'destination port', 'protocol', 'timestamp']
    dfo = dfo.drop(columns=excluded, errors='ignore')

    #Taking importang columns rest are droping out.

    columns_to_keep = ['Average Packet Size', 'Flow Bytes/s', 'Max Packet Length',
                    'Fwd Packet Length Mean', 'Fwd IAT Min',
                    'Total Length of Fwd Packets', 'Flow IAT Mean',
                    'Fwd Packet Length Max', 'Fwd IAT Std', 'Fwd Header Length']
    columns_to_keep = [item.lower() for item in columns_to_keep]

   # df = [item.lower() for item in excluded]

    df = dfo[columns_to_keep]
    return df

def predict(df):
    predictions = model.predict(df)
    return predictions