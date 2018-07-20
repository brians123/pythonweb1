from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, world\n\n'
@app.route('/brian')
def hello_brian():
	return """
	<b>Hello brian</b>
	<a href="table">back to table</a>
	"""

@app.route('/table')
def create_table():
	return """
	<table>
	<tr>
		<th>Firstname</th>
		<th>Lastname</th>
		<th>Age</th>
	</tr>
	<tr>
		<td>Jill</td>
		<td>Stein</td>
		<td>506</td>
	</tr>
	</table>
	<a href="brian">hello</a>
	"""


if __name__ == "__main__":
	app.run(host="ec2-18-217-6-113.us-east-2.compute.amazonaws.com", port=80)
