pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                echo " Build"
//                 sh 'python3 getRandom.py'
                sh "mvn clean package"
            }
        }
        
        stage('SonarQube analysis') {
            steps {
                script{
                    def scannerHome = tool 'sonarscan';
                    withSonarQubeEnv('sonarqube') {
                           sh "mvn verify org.sonarsource.scanner.maven:sonar-maven-plugin:sonar -Dsonar.projectKey=pojjala_jenkinpipeline"
//                         sh "${tool("sonarscan")}/bin/sonar-scanner \
//                         -Dsonar.projectKey=reactapp \
//                         -Dsonar.projectName=reactapp"
                    }
                }
            }
        }
        stage('Execute') { 
            steps {
                echo " test"
//                 sh 'python3 getRandom.py'
//                 sh "java Hello"
            }
        }
        stage('Deploy') { 
            steps {
                echo " Deploy_1"
            }
        }
    }
}
