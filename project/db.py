from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column

engine = create_engine(
    "postgresql+psycopg2://postgres:admin@localhost:5432/internet_store",
    echo=True
    )


Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class ItemsORM(Base):

    __tablename__ = "items"

    id : Mapped[int] = mapped_column(primary_key=True)
    creator : Mapped[str]
    model : Mapped[str]
    category : Mapped[str]
    price : Mapped[int]

Base.metadata.create_all(engine)

