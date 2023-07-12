from abc import ABC, abstractmethod

class ModelPersist(ABC):
    def __init__(self, file_name=None, file_location=None):
        if file_location:
            self.file_location = file_location
        else:
            self.file_location = 'out/'

        if file_name:
            self.file_name = file_name
        else:
            self.file_name = 'knn_serialized_model'

    @property
    def file(self):
        return f'{self.file_location}{self.file_name}'   

    @abstractmethod
    def save_model(self, data: any, file_name: str) -> bool : pass

    @abstractmethod
    def load_model(self, file_name: str) -> any: pass

    @abstractmethod
    def model_exists(self, file_name: str) -> bool: pass

