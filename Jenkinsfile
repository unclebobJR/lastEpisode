 node ('master'){
  stage ('Build and Test') {
    checkout scm
    sh 'pwd'
    sh 'test'
    stage 'Deploy'
  }
 }
