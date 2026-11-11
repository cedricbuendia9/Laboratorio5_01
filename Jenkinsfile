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

        //stage('Run Container') {
        //    steps {
        //        sh 'docker run --rm diabetes-model'
        //    }
        //}
        stage('Deploy API') {
            steps {
                sh '''
                docker stop diabetes-api || true
                docker rm diabetes-api || true

                docker run -d \
                --name diabetes-api \
                -p 5000:5000 \
                --restart unless-stopped \
                diabetes-model
            '''
        }


    }

    post {
        success {
            archiveArtifacts artifacts: 'artifacts/model.pkl', fingerprint: true
        }
    }
}