pipeline {
    agent any

    stages {

        stage('GitHub Clone') {
            steps {
                git 'https://github.com/Mariakhan19/student-course-registration.git'
            }
        }

        stage('Build Backend Image') {
            steps {
                sh 'docker build -t student-backend ./backend'
            }
        }

        stage('Build Frontend Image') {
            steps {
                sh 'docker build -t student-frontend ./frontend'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                docker stack deploy -c docker-compose.yml student-app
                '''
            }
        }
    }
}
