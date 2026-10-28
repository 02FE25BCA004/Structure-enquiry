
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Python Unit Tests') {
            steps {
                bat 'python -m unittest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t structure-enquiry .'
            }
        }

        stage('Docker Application Test') {
            steps {
                bat '''
                (echo Sahil& echo BCA& echo 1& echo 90& echo 85& echo 80) | docker run --rm -i --entrypoint python structure-enquiry -u app.py | findstr /C:"Assigned Grade: Grade A"
                '''
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: Tests passed and Docker application ran successfully.'
        }
        failure {
            echo 'FAILED: Check the Jenkins Console Output for the error.'
        }
    }
}
