pipeline {
  agent {
    dockerfile {
      filename 'todoapp'
    }

  }
  stages {
    stage('preperation') {
      steps {
        git(url: 'https://github.com/itskrish9/devops_python', branch: 'master', credentialsId: 'github')
      }
    }
    stage('build') {
      steps {
        sh 'python3 app1.py'
      }
    }
    stage('archive') {
      steps {
        archiveArtifacts(allowEmptyArchive: true, artifacts: '*.py')
        echo 'successfully executed'
      }
    }
  }
}