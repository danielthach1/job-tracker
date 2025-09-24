from flask import Flask, render_template, request, redirect, url_for
from job_tracker.api import search, details

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query = request.form['query']
        country = request.form['country']
        date_posted = request.form['date_posted']
        employment_types = request.form['employment_types']  
        return redirect(url_for(
            'results',
            query=query,
            country=country,
            date_posted=date_posted,
            employment_types=employment_types,
            page=1
        ))
    random_jobs = search(query="developer", country="us", date_posted="all", employment_types="FULLTIME", page=1, num_pages=1)
    return render_template('index.html', random_jobs=random_jobs)

@app.route('/results')
def results():
    query = request.args.get('query', '')
    country = request.args.get('country', 'us')
    date_posted = request.args.get('date_posted', 'all')
    employment_types = request.args.get('employment_types', 'FULLTIME')
    page = int(request.args.get('page', 1))
    jobs = search(query, country, date_posted, employment_types, page=page, num_pages=1)
    return render_template(
        'results.html',
        jobs=jobs,
        query=query,
        country=country,
        date_posted=date_posted,
        employment_types=employment_types,
        page=page
    )

@app.route('/details/<job_id>', methods=['GET'], endpoint='details_page')
def show_job_details(job_id):
    country = request.args.get('country', 'us')
    detail_list = details(job_id, country)
    job = detail_list[0] if detail_list else None
    return render_template('details.html', job=job)

@app.route("/tracker")
def view_tracker():
    return render_template("tracker.html")

if __name__ == '__main__':
    app.run(debug=True)
