from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from settings import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# These imports must stay after app and db initialization to avoid
# circular imports: the modules below import app and/or db from this package.
from opinions_app import cli_commands, error_handlers, views  # noqa: E402, F401
