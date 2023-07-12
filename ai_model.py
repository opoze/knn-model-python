from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from services.domain.model_persist import ModelPersist
from pandas import DataFrame, Series

MODEL_TRAINING_MSG = 'Training model...'
MODEL_TRAINED_MSG = 'Model trained!'
NO_TRAINING_DATA_MSG = 'No training data found, use model.set_data()'
NO_PREDICT_DATA_MSG = 'No predict data found, use model.set_predict_data()'

class AIModel:
    def __init__(self, persist: ModelPersist = None):
        self.persist = persist
        self.n_neighbors = 3
        self.test_size = 0.3
        self.knn: KNeighborsClassifier = None
        self.X_train: DataFrame = None
        self.X_test: DataFrame = None
        self.y_train: Series = None
        self.y_test: Series = None
        self.y_pred = None
    
    @property
    def exists(self) -> bool:
        if self.persist is not None:
            return self.persist.model_exists()
        
    @property
    def file(self) -> str:
        if self.persist is not None:
            return self.persist.file
    
    def set_data(self, data: DataFrame):
        # São 4 colunas. Heart Rate, Temperature, SpO2, Label
        X = data.drop(data.columns[3], axis=1) # as 3 primeiras
        y = data[data.columns[3]]
        self.split_data(X, y)

    def split_data(self, X: DataFrame, y: Series):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=self.test_size)
 
    def set_predict_data(self, X_test: DataFrame):
        self.X_test = X_test

    def train(self):
        if self.X_train is not None and self.y_train is not None:
            print(MODEL_TRAINING_MSG)
            self.knn = KNeighborsClassifier(n_neighbors=self.n_neighbors)

            self.knn.fit(self.X_train, self.y_train)
            print(MODEL_TRAINED_MSG)
        else:
            print(NO_TRAINING_DATA_MSG)

    def predict(self):
        if self.X_test is not None:
            self.y_pred = self.knn.predict(self.X_test)
            return self.y_pred
        else:
            print(NO_PREDICT_DATA_MSG)
    
    def save(self) -> bool:
        if self.persist is not None:
            self.persist.save_model(self.knn)
            return True
        
        return False

    def load(self) -> bool:
        if self.persist is not None:
            self.knn = self.persist.load_model()
            return True

        return False

    def get_test_data(self):
        return self.X_test, self.y_test

    def get_predicted_data(self):
        return self.y_pred