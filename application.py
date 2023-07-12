import json
from ai_model import AIModel
from services.metrics import Metrics
from services.plot import Plot
from repositories.pg_vital_signs_repository import PGVitalSignsRepository
from services.joblib_model_persist import JoblibModelPersist

ASK_TO_USE_FIXTURE_DATA_MSG = (
    'Use fixture data to predict otherwise random data from database will be used? (y/n)'
)
ASK_TO_SAVE_MODEL_MSG = 'Save model? (y/n)'
ASK_TO_SHOW_METRICS_MSG = 'Show metrics? (y/n)'
ASK_TO_SHOW_PLOT_MSG = 'Show plot? (y/n)'
ASK_TO_USE_PRE_TRAINED_MODEL_FOUND_MSG = 'Pre trained model found in {f}, use it? (y/n)'

USING_FIXTURE_MSG = 'Using fixture to predict...'
USING_RANDOM_DATABASE_DATA_MSG = 'Using random data from database to predict...'
RETRIEVING_ALL_VITAL_SIGNS_MSG = 'Retrieving all vital signs from database...'


class Application:
    def __init__(self):
        self.model = AIModel(JoblibModelPersist())
        self.repository = PGVitalSignsRepository()

    def ask(self, message: str) -> bool:
        answer = input(message)
        return answer.lower() == 'y'

    def run(self):
        ask = ASK_TO_USE_PRE_TRAINED_MODEL_FOUND_MSG.replace(
            '{f}', self.model.file)
        if self.model.exists and self.ask(ask):
            self.model.load()
            self.use_trained_model()
        else:
            self.handle_untrained_model()
            self.show_training_metrics()

        self.show_plot()

    def use_trained_model(self):
        if self.ask(ASK_TO_USE_FIXTURE_DATA_MSG):
            print(USING_FIXTURE_MSG)
            data = self.repository.get_fixture()
            print(json.dumps(data.to_dict(), indent=4))
        else:
            print(USING_RANDOM_DATABASE_DATA_MSG)
            data = self.repository.get_random(10)
            print(json.dumps(data.to_dict(), indent=4))

        self.model.set_predict_data(data)
        self.model.predict()

    def handle_untrained_model(self):
        print(RETRIEVING_ALL_VITAL_SIGNS_MSG)

        data = self.repository.get_all()

        self.model.set_data(data)
        self.model.train()
        self.model.predict()

        if self.ask(ASK_TO_SAVE_MODEL_MSG):
            self.model.save()

    def show_training_metrics(self):
        if self.ask(ASK_TO_SHOW_METRICS_MSG):
            metrics = Metrics(self.model.get_test_data()
                              [1], self.model.predict())
            metrics.calculate()

    def show_plot(self):
        if self.ask(ASK_TO_SHOW_PLOT_MSG):
            plot = Plot(self.model)
            plot.show()
