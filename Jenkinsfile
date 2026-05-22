pipeline {
    agent any

    stages {

        stage('Run Log Analyzer') {
            steps {
                bat '"C:\\Users\\pavit\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" lambda_function.py'
            }
        }
    }
}
