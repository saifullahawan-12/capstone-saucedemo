pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
            args '-u root'
        }
    }
    stages {
        stage('Setup') {
            steps {
                echo 'Starting Capstone Pipeline - Dockerized...'
                sh 'python --version'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest -v --html=report.html --self-contained-html -n 2'
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
                reportName: 'Capstone Docker Report'
            ])
            emailext(
                subject: "Capstone Build: ${currentBuild.currentResult} - Build #${env.BUILD_NUMBER}",
                body: """
                <p>Build Status: <b>${currentBuild.currentResult}</b></p>
                <p>Build Number: ${env.BUILD_NUMBER}</p>
                <p>Check report: ${env.BUILD_URL}HTML_20Report/</p>
                <p>Logs: ${env.BUILD_URL}console</p>
                """,
                to: "saifullahimran553@gmail.com",
                mimeType: 'text/html'
            )
        }
        success {
            echo 'Build PASSED - Dockerized CI Complete - Ready for CD!'
        }
        failure {
            echo 'Build FAILED - Check Email & Report!'
        }
    }
}
