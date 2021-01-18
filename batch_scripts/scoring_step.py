import os
import pickle
import joblib
import argparse
import pandas as pd
from azureml.core.run import Run
from azureml.core.model import Model
from sklearn.preprocessing import LabelEncoder

# load arguments
parser = argparse.ArgumentParser("preprocess")
parser.add_argument("--intermediate-data-path", type=str)
parser.add_argument("--result-data-path", type=str)
args = parser.parse_args()

# load data
run = Run.get_context()
print(args.intermediate_data_path)
features = pickle.load(open(f'{args.intermediate_data_path}/preprocessed_features.pkl', "rb"))
data = pd.read_csv(f'{args.intermediate_data_path}/preprocessed_data.csv')

# load model
ws = run.experiment.workspace
# model = Model(ws, 'german-credit-local-model').download(exist_ok=True)
pipeline_path = Model.get_model_path('german-credit-local-model')
pipeline = joblib.load(pipeline_path)

# score
out = pipeline['classifier'].predict(features)

# save result file

if args.result_data_path is not None:
    os.makedirs(args.result_data_path, exist_ok=True)
    print(f"{args.result_data_path} created")
le = LabelEncoder()
le.fit(data['Risk'])
data['prediction'] = le.inverse_transform(out)
data.to_csv(f'{args.result_data_path}/result_data.csv', index=False)