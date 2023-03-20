from flask import Flask
from model_marsians.data import db_session
from data.users import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/jobs.db")

    j = Jobs()
    j.team_leader = 1
    j.job = "deployment of residential modules 1 and 2"
    j.work_size = 15
    j.collaborators = "2, 3"
    j.start_date = "now"
    j.is_finished = False

    db_sess = db_session.create_session()
    db_sess.add(j)
    db_sess.commit()


if __name__ == '__main__':
    main()