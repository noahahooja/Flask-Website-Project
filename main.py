from flask import Flask, request, url_for, redirect, render_template
#create a flask instance

app = Flask(__name__)


class Projects:
  def __init__(self, projectname, repl, projectplan):
    self.projectname = projectname
    self.repl = repl
    self.projectplan = projectplan

#past 6 weeks project
GamesProject = Projects("Games Project", "https://repl.it/@NolanDEsopo/Games#README.MD", "https://docs.google.com/document/d/1WtuvQZD_jODhgrxv6mhmUYqV28o_DA9hs4gDBUIGt_A/edit?usp=sharing")
#next 6 weeks project
PortfolioProject = Projects("Portfolio Project", "https://repl.it/@NoahAhooja/Flask-Website-Project#main.py", "/portfolio")

#connects default URL of server to a python function
@app.route('/')
def home():
  return render_template("home.html", links = [GamesProject, PortfolioProject], Title = "Home")

@app.route('/calculator')
def calculator():
  return render_template('calculator.html')

calculator = Projects("Calculator", "/calculator", "")

@app.route('/portfolio')
def portfolio():
  return render_template('portfolio.html', portfolioprojects = [calculator], Title = "Portfolio")

if __name__ == "__main__":
  app.run(debug=True, port='3000', host='0.0.0.0')