@Library('my-shared-library') _

pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'echo "Building..."'
            }
        }
        stage('My stage') {
          steps {
              script {
                  def myVar = com.mycompany.utils.MyUtils.doSomething()
                  echo "My variable: ${myVar}"
                  myCustomStep()
              }
          }
        }
        stage('Test') {
            steps {
                sh 'echo "Testing..."'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "Deploying..."'
            }
        }
    }
}
