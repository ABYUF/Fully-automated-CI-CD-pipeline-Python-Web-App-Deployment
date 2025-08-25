from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h2>CI/CD Deployment Successful!</h2>
    <p>Your <b>Python Flask Application</b> is up and running on <b>AWS EC2</b>.</p>
    <p>Deployed using <b>GitHub Actions</b> with <b>Automated Build, Linting, Testing, and Deployment</b>.</p>
    <p>Technology Stack: Flask | Gunicorn | Nginx | GitHub Actions</p>
    <hr>
    <p style="font-size:12px; color:gray;"> Pipeline verified and is working end-to-end.</p>
    """

if __name__ == '__main__':
    app.run()
