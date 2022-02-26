pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                echo " Build"
                javac HellowWorld.java
            }
        }
        stage('Execute') { 
            steps {
                echo " test"
                java HellowWorld
            }
        }
        stage('Deploy') { 
            steps {
                echo " Deploy"
            }
        }
    }
}
