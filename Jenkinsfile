pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Codigo descargado desde GitHub'
            }
        }

        stage('Verificar Estructura') {
            steps {
                sh 'ls -la'
                sh 'find .'
            }
        }

        stage('Verificar Modelo') {
            steps {
                sh 'test -f artifacts/model.pkl'
                echo 'Modelo encontrado'
            }
        }
    }
}