from data import db_session
from flask import render_template
from data.jobs import Jobs

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    app.run()

@app.route("/")
def index():
    db_session.global_init("db/jobs.db")
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template("prof.html", jobs=jobs)


if __name__ == '__main__':
    main()
