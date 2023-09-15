import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

data_frame = pd.read_csv('static/mushrooms.csv')
characteristic = data_frame[['class', 'cap-color', 'cap-shape', 'cap-surface', 'bruises', 'habitat']]


def main(cc, cs, csur, b, h):
    keys = characteristic.loc[
        (characteristic['cap-color'] == cc) &
        (characteristic['cap-shape'] == cs) &
        (characteristic['cap-surface'] == csur) &
        (characteristic['bruises'] == b) &
        (characteristic['habitat'] == h)
        ]
    return keys


# To transform data from nominal (categorical) to ordinal (numerical).
LE = LabelEncoder()
for column in characteristic.columns:
    characteristic[column] = LE.fit_transform(characteristic[column])


def classify(userSelection):
    try:
        # Excluding the 'class' column from a DataFrame chosen by the user.
        X = userSelection.drop(['class'], axis=1)
        Y = userSelection["class"]
        # Preparing the training and testing datasets.
        X_train, X_test, Y_train, Y_test = train_test_split(
            X, Y, random_state=42, test_size=.2, train_size=.8)
        random_forest = RandomForestClassifier(n_estimators=50, random_state=42)
        random_forest.fit(X_train, Y_train)
        # Accuracy score to measures the proportion of correctly
        # predicted instances (both true positives and true negatives)
        # out of the total number of instances in the dataset.
        accuracy = round(random_forest.score(X_test, Y_test) * 100, 2)
        forecast = list(random_forest.predict(X_test))
        if forecast[0] == 1:
            predictedClass = 'toxic '
        else:
            predictedClass = 'non-toxic '
        predictions = int(len(forecast))
        message = "This class prediction is {}".format(predictedClass) + "and the accuracy result was {}% ".format(
            accuracy) + "valid for {}".format(predictions) + " samples. To try a different combinations, click the back arrow."
        if predictions > 0:
            return message
        else:
            return 'Sorry, there are not enough data. Try again.'
    except ValueError:
        return 'Sorry, there are no matching results, please try different combinations.'
