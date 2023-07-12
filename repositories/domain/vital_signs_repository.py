from abc import ABC, abstractmethod
from pandas import DataFrame

class VitalSignsRepository(ABC):
    def print_columns(dataFrame: DataFrame):
        print('Column headings:')
        print(dataFrame.columns)

    def print_head(dataFrame: DataFrame):
        print('First 5 rows:')
        print(dataFrame.head())

    @abstractmethod
    def get_all(self) -> DataFrame: pass

    @abstractmethod
    def get_random(self, limit: int) -> DataFrame: pass

    @abstractmethod
    def get_fixture(self) -> DataFrame: pass
