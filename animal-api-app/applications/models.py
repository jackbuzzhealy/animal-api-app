from application import db

class Animals(db.model):
    id = db.column(db.Integer, primary_key=True)
    animal = db.column(db.String(30))
    noise = db.column(db.String(30))

    def __repr__(self):
        return ''.join(['Animals:',self.animal,'Noise:',self.noise])


