from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h2>CI/CD Cloud DevOps Project is Deployment Successful!</h2>
    <p>This Flask application demonstrates a <b>Fully Automated CI/CD Pipeline</b>.</p>
    <p><b>Code pushed to GitHub → Linted → Unit Tested → Built → Deployed to EC2</b></p>
    <p>Integrated with Gunicorn & Nginx for production</p>
    <p>Managed using GitHub Actions workflow</p>
    <footer style="font-size:12px; color:gray;">
        (Project by Abrar Basha — Cloud & DevOps Engineer)
    </footer>
    """

if __name__ == '__main__':
    app.run()
