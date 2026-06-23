Soccer Recruiting Tool


A web app for tracking college soccer recruiting outreach (coach contacts, camp dates, and communication status).
I built it because I needed it for my own recruiting process and existing tools didn't fit.


Live app: https://soccer-recruiting-tool-project.onrender.com/


Why I built this:
During my own recruiting process I was tracking coach emails, camp invites, and response status across a dozen+ schools in scattered notes and tabs.
Information was changing constantly. Coaching staff turn over (e.g. a coach I'd been in contact with left for another program mid-cycle), camp dates move, and athletics department contact pages go stale.
I built this to have one place to track outreach status per school, with editable coach/contact info so the data stays current instead of relying on a static spreadsheet.


Features:

Browse D1 programs with search and filters by conference and state

Per-school detail pages with editable head coach, recruiting contact, email, and camp dates

Outreach tracker per school: status (Not Contacted, Emailed, Responded, Camp Registered, Camp Attended, Not Interested), notes, and date contacted

"My Recruits" dashboard showing only schools with active outreach

User accounts: each user has their own independent outreach tracker; school/coach data is shared and editable by all users


Tech stack:

Backend - Python, Flask, Flask-SQLAlchemy, Flask-Login

Database - PostgreSQL in production (Render), SQLite for local development

Frontend - Server-rendered HTML/CSS (Jinja2 templates), no JS framework

Deployment -  Render, via render.yaml blueprint (web service + managed Postgres)


Setting it up (Macbook):

In Terminal, write and run these lines one-by-one.

git clone https://github.com/oadelakin27/Soccer-Recruiting-Tool-Project.git

cd Soccer-Recruiting-Tool-Project

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python seed_data.py

python app.py       # runs at http://127.0.0.1:5000
