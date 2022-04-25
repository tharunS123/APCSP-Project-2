"""
  Some unique resource that I used in this program was learned from: 
    https://flask-login.readthedocs.io/en/latest/
    https://pypi.org/project/Flask-Login/
    https://pypi.org/project/Flask-SQLAlchemy/
"""

from website import create_app # importing the create_app fucntions from __init__.py

app = create_app()

# Making the debugger mode to True if the web server is running. 
if __name__ == '__main__':
  app.run(debug=True)