from flask_migrate import Migrate,MigrateCommand
from flask_script import Shell,Manager
from app import app,db
from models import *
manager = Manager(app=app)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)
if __name__ == '__main__':
    manager.run()