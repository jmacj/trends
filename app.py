from flask import Flask
from core import (
		api,
		models,
		home
	)

app = Flask(__name__)
app.config.from_object("core.config")

@app.before_request
def before_request():
	models.initialize_db()

@app.teardown_request
def teardown_request(exception):
	models.close_db()

''' Register modules '''
app.register_blueprint(home.app, url_prefix="")
app.register_blueprint(api.app, url_prefix="/api")


if __name__ == "__main__":
	# app = create_app()
	app.run(debug=True)