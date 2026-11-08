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
                bat 'docker build -t diabetes-model .'
            }
        }

        stage('Train Model') {
            steps {
                bat '''
                docker rm -f diabetes-container || exit 0
                docker run --name diabetes-container diabetes-model
                '''
            }
        }
    }
}