from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <body style="font-family:Arial;text-align:center">
        <h1>Student Information System</h1>
        <p>Student Name: Arun Kumar</p>
        <p>Roll Number: 101</p>
        <p>Department: Computer Science</p>
        <h3>Application Running Successfully!</h3>
    </body>
    </html>
