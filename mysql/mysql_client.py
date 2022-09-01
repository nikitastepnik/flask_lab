import sqlalchemy
from sqlalchemy.orm import sessionmaker


class MySqlClient:

    def __init__(self, db_name, user, password):
        self.user = user
        self.port = 3306
        self.password = password
        self.host = '0.0.0.0'
        self.db_name = db_name

        self.connection = None
        self.engine = None
        self.session = None

    def connect(self):
        url = f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}'
        self.engine = sqlalchemy.create_engine(url)
        self.connection = self.engine.connect()

        session = sessionmaker(bind=self.connection.engine)
        self.session = session()
