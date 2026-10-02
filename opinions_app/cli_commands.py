import csv

import click

from opinions_app import app, db
from opinions_app.models import Opinion


@app.cli.command('load_opinions')
def load_opinions_command():
    """Загрузить мнения из CSV-файла в базу данных."""
    with open('opinions.csv', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        counter = 0
        for row in reader:
            opinion = Opinion(**row)
            db.session.add(opinion)
            db.session.commit()
            counter += 1
    click.echo(f'Загружено мнений: {counter}')
