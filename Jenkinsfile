pipeline {
    agent any
    
    stages {
        stage('Pull Docker Image') {
            steps {
                script {
                    // Pull the Docker image from Docker Hub
                    sh 'docker pull python:3.9-slim'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Run a command inside the Docker container
                    sh 'docker run --rm python:3.9-slim python --version'
                }
            }
        }
    }
    environment {
        VENV_DIR = 'venv' // Directory for the virtual environment
    }
    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning repository...'
                git branch: "main", url: 'https://github.com/erYash15/MLOps-Automation-AWS.git'
            }
        }
        stage('Setup Environment') {
            steps {
                echo 'Setting up Python environment...'
                sh '''
                python3 -m venv ${VENV_DIR}
                . ${VENV_DIR}/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }
        stage('Lint Code') {
            steps {
                echo 'Linting code...'
                echo 'TODO'
            }
        }
        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh '''
                source ${VENV_DIR}/bin/activate
                python3 -m unittest discover -s tests -p "*.py"
                '''
            }
        }
        stage('Cleanup') {
            steps {
                echo 'Cleaning up environment...'
                sh '''
                deactivate
                rm -rf ${VENV_DIR}
                '''
            }
        }
    }
    post {
        always {
            echo 'Pipeline completed.'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
