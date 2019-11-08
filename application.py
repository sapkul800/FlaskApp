from flask import Flask
app = Flask(__name__)

def sample():
	a = 10
	b = 20
	c = a + b
	d = 0
	if c > 10:
		if c > 100:
			if c != 100:
				print ("ok")
	d = 0
	if c > 10:
		if c > 100:
			if c != 100:
				print ("ok")
@app.route("/")
def hello():
    return "Hello World! This is First new sample Flask application"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=9999)