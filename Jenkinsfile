pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                echo 'Starting Capstone Pipeline...'
            }
        }
        stage('Run Parallel Tests') {
            steps {
                bat '"C:\\Users\\New Computer Arena\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pytest -n 2 -v --html=report.html --self-contained-html'
            }
        }
    }
    post {
        always {
            publishHTML([
                allowMissing: false, 
                alwaysLinkToLastBuild: true, 
                keepAll: true, 
                reportDir: '.', 
                reportFiles: 'report.html', 
                reportName: 'Capstone Test Report'
            ])
        }
        success {
            echo 'Build PASSED - Ready for Deployment!'
        }
        failure {
            echo 'Build FAILED - Check Report!'
        }
    }
}