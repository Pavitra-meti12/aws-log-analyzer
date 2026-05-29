pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/Pavitra-meti12/aws-log-analyzer.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building AWS Log Analyzer Project...'
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Docker build step (run only if Docker installed)'
                bat 'docker build -t aws-log-analyzer .' 
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploy stage executed'
            }
        }
    }
}