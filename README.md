# W4153-Job-Service

Simple microservice application for the Job service.

## Endpoints
### GET `/`
- Returns a welcome message to indicate the service is running.
- Example Response:
```json
{
  "message": "Hello BuggySoft!"
}
```

### GET `/job_info/{job_id}`
- Returns the job information for the given job id.
- Example Response:
```json
{
  "job_id": 1,
  "job_name": "Software Development Engineer I",
  "job_company": "Amazon",
  "job_created_at": "2024-09-04T00:00:00",
  "job_url": "https://www.amazon.jobs/en/jobs/2748536/software-development-engineer-i"
}
```

### GET `/jobs_of_company/{company_name}`
- Returns the list of job information for the given company name.
- Example Response:
```json
[
  {
    "job_id": 1,
    "job_name": "Software Development Engineer I",
    "job_company": "Amazon",
    "job_created_at": "2024-09-04T00:00:00",
    "job_url": "https://www.amazon.jobs/en/jobs/2748536/software-development-engineer-i"
  },
  {
    "job_id": 3,
    "job_name": "Data Engineer Summer Internship",
    "job_company": "Amazon",
    "job_created_at": "2024-09-01T00:00:00",
    "job_url": "https://amazon.jobs/en/jobs/2740350/data-engineer-summer-internship-2025-us"
  }
]
```

## Deployment Instructions

Make sure you have Python 3 and `pip` installed on your machine and clone the repository.
```bash
cd ./job-service/
```
Create a virtual environment and install the dependencies.
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Run the application from the root directory.
```bash
python3 -m app.main
```
The application will be running on `http://localhost:8003/`.

If you want to let the application run in the background, you can use a simple `nohup` command,
or other terminal multiplexers like `tmux` or `screen` as you wish.
Here is an example of using `nohup` and redirecting the output to a log file.
```bash
nohup python3 -m app.main >~/log/job-service.20240929.log 2>&1 &
```