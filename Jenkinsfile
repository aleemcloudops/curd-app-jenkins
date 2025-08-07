pipeline {
    agent any

    environment {
        DOCKER_COMPOSE = 'docker compose'
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Images') {
            steps {
                sh "${DOCKER_COMPOSE} build"
            }
        }

        stage('Clean Old Containers') {
            steps {
                sh '''
                    docker rm -f backend || true
                    docker rm -f frontend || true
                '''
            }
        }

        stage('Start Containers') {
            steps {
                sh "${DOCKER_COMPOSE} up -d"
            }
        }

        stage('Test App Health') {
            steps {
                sh 'curl -f http://localhost:5000/notes || exit 1'
            }
        }

        stage('Stop Containers') {
            steps {
                sh "${DOCKER_COMPOSE} down --volumes --remove-orphans"
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh "${DOCKER_COMPOSE} down --volumes --remove-orphans || true"
        }
    }
}
