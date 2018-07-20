from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, world\n\n'
@app.route('/brian')
def hello_brian():
	return 'Hello.... brian...\n\n\n\n\n\n'

if __name__ == "__main__":
	app.run(host="ec2-18-217-6-113.us-east-2.compute.amazonaws.com", port=80)
