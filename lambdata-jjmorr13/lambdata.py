import pandas as pd 
import numpy as np 
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels

def hello():
    print('Hello World')


def train_val_test(df, target):
    '''
    This takes a dataframe and returns a train, validation, and test dataframes
    The train set is 60% of the data, while validation and test set are 20% each
    Proper use of function = " train, val, test = train_val_test(df, 'target') "
    '''
    # Sklearn to split train and test 80/20, stratify on target
    train, test = train_test_split(train, test_size=0.2, train_size=0.8, 
                                    stratify=train[target], random_state=42)
    
    # Split train and validation 60/20 from original size, stratify on target
    train, val = train_test_split(train, test_size=0.25, train_size=0.75,
                                    stratify=train[target], random_state=42)
    
    return train, val, test


def plot_confusion_matrix(y_true, y_pred):
    '''
    Returns a seaborn heatmap with labels from the y_true values
    Useful for visualizing precision and recall from classification regression

    '''
    # Create labels based off y_true values
    labels = unique_labels(y_true)

    # Predicted value labels on the x axis
    columns = [f'Predicted {label}' for label in labels]

    # Actual value labels on the y axis
    index = [f'Actual {label}' for label in labels]

    # Forms the df
    table = pd.DataFrame(confusion_matrix(y_true, y_pred), 
                         columns=columns, index=index)

    # Returns heatmap with no decimals and virids colors
    return sns.heatmap(table, annot=True, fmt='.0f', cmap='viridis')