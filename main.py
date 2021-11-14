from flask import Flask, request, render_template, send_file
from scrapper_wework import get_jobs as get_ww_jobs
from scrapper_stackoverflow import get_jobs as get_so_jobs
from scrapper_remoteok import get_jobs as get_ro_jobs
from save import save_to_file as save

db = {}

app = Flask("Job Scrapper")

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/result")
def result():
  search = request.args.get("search")
  if search:
    search = search.lower()
    if search in db:
      jobs = db[search]
    else:
      jobs = get_ww_jobs(search) + get_so_jobs(search) + get_ro_jobs(search)
      if not jobs:
        return render_template("error.html", er_code=1)
    return render_template("result.html", jobs = jobs, cnt = len(jobs), search = search)
  return render_template("error.html", er_code=2)

@app.route("/export")
def export():
  search = request.args.get("search")
  if search:
    search = search.lower()
    jobs = db.get(search)
    if jobs:
      save(jobs)
      return send_file("jobs.csv")
  return render_template("error.html", er_code=2)

app.run(host="0.0.0.0")