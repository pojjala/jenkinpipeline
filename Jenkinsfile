pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                echo " Build"
                javac HelloWorld.java
            }
        }
        stage('Execute') { 
            steps {
                echo " test"
                java HelloWorld
            }
        }
        stage('Deploy') { 
            steps {
                echo " Deploy"
            }
        }
    }
}
