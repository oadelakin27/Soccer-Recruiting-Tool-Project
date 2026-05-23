from app import app
from database import db, School

schools_data = [
    # Ivy League
    {"name": "Cornell University", "conference": "Ivy League", "state": "New York", "head_coach": "John Smith", "recruiting_email": "tk683@cornell.edu", "camp_dates": "July 2-3, July 11-12, August 1-2"},
    {"name": "Dartmouth College", "conference": "Ivy League", "state": "New Hampshire", "head_coach": "Connor Klekota", "recruiting_email": "Connor.A.Klekota@dartmouth.edu", "camp_dates": "July 6-8, July 8-10"},
    {"name": "Yale University", "conference": "Ivy League", "state": "Connecticut", "head_coach": "Kylie Stannard", "recruiting_email": "kylie.stannard@yale.edu", "camp_dates": "TBD"},
    {"name": "Columbia University", "conference": "Ivy League", "state": "New York", "head_coach": "Michael Casper", "recruiting_email": "columbiamsoccer@gmail.com", "camp_dates": "TBD"},
    {"name": "University of Pennsylvania", "conference": "Ivy League", "state": "Pennsylvania", "head_coach": "Brian Gill", "recruiting_email": "brgill@upenn.edu", "camp_dates": "TBD"},
    {"name": "Harvard University", "conference": "Ivy League", "state": "Massachusetts", "head_coach": "Josh Shapiro", "recruiting_email": "msoccer@fas.harvard.edu", "camp_dates": "TBD"},
    {"name": "Brown University", "conference": "Ivy League", "state": "Rhode Island", "head_coach": "Chase Wileman", "recruiting_email": "msoccer@brown.edu", "camp_dates": "TBD"},
    {"name": "Princeton University", "conference": "Ivy League", "state": "New Jersey", "head_coach": "Jim Barlow", "recruiting_email": "jimbarlo@princeton.edu", "camp_dates": "TBD"},

    # ACC
    {"name": "Duke University", "conference": "ACC", "state": "North Carolina", "head_coach": "John Kerr", "recruiting_email": "jjk21@duke.edu", "camp_dates": "TBD"},
    {"name": "University of Virginia", "conference": "ACC", "state": "Virginia", "head_coach": "George Gelnovatch", "recruiting_email": "Vrp9as@virginia.edu", "camp_dates": "TBD"},
    {"name": "Wake Forest University", "conference": "ACC", "state": "North Carolina", "head_coach": "Bobby Muuss", "recruiting_email": "muussrp@wfu.edu", "camp_dates": "TBD"},
    {"name": "University of North Carolina", "conference": "ACC", "state": "North Carolina", "head_coach": "Carlos Somoana", "recruiting_email": "csomoano@uncaa.unc.edu", "camp_dates": "TBD"},
    {"name": "Clemson University", "conference": "ACC", "state": "South Carolina", "head_coach": "Mike Noonan", "recruiting_email": "msoccer@clemson.edu", "camp_dates": "TBD"},
    {"name": "Syracuse University", "conference": "ACC", "state": "New York", "head_coach": "Ian McIntyre", "recruiting_email": "ismcinty@syr.edu", "camp_dates": "TBD"},
    {"name": "Notre Dame", "conference": "ACC", "state": "Indiana", "head_coach": "Chad Riley", "recruiting_email": "criley@nd.edu", "camp_dates": "TBD"},

    # Big East
    {"name": "Georgetown University", "conference": "Big East", "state": "Washington DC", "head_coach": "Brian Wiese", "recruiting_email": "gumenssoccer@georgetown.edu", "camp_dates": "TBD"},
    {"name": "Creighton University", "conference": "Big East", "state": "Nebraska", "head_coach": "Johnny Torres", "recruiting_email": "creightonsocceracademy@creighton.edu", "camp_dates": "TBD"},
    {"name": "St. John's University", "conference": "Big East", "state": "New York", "head_coach": "Dr. David Masur", "recruiting_email": "masurd@stjohns.edu", "camp_dates": "TBD"},
    {"name": "University of Connecticut", "conference": "Big East", "state": "Connecticut", "head_coach": "Chris Gbandi", "recruiting_email": "menssoccer@uconn.edu", "camp_dates": "TBD"},

    # Big Ten
    {"name": "Northwestern University", "conference": "Big Ten", "state": "Illinois", "head_coach": "Russell Payne", "recruiting_email": "msoccer@northwestern.edu", "camp_dates": "TBD"},
    {"name": "University of Michigan", "conference": "Big Ten", "state": "Michigan", "head_coach": "Chaka Daley", "recruiting_email": "email.mscoccer@umich.edu", "camp_dates": "TBD"},
    {"name": "Penn State University", "conference": "Big Ten", "state": "Pennsylvania", "head_coach": "Rob Dow", "recruiting_email": "msoc@athletics.psu.edu", "camp_dates": "TBD"},
    {"name": "University of Maryland", "conference": "Big Ten", "state": "Maryland", "head_coach": "Sasho Cirovski", "recruiting_email": "sasho@umd.edu", "camp_dates": "TBD"},

    # Others
    {"name": "Rice University", "conference": "AAC", "state": "Texas", "head_coach": "TBD", "recruiting_email": "TBD", "camp_dates": "TBD"},
    {"name": "SMU", "conference": "AAC", "state": "Texas", "head_coach": "TBD", "recruiting_email": "TBD", "camp_dates": "TBD"},
    {"name": "Carnegie Mellon University", "conference": "UAA", "state": "Pennsylvania", "head_coach": "TBD", "recruiting_email": "TBD", "camp_dates": "TBD"},
    {"name": "Johns Hopkins University", "conference": "Centennial", "state": "Maryland", "head_coach": "TBD", "recruiting_email": "TBD", "camp_dates": "TBD"},
    {"name": "Tufts University", "conference": "NESCAC", "state": "Massachusetts", "head_coach": "TBD", "recruiting_email": "TBD", "camp_dates": "TBD"},
]

with app.app_context():
    db.create_all()
    
    # Clear existing data
    School.query.delete()
    db.session.commit()
    
    for school_data in schools_data:
        school = School(**school_data)
        db.session.add(school)
    
    db.session.commit()
    print(f"Successfully added {len(schools_data)} schools to the database.")