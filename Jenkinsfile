pipeline {
agent any

```
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
            bat 'docker build -t aws-log-analyzer .'
        }
    }

    stage('Deploy') {
        steps {
            echo 'Deploying Project...'
        }
    }
}
```

}
