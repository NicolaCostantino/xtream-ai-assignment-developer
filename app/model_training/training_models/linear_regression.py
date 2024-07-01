from sklearn.model_selection import train_test_split

from ..interfaces import TrainingModel


class LinearRegression(TrainingModel):
    def prepare_sets(self, dataset):
        x = dataset.drop(columns='price')
        y = dataset.price

        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    def train(self):
        self.model = LinearRegression()
        self.model.fit(self.x_train, self.y_train)

    def predict(self):
        self.prediction = self.model.predict(self.x_test)
