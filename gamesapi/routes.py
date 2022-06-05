"""Application routes."""
from datetime import datetime as dt

from flask import current_app as app
from flask import make_response, redirect, render_template, request, url_for, Response

from .models import User, db


@app.route("/", methods=["GET"])
def user_records():
    """Create a user via query string parameters."""
    results = []
    # username = request.args.get("user")
    # email = request.args.get("email")
    # results = []
    # if username and email:
    #     # existing_user = User.query.filter(
    #     #     User.username == username or User.email == email
    #     # ).first()
    #     # if existing_user:
    #     #     return make_response(f"{username} ({email}) already created!")
    #     new_user = User(
    #         username=username,
    #         email=email,
    #         created=dt.now(),
    #         bio="In West Philadelphia born and raised, \
    #         on the playground is where I spent most of my days",
    #         admin=False,
    #     )  # Create an instance of the User class
    #     db.session.add(new_user)  # Adds new User record to database
    #     db.session.commit()  # Commits all changes
    #     # redirect(url_for("user_records"))
    #     users = User.query.all()
    #     print(users)
    #     results.append(users)
    # new_user = User(
    #   username = 'dummy1',
    # email = 'letsgoceltics@protonmail.org',
    # created = dt.now(),
    # bio = '!Korn',
    # admin = False
    # )
    # db.session.add(new_user)
    # db.session.commit()
    query = User.query.all()
    for idx in query:
      results_dict = {
        'username' : idx.username,
        'email': idx.email,
        'date_created': idx.created,
        'bio': idx.bio,
        'admin': idx.admin
      }
      results.append(results_dict)
    print(results)
    return Response("users_endpoint: {results}".format(results=results), 200)