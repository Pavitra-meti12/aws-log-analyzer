pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/Pavitra-meti12/aws-log-analyzer.git'
            }
        }

        stage('Run Log Analyzer') {
            steps {
                bat 'python lambda_function.py'
            }
        }
    }
}