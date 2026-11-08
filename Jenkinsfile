pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Codigo descargado'
            }
        }

        stage('Ver archivos') {
            steps {
                sh 'ls -la'
                sh 'find .'
            }
        }
    }
}