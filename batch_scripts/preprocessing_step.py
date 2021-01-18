import os
import pickle
import joblib
import argparse
from azureml.core.run import Run
from azureml.core.model import Model

# load data
run = Run.get_context()
data = run.input_datasets['input_dataset'].to_pandas_dataframe()

# load model
ws = run.experiment.workspace
# model = Model(ws, 'german-credit-local-model').download(exist_ok=True)
pipeline_path = Model.get_model_path('german-credit-local-model')
pipeline = joblib.load(pipeline_path)

# preprocess
data.drop("Sno", axis=1, inplace=True)
X_raw = data.drop('Risk', axis=1)
out = pipeline['preprocessor'].transform(X_raw)

# save intermediate file
parser = argparse.ArgumentParser("preprocess")
parser.add_argument("--intermediate-data-path", type=str)
args = parser.parse_args()
if args.intermediate_data_path is not None:
    os.makedirs(args.intermediate_data_path, exist_ok=True)
    print(f"{args.intermediate_data_path} created")
pickle.dump(out, open(f"{args.intermediate_data_path}/preprocessed_features.pkl", "wb" ) )
data.to_csv(f'{args.intermediate_data_path}/preprocessed_data.csv', index=False)