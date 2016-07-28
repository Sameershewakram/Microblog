from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname' : 'Miguel'}

	posts=[
		{
			'author' : {'nickname':'john'},
			'body': 'Beautiful day in portland'
		},
		{
			'author': {'nickname':'susan'},
			'body': 'The Avengers movie was so cool'
		}
	]
	return render_template('index.html' , title='sameer' , user=user , posts=posts)
