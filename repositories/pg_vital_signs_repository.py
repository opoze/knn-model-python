from sqlalchemy import create_engine, Connection
import pandas as pd
from repositories.domain.vital_signs_repository import VitalSignsRepository

class PGVitalSignsRepository(VitalSignsRepository):
    def __init__(self):
        self.url = 'postgresql+psycopg2://lpozenato:po12ze@localhost:5432/mimic'
        pd.set_option('display.expand_frame_repr', False)
        self.is_connected = False

    def connect(self) -> Connection:
        try:
            print('Connecting to database')
            engine = create_engine(self.url, pool_recycle=3600)
            self.is_connected = True
            return engine.connect()
        except Exception as error:
            self.is_connected = False
            print(f'I am unable to connect to the database {error}')

    def close(self, connection: Connection):
        if self.is_connected:
            print('Closing connection to database')
            connection.close()
            self.is_connected = False
        else:
            print('There is no connection to be closed')

    def run_query(self, query: str) -> pd.DataFrame:
        connection = self.connect()
        data = pd.read_sql(query, connection)
        self.close(connection)

        # Remove index column, features key
        data.columns = range(data.shape[1])
        data.reset_index(drop=True, inplace=True)
        return data

    def get_all(self) -> pd.DataFrame:
        query = 'SELECT heart_rate, temperature, spo2, label FROM mimiciii.vitals;'
        return self.run_query(query)

    def get_random(self, limit: int) -> pd.DataFrame:
        query = (
            'SELECT heart_rate, temperature, spo2 '
            'FROM mimiciii.vitals '
            f'ORDER BY random() LIMIT {limit};'
        )

        return self.run_query(query)
    
    def get_fixture(self) -> pd.DataFrame:
        fixture = [
            [97.0, 36.7, 99.0],
            [82.0, 36.2, 100.0],
            [17.0, 36.6, 93.0],
            [88.0, 37.2, 100.0],
            [75.0, 36.6, 100.0],
            [98.0, 37.1, 96.0],
            [90.0, 37.6, 98.0],
            [82.0, 36.9, 100.0],
            [11.0, 36.2, 97.0],
            [93.0, 36.8, 94.0],
        ]
        return pd.DataFrame(data=fixture)

