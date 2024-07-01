import xgboost
import pandas as pd
from sklearn.model_selection import train_test_split

from ..interfaces import TrainingModel


class LinearRegression(TrainingModel):
    def prepare_sets(self, dataset):
        diamonds_processed_xgb = dataset.copy()
        diamonds_processed_xgb['cut'] = pd.Categorical(diamonds_processed_xgb['cut'], categories=['Fair', 'Good', 'Very Good', 'Ideal', 'Premium'], ordered=True)
        diamonds_processed_xgb['color'] = pd.Categorical(diamonds_processed_xgb['color'], categories=['D', 'E', 'F', 'G', 'H', 'I', 'J'], ordered=True)
        diamonds_processed_xgb['clarity'] = pd.Categorical(diamonds_processed_xgb['clarity'], categories=['IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1'], ordered=True)
        # diamonds_processed_xgb.info()

        self.x_train_xbg, self.x_test_xbg, self.y_train_xbg, self.y_test_xbg = train_test_split(diamonds_processed_xgb.drop(columns='price'), diamonds_processed_xgb['price'], test_size=0.2, random_state=42)

    def train(self):
        self.model = xgboost.XGBRegressor(enable_categorical=True, random_state=42)
        self.model.fit(self.x_train_xbg, self.y_train_xbg)

    def predict(self):
        self.prediction = self.model.predict(self.x_test_xbg)
