from flask import Flask, render_template, request
from database import db, School, OutreachTracker

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///soccer_recruit.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route("/")
def home():
    query = request.args.get('search', '')
    conference = request.args.get('conference', '')
    state = request.args.get('state', '')

    schools = School.query

    if query:
        schools = schools.filter(School.name.ilike(f'%{query}%'))
    if conference:
        schools = schools.filter(School.conference == conference)
    if state:
        schools = schools.filter(School.state == state)

    schools = schools.all()

    conferences = db.session.query(School.conference).distinct().all()
    conferences = [c[0] for c in conferences if c[0]]

    states = db.session.query(School.state).distinct().all()
    states = [s[0] for s in states if s[0]]

    return render_template("index.html", 
                         schools=schools,
                         conferences=conferences,
                         states=states,
                         search=query,
                         selected_conference=conference,
                         selected_state=state)

@app.route("/school/<int:school_id>")
def school_detail(school_id):
    school = School.query.get_or_404(school_id)
    tracker = OutreachTracker.query.filter_by(school_id=school_id).first()
    return render_template("school.html", school=school, tracker=tracker)

@app.route("/update_status/<int:school_id>", methods=["POST"])
def update_status(school_id):
    tracker = OutreachTracker.query.filter_by(school_id=school_id).first()
    if not tracker:
        tracker = OutreachTracker(school_id=school_id)
        db.session.add(tracker)
    tracker.status = request.form.get('status')
    tracker.notes = request.form.get('notes')
    tracker.date_contacted = request.form.get('date_contacted')
    db.session.commit()
    return home()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)