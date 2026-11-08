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
            }
        }

        stage('Mostrar Python') {
            steps {
                sh 'python --version || python3 --version'
            }
        }
    }
}