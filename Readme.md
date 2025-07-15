Django Job Portal API Test

## Tasks
- Create job post
- Apply to a job
- Get job summary with applicant count
- Apply limit: max 3/day per email

## Setup
```bash
git clone <repo-url> # not included due to shared drive link
cd job_portal
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py makemigrations 
python manage.py migrate
python manage.py runserver # default port 8000