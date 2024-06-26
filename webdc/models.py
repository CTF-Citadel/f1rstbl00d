# models.py
from sqlalchemy import Column, Integer, DateTime, Boolean, String, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class FirstBlood(Base):
    """
    Model for the FirstBlood table

    This table stores the first bloods of all challenges which are submitted with a unique contrainst on the event_id and challenge_id
    """

    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, nullable=False)
    username = Column(String, nullable=False)
    event_id = Column(String, nullable=False)
    challenge_id = Column(String, nullable=False)
    challenge_name = Column(String, nullable=False)
    challenge_category = Column(String, nullable=True)
    challenge_difficulty = Column(String, nullable=True)
    was_sent = Column(Boolean, default=False)
    __table_args__ = (
        UniqueConstraint("event_id", "challenge_id", name="_event_challenge_uc"),
    )
