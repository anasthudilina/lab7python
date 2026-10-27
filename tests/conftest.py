import pytest
from collections.abc import Iterator  # <--- ДОДАЙ ЦЕЙ РЯДОК
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from bank_app.models import Base

@pytest.fixture
def session() -> Iterator[Session]:  # <--- ЗМІНИ ТИП НА Iterator[Session]
    # Використовуємо in-memory базу для тестів (ізоляція)
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    TestSession = sessionmaker(bind=engine, expire_on_commit=False)
    
    with TestSession() as sess:
        yield sess
        
    Base.metadata.drop_all(engine)