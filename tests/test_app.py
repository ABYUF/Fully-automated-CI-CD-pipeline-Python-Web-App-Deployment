from app import app

def test_index():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200

    # Headline
    assert b"CI/CD Cloud DevOps Project is Deployment Successful!" in response.data

    # Body
    assert b"This Flask application demonstrates a <b>Fully Automated CI/CD Pipeline</b>." in response.data
    assert b"<b>Code pushed to GitHub \xe2\x86\x92 Linted \xe2\x86\x92 Unit Tested \xe2\x86\x92 Built \xe2\x86\x92 Deployed to EC2</b>" in response.data
    assert b"Integrated with Gunicorn & Nginx for production" in response.data
    assert b"Managed using GitHub Actions workflow" in response.data

    # Footer
    assert b"(Project by Abrar Basha \xe2\x80\x94 Cloud & DevOps Engineer)" in response.data
