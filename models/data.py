from boot import db, ma


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    field = db.Column(db.String(100))

class DataSchema(ma.ModelSchema):
    class Meta:
        model = Data


data_schema_many = DataSchema(many=True)
data_schema = DataSchema()
