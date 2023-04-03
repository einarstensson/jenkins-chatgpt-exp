@Library('jenkins-chatgpt-shared-library-exp') _

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
        stage('Run Python script') {
            steps {
                withEnv(['MY_ENV_VAR=${MY_ENV_VAR}']) {
                    sh 'ls -la'
                    sh 'pip install -r ./requirements.txt'
                    sh 'python3 scripts/s3_bucket_ls.py'
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
