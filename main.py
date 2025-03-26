from flask import Flask
from data import db_session
from data.users import User, Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init('db/table.sqlite')

    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.position = "captain"
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'
    user.age = 21
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = "Steve"
    user.name = "Rick"
    user.position = "private"
    user.speciality = 'engineer'
    user.address = 'module_2'
    user.age = 31
    user.email = 'aolsdfj@mars.org'
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = "Samanta"
    user.name = "Uiliar"
    user.position = "sergeant"
    user.age = 20
    user.speciality = 'engineer'
    user.address = 'module_3'
    user.email = 'slfkgdjlskdjf@mars.org'
    db_sess.add(user)
    db_sess.commit()


    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    db_sess.add(job)
    db_sess.commit()
    app.run()


if __name__ == '__main__':
    main()