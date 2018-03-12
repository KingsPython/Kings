from ext import model



class Student(model.Model):
    id = model.Column(model.Integer,primary_key=True)
    name = model.Column(model.String(16))



