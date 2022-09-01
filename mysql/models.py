from sqlalchemy import Column, SMALLINT, CHAR, FLOAT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TableElements(Base):
    __tablename__ = 'elements'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"" \
               f"{self.n1} " \
               f"{self.n2} " \
               f"{self.n3}" \
               f""

    id = Column(SMALLINT, primary_key=True, autoincrement=True, default=0)
    n1 = Column(SMALLINT, default=0)
    n2 = Column(SMALLINT, default=0)
    n3 = Column(SMALLINT, default=0)
    props = Column(CHAR(12), default='steel')


class TableNodes(Base):
    __tablename__ = 'nodes'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"" \
               f"{self.x}," \
               f"{self.y}" \
               f""

    id = Column(SMALLINT, primary_key=True, autoincrement=True, default=0)
    x = Column(FLOAT, default=0)
    y = Column(FLOAT, default=0)
