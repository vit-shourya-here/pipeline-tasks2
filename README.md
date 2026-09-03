#This is a readme file for an example respository!

#task1-Show files

<!-- pipeline{
    agent any
    stages{
        stage("Check out code"){
            steps{
                git branch: 'main', url: 'https://github.com/vit-shourya-here/pipeline-tasks2.git'
            }
        }
        
        stage('Show files'){
            steps{
                bat 'dir'
            }
        }
    }
} -->

#task2-print directory

<!-- pipeline{
    agent any
    stages{
        stage('Check out code'){
            steps{
                git branch: 'main', url: 'https://github.com/vit-shourya-here/pipeline-tasks2.git'
            }
        }
        stage('Print Directory'){
            steps{
                bat 'cd'
            }
        }
    }
} -->

#task3-print a message

<!-- pipeline{
    agent any
    stages{
        stage('Check out code'){
            steps{
                git branch: 'main', url: 'https://github.com/vit-shourya-here/pipeline-tasks2.git'
            }
        }
        stage('Print a message'){
            steps{
                echo 'Hello! Jenkins is running successfully here!'
            }
        }
    }
} -->

#task4-create a file

<!-- pipeline{
    agent any
    stages{
        stage('Check out code'){
            steps{
                git branch: 'main', url: 'https://github.com/vit-shourya-here/pipeline-tasks2.git'
            }
        }
        stage('Create a file'){
            steps{
                bat 'echo This is a new file made by jenkins > jenkins_demo.txt'
            }
        }
    }
} -->

#task5 - read file
<!-- pipeline{
    agent any
    stages{
        stage('Check out code'){
            steps{
                git branch: 'main', url: 'https://github.com/vit-shourya-here/pipeline-tasks2.git'
            }
        }
        stage('Read file'){
            steps{
                bat 'type README.md'
            }
        }
    }
} -->