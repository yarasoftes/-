from flask import Flask
from config import Config
from models import db
import handlers

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Регистрация маршрутов
app.add_url_rule('/', 'index', handlers.index)
app.add_url_rule('/add_user', 'add_user', handlers.add_user, methods=['GET', 'POST'])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Создаёт таблицы, если их нет
    app.run(debug=True)