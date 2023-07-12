import joblib
import os.path
from services.domain.model_persist import ModelPersist
from sklearn.neighbors import KNeighborsClassifier

class JoblibModelPersist(ModelPersist):
    def save_model(self, model: KNeighborsClassifier) -> bool:
        try:
            print(f'Saving model to file {self.file}')
            joblib.dump(model, self.file)
            print(f'Saving model to file {self.file}. Done!')
            return True
        except Exception as error:
            print(f'Error saving model to file {self.file} {error}')
            return False

    def load_model(self) -> KNeighborsClassifier:
        try:
            print(f'Loading model from file {self.file}')
            model = joblib.load(self.file)
            print(f'Loading model from file {self.file}. Done!')
            return model
        except Exception as error:
            print(f'Error loading model {self.file} file not found {error}')

    def model_exists(self) -> bool:
        return os.path.isfile(self.file)
    