from app import db,app
from flask_migrate import Migrate,MigrateCommand
from flask_script import  Manager
from models import *
manager = Manager(app)
miggrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)



if __name__ == '__main__':
    manager.run()