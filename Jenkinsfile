pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Obteniendo codigo'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t diabetes-model .'
            }
        }

        stage('Train Model') {
            steps {
                sh '''
                docker rm -f diabetes-container || true
                docker run --name diabetes-container diabetes-model
                '''
            }
        }
    }
}