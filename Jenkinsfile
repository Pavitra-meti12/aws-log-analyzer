pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test Environment') {
            steps {
                bat 'docker --version'
            }
        }

        stage('Build') {
            steps {
                echo 'Building project...'
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker build -t aws-log-analyzer .'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploy step completed'
            }
        }
    }
}
