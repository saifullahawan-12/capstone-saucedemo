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
            emailext(
                subject: "PASS: ${env.JOB_NAME} - Build #${env.BUILD_NUMBER}",
                body: """<p>Good news! Build PASSED.</p>
                        <p>Job: ${env.JOB_NAME}<br>
                        Build Number: ${env.BUILD_NUMBER}<br>
                        Build URL: <a href="${env.BUILD_URL}">${env.BUILD_URL}</a><br>
                        Report: <a href="${env.BUILD_URL}Capstone_20Test_20Report">Click Here</a></p>""",
                to: "saifullahimran553@gmail.com",
                mimeType: 'text/html'
            )
        }
        failure {
            echo 'Build FAILED - Check Report!'
            emailext(
                subject: "FAIL: ${env.JOB_NAME} - Build #${env.BUILD_NUMBER}",
                body: """<p>Build FAILED - Please check.</p>
                        <p>Job: ${env.JOB_NAME}<br>
                        Build Number: ${env.BUILD_NUMBER}<br>
                        Build URL: <a href="${env.BUILD_URL}">${env.BUILD_URL}</a><br>
                        Report: <a href="${env.BUILD_URL}Capstone_20Test_20Report">Click Here</a></p>""",
                to: "saifullahimran553@gmail.com",
                mimeType: 'text/html',
                attachmentsPattern: 'report.html'
            )
        }
    }
}
