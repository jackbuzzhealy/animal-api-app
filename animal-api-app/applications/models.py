from applications import db

class Animals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal = db.Column(db.String(30))
    noise = db.Column(db.String(30))

    def __repr__(self):
        return ''.join(['Animals:',self.animal,'Noise:',self.noise])


