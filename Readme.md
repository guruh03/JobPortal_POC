Django Job Portal API Test

## Tasks
- Create job post
- Apply to a job
- Get job summary with applicant count
- Apply limit: max 3/day per email

## Setup
```bash
git clone https://github.com/guruh03/JobPortal_POC.git
cd job_portal
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py makemigrations 
python manage.py migrate
python manage.py runserver 0.0.0.0:8000 # default port 8000