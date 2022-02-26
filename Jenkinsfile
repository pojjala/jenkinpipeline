pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                echo " Build"
                sh 'python3 Hello.py'
            }
        }
        stage('Execute') { 
            steps {
                echo " test"
                sh 'python3 Hello.py'
            }
        }
        stage('Deploy') { 
            steps {
                echo " Deploy"
            }
        }
    }
}
