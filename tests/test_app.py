from app import app

def test_index():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    # Headline
    assert b"CI/CD Deployment Successful!" in response.data

    # Body
    assert b"Your <b>Python Flask Application</b> is up and running on <b>AWS EC2</b>." in response.data
    assert b'Deployed using <b>GitHub Actions</b> with <b>Automated Build, Linting, Testing, and Deployment</b>.' in response.data
    assert b"Technology Stack: Flask | Gunicorn | Nginx | GitHub Actions" in response.data

    # Footer
    assert b'style="font-size:12px; color:gray;"> Pipeline verified and is working end-to-end.' in response.data
