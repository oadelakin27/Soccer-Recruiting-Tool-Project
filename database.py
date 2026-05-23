from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class School(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    conference = db.Column(db.String(100))
    state = db.Column(db.String(50))
    head_coach = db.Column(db.String(100))
    recruiting_contact = db.Column(db.String(100))
    recruiting_email = db.Column(db.String(100))
    camp_dates = db.Column(db.String(200))
    program_notes = db.Column(db.String(500))

class OutreachTracker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'), nullable=False)
    status = db.Column(db.String(50), default='Not Contacted')
    notes = db.Column(db.String(500))
    date_contacted = db.Column(db.String(50))
    school = db.relationship('School', backref='outreach')