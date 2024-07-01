from abc import ABC, abstractmethod


class TrainingModel(ABC):

    @abstractmethod
    def prepare_sets(self, dataset):
        pass

    @abstractmethod
    def train(self):
        pass

    @abstractmethod
    def predict(self):
        pass