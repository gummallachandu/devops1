pipeline {
  agent any
  stages {
    stage('preperation') {
      steps {
        git(url: 'https://github.com/itskrish9/devops_python', branch: 'master', credentialsId: 'github')
      }
    }
    stage('build') {
      steps {
        powershell 'python3 app.py'
      }
    }
  }
}