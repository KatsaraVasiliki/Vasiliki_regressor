import pandas as pd
import os
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import median_absolute_error
from sklearn.metrics import mean_absolute_percentage_error


def evaluate_model_NoSMRTNoTfl(dnn, preprocessed_train_split_X, preproc_test_split_y, preproc_y, fold, features,experiment, X):
    preproc_y_preds = dnn.predict(preprocessed_train_split_X, verbose=0)
    test_split_y = preproc_y.inverse_transform(preproc_test_split_y.reshape(-1, 1)).flatten()
    y_preds = preproc_y.inverse_transform(preproc_y_preds.reshape(-1, 1)).flatten()
    # This dictionary creates the evaluation results
    evaluation_dictionary = {
        'mae': mean_absolute_error(test_split_y, y_preds),
        'medae': median_absolute_error(test_split_y, y_preds),
        'mape': mean_absolute_percentage_error(test_split_y, y_preds),
        'fold': fold,
        'features': features,
        'experiment_number': experiment,
        'dataset size': X.shape[0]
    }

    # Convert results dictionary to DataFrame, so it can be easily saved as a csv file
    results_df = pd.DataFrame([evaluation_dictionary])

    # Save the DataFrame to CSV
    if not os.path.exists("./results_NoSMRTNoTfl/evaluation_results_NoSMRTNoTfl.txt"):
        # If the file doesn't exist, set header=True
        results_df.to_csv("./results_NoSMRTNoTfl/evaluation_results_NoSMRTNoTfl.txt", index=False, header=True)
    else:
        # If the file exists, set header=False
        results_df.to_csv("./results_NoSMRTNoTfl/evaluation_results_NoSMRTNoTfl.txt", index=False, header=False, mode='a')

    print(f"Evaluation results have been saved into ./results_nSMRTntf/evaluation_results_NoSMRTNoTfl.txt")