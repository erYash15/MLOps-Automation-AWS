import numpy as np
import pandas as pd
import warnings

# Ignore all warnings
warnings.filterwarnings("ignore")

class DataPreprocessor:
    def __init__(self, train_file):
        self.train = pd.read_csv(train_file)

    def handle_missing_values(self):
        # Dropping the 'Cabin' column due to too many null values
        self.train.drop(columns=['Cabin'], inplace=True)

        # Handling missing values in 'Embarked'
        self.train['Embarked'].fillna('S', inplace=True)

        # Fill missing 'Age' values based on median age grouped by Sex and Pclass then full median
        self.train['Age'] = self.train.groupby(['Sex', 'Pclass'])['Age'].transform(lambda x: x.fillna(x.median()))
        self.train['Age'].fillna(self.train['Age'].median(), inplace=True)


    def extract_titles(self):
        self.train['Title'] = self.train['Name'].str.split(", ", expand=True)[1].str.split(".", expand=True)[0]
        self.train['Title'] = self.train['Title'].replace(
            ['Lady', 'the Countess', 'Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
        self.train['Title'] = self.train['Title'].replace(['Mlle', 'Ms', 'Mme'], 'Miss')

    def create_family_size_column(self):
        self.train['Family_size'] = self.train['SibSp'] + self.train['Parch'] + 1
        self.train['Family_size'] = self.train['Family_size'].apply(self.family_size)

    def family_size(self, number):
        if number == 1:
            return "Alone"
        elif number > 1 and number < 5:
            return "Small"
        else:
            return "Large"

    def drop_unnecessary_columns(self):
        self.train.drop(columns=['Name', 'Parch', 'SibSp', 'Ticket'], inplace=True)

    def preprocess_data(self):
        self.handle_missing_values()
        self.extract_titles()
        self.create_family_size_column()
        self.drop_unnecessary_columns()
        return self.train

# Example usage:
preprocessor = DataPreprocessor('data/train.csv')
processed_df = preprocessor.preprocess_data()
print(processed_df.head())
