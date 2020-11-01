"""Initialize Flask app."""
from flask import Flask
from .plotlydash import dashboard1, dashboard2, dashboard3
import pandas as pd
import config
from sqlalchemy import create_engine


def get_data():
    # A long string that contains the necessary Postgres login information
    postgres_str = ('postgresql://{username}:{password}@{ipaddress}:{port}/{dbname}'
                    .format(username=config.POSTGRES_USERNAME,
                            password=config.POSTGRES_PASSWORD,
                            ipaddress=config.POSTGRES_ADDRESS,
                            port=config.POSTGRES_PORT,
                            dbname=config.POSTGRES_DBNAME))
    # Create the connection
    cnx = create_engine(postgres_str)

    query1 = pd.read_sql_query('''SELECT name, popularity FROM songs ORDER BY popularity DESC LIMIT 10;''', cnx)
    query2 = pd.read_sql_query('''SELECT genre, COUNT(name) FROM songs GROUP BY genre ORDER BY COUNT(name) DESC LIMIT 10;''', cnx)
    query3 = pd.read_sql_query('''SELECT s.name, SUM(r.playbacks) 
                                FROM songs s, songs_heard r 
                                WHERE s.id = r.song_id 
                                GROUP BY name 
                                ORDER BY SUM(r.playbacks) DESC;''', cnx)

    """Construct core Flask application with embedded Dash app."""

    return query1, query2, query3

def init_app():
    q1, q2, q3 =get_data()
    server = Flask(__name__)
    dashboard1.init_dashboard1(server, q1)
    dashboard2.init_dashboard2(server, q2)
    dashboard3.init_dashboard3(server, q3)
    return server