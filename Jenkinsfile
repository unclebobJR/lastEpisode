 node ('master'){
  stage ('Build and Test') {
    checkout scm
    sh 'test'
    stage 'Deploy'
  }
 }
