# -*- coding: utf-8 -*-
from sqlalchemy.orm import sessionmaker
from sport_bot.models import TeamsPropability, db_connect, create_teamspropability_table


class SportBotPipeline(object):
    """SportBot pipeline for storing scraped items in the database"""

    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates TeamsPropability table.
        """
        engine = db_connect()
        create_teamspropability_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save TeamsPropability in the database.

        This method is called for every item pipeline component.

        """
        session = self.Session()
        teams_propability = TeamsPropability(**item)

        try:
            session.add(teams_propability)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item