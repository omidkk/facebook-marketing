"""Initialize Flask app."""
import logging

from flask import Flask

from config import Config
from rest.api import api_v1

_log = logging.getLogger(__name__)


def create_app():
    """Construct the core application."""
    _log.info("start create the app.")

    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)
    # app.config['SECRET_KEY'] = Config.SECRET_KEY
    # app.config['JWT_SECRET_KEY'] = Config.SECRET_KEY

    # db.init_app(app)
    # jwt.init_app(app)

    app.register_blueprint(api_v1)

    # @click.command('init-db')
    # @with_appcontext
    # def init_db_command():
    #     click.echo('start initial the database!')
    #     init_db(db)
    #     click.echo('database Initialized complete.')
    #
    # @click.command('load-data')
    # @with_appcontext
    # def init_data_command():
    #     click.echo('start loading the data!')
    #     load_data(db)
    #     click.echo('data loaded complete.')
    #
    # app.cli.add_command(init_db_command)
    # app.cli.add_command(init_data_command)
    return app
