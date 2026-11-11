pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r source/requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest tests/
                '''
            }
        }

        stage('Train Model') {
            steps {
                sh '''
                . venv/bin/activate
                python source/train.py
                '''
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t diabetes-model .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run --rm diabetes-model'
            }
        }
    }

    post {
        success {
            archiveArtifacts artifacts: 'artifacts/model.pkl', fingerprint: true
        }
    }
}