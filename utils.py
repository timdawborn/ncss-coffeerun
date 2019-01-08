from application import app, db
from application.models import User


def get_or_create_user(user_id, team_id, name):
    print(team_id)
    q = User.query.filter_by(slack_user_id=user_id, slack_team_id=team_id)
    users = q.all()
    if len(users) == 1:
        return users[0]
    if len(users) == 0:
        user = User(name)
        user.slack_user_id = user_id
        user.slack_team_id = team_id
        user.tutor = team_id == app.config['SLACK_TEAM_ID']
        user.teacher = not user.tutor
        db.session.add(user)
        db.session.commit()
        return user

    assert False, 'More than one user with the same slack ID - Something is very wrong'
