import json
import random

from boot import db
from models.data import Data
from seeds.Seeder import Seeder

class DataSeeder(Seeder):

    def run(self):
        for _ in range(100):
            d = Data()
            d.field = 'Data %s' % random.randint(0,100)
            db.session.add(d)
            db.session.commit()