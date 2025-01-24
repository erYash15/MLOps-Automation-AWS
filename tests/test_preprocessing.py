import unittest
import pandas as pd
from unittest.mock import patch
from preprocessing.data_processor import DataPreprocessor

class TestDataPreprocessor(unittest.TestCase):

    @patch('pandas.read_csv')  # Mock pandas read_csv method
    def setUp(self, mock_read_csv):
        # Set up a small test dataset for unit tests
        data = {
            'PassengerId': [1, 2, 3, 4],
            'Survived': [0, 1, 1, 0],
            'Pclass': [3, 1, 3, 2],
            'Name': ['Braund, Mr. Owen Harris', 'Cumings, Mrs. John Bradley', 'Heikkinen, Miss. Laina', 'Futrelle, Mrs. Jacques Heath'],
            'Sex': ['male', 'female', 'female', 'female'],
            'Age': [22, 38, 26, None],
            'SibSp': [1, 1, 0, 1],
            'Parch': [0, 0, 0, 0],
            'Ticket': ['A/5 21171', 'PC 17599', 'STON/O2. 3101282', '113803'],
            'Fare': [7.25, 71.2833, 7.925, 53.1],
            'Cabin': [None, 'C85', None, 'C123'],
            'Embarked': ['S', 'C', 'S', 'S']
        }
        # Set the return value of the mock to be the mock DataFrame
        mock_read_csv.return_value = pd.DataFrame(data)

        # Initialize the preprocessor
        self.preprocessor = DataPreprocessor(train_file=None)
        self.preprocessor.train = self.preprocessor.train.copy()

    def test_handle_missing_values(self):
        # Ensure that missing 'Age' and 'Embarked' columns are filled properly
        self.preprocessor.handle_missing_values()

        # Test if missing values in 'Age' are filled
        self.assertEqual(self.preprocessor.train['Age'].isnull().sum(), 0)

        # Test if missing values in 'Embarked' are filled with 'S'
        self.assertEqual(self.preprocessor.train['Embarked'].isnull().sum(), 0)

    def test_extract_titles(self):
        self.preprocessor.extract_titles()

        # Test that the 'Title' column is created correctly
        self.assertIn('Title', self.preprocessor.train.columns)

        # Check if the titles are correctly replaced
        self.assertEqual(self.preprocessor.train['Title'].iloc[0], 'Mr')
        self.assertEqual(self.preprocessor.train['Title'].iloc[1], 'Mrs')
        self.assertEqual(self.preprocessor.train['Title'].iloc[2], 'Miss')
        self.assertEqual(self.preprocessor.train['Title'].iloc[3], 'Mrs')

    def test_create_family_size_column(self):
        self.preprocessor.create_family_size_column()

        # Test if the 'Family_size' column is created
        self.assertIn('Family_size', self.preprocessor.train.columns)

        # Check if the 'Family_size' is categorized properly
        self.assertEqual(self.preprocessor.train['Family_size'].iloc[0], 'Small')
        self.assertEqual(self.preprocessor.train['Family_size'].iloc[1], 'Small')
        self.assertEqual(self.preprocessor.train['Family_size'].iloc[2], 'Alone')
        self.assertEqual(self.preprocessor.train['Family_size'].iloc[3], 'Small')

    def test_drop_unnecessary_columns(self):
        self.preprocessor.drop_unnecessary_columns()

        # Check if unnecessary columns are dropped
        self.assertNotIn('Name', self.preprocessor.train.columns)
        self.assertNotIn('Parch', self.preprocessor.train.columns)
        self.assertNotIn('SibSp', self.preprocessor.train.columns)
        self.assertNotIn('Ticket', self.preprocessor.train.columns)

    def test_preprocess_data(self):
        # Run the full preprocessing pipeline
        processed_df = self.preprocessor.preprocess_data()

        # Test if the final dataframe contains all expected columns
        self.assertIn('Title', processed_df.columns)
        self.assertIn('Family_size', processed_df.columns)

        # Test if there are no missing values in 'Age' and 'Embarked'
        self.assertEqual(processed_df['Age'].isnull().sum(), 0)
        self.assertEqual(processed_df['Embarked'].isnull().sum(), 0)
        
        # Test if unnecessary columns are dropped
        self.assertNotIn('Name', processed_df.columns)
        self.assertNotIn('Parch', processed_df.columns)
        self.assertNotIn('SibSp', processed_df.columns)
        self.assertNotIn('Ticket', processed_df.columns)

if __name__ == '__main__':
    unittest.main()
