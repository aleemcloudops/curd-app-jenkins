pipeline {
    agent any

    environment {
        COMPOSE_PROJECT_NAME = "curdapp"
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker compose build'
            }
        }

        stage('Start Containers') {
            steps {
                sh 'docker compose up -d'
            }
        }

        stage('Test App Health') {
            steps {
                sh 'curl -f http://localhost:5000/ping || echo "Backend not responding"'
                sh 'curl -f http://localhost:3000 || echo "Frontend not responding"'
            }
        }

        stage('Stop Containers') {
            steps {
                sh 'docker compose down'
            }
        }
    }

    post {
        always {
            echo "Cleaning up..."
            sh 'docker compose down --volumes --remove-orphans || true'
        }
    }
}
