pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                echo " Build"
                sh 'javac HelloWorld.java'
            }
        }
        stage('Execute') { 
            steps {
                echo " test"
                sh 'java HelloWorld'
            }
        }
        stage('Deploy') { 
            steps {
                echo " Deploy"
            }
        }
    }
}
