pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                echo " Build"
//                 sh 'python3 getRandom.py'
                sh "javac Hello.java"
            }
        }
        stage('Execute') { 
            steps {
                echo " test"
                sh 'python3 getRandom.py'
                sh "java Hello"
            }
        }
        stage('Deploy') { 
            steps {
                echo " Deploy_1"
            }
        }
    }
}
