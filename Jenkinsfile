pipeline {
    agent any
    environment {
        VENV_DIR = 'venv' // Directory for the virtual environment
    }
    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning repository...'
                echo "Branch name: ${env.BRANCH_NAME}"
                git branch: "main", url: 'https://github.com/erYash15/MLOps-Automation-AWS.git'
            }
        }
        stage('Setup Environment') {
            steps {
                echo 'Setting up Python environment...'
                sh '''
                apt install python3.12-venv
                python3 -m venv ${VENV_DIR}
                source ${VENV_DIR}/bin/activate
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

                python3 -m unittest discover -s tests -p "*.py" > result.xml
                '''
                // Archiving test results
                junit 'results.xml'
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
