from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#############################################################################


class User(db.Model):
    """User of website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    username = db.Column(db.String(64),
                         unique=True,
                         nullable=False)
    email = db.Column(db.String(64),
                      unique=True,
                      nullable=False)
    password = db.Column(db.String(200),
                         nullable=False)

    def __repr__(self):

        return "<User user_id=%s username=%s>" % (self.user_id, self.username)


