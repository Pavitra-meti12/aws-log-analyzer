pipeline {
    agent any

    stages {

        stage('Run Log Analyzer') {
            steps {
                bat 'python lambda_function.py'
            }
        }
    }
}
