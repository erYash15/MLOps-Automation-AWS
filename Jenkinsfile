pipeline {
    agent any
    stages {
        stage('Setup Python') {
            steps {
                sh 'python3 --version'
            }
        }
        stage('Setup Python 2') {
            steps {
                sh 'which python3'
            }
        }
    }
}