pipeline {
    agent any

    stages {
        stage('Pull Docker Image') {
            steps {
                script {
                    // Pull the Docker image from Docker Hub
                    sh 'docker --version'
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
        stage('Clone Repository') {
            steps {
                echo 'Cloning repository...'
                script {
                    def branchName = sh(script: 'echo ${GIT_BRANCH} | cut -d"/" -f2', returnStdout: true).trim()
                    echo "Branch name is: ${branchName}"
                    git branch: "${branchName}", url: 'https://github.com/erYash15/MLOps-Automation-AWS.git'
                }
            }
        }
        stage('Setup Environment') {
            steps {
                echo 'Setting up Python environment...'
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip setuptools wheel
                pip install -r requirements.txt
                '''
            }
        }
        stage('Lint Code') {
            steps {
                echo 'Linting code...'
                sh '''
                . venv/bin/activate
                git config --unset-all core.hooksPath
                chmod +x ./pre-commit.sh
                ./pre-commit.sh
                pre-commit install
                pre-commit run -a
                '''
            }
        }
        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh '''
                . venv/bin/activate
                python3 -m unittest discover -s tests -p "*.py"
                '''
            }
        }
        stage('Cleanup') {
            steps {
                echo 'Cleaning up environment...'
                sh '''
                rm -rf venv
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
