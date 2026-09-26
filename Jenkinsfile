pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                echo 'Starting Capstone Pipeline - Docker Ready...'
                bat '"C:\\Users\\New Computer Arena\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" --version'
                bat '"C:\\Users\\New Computer Arena\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\New Computer Arena\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pytest -v --html=report.html --self-contained-html -n 2'
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
            emailext(
                subject: "Capstone Build: ${currentBuild.currentResult} - Build #${env.BUILD_NUMBER}",
                body: """
                <h2>Capstone Saucedemo - Build ${env.BUILD_NUMBER}</h2>
                <p><b>Status:</b> ${currentBuild.currentResult}</p>
                <p>View online: <a href="${env.BUILD_URL}HTML_20Report/">Click Here for HTML Report</a></p>
                <p>Console: <a href="${env.BUILD_URL}console">${env.BUILD_URL}console</a></p>
                <br>
                <p>Full report is attached.</p>
                """,
                to: "saifullahimran553@gmail.com",
                mimeType: 'text/html',
                attachmentsPattern: 'report.html'
            )
        }
        success {
            echo 'Build PASSED - Ready for CD!'
        }
        failure {
            echo 'Build FAILED!'
        }
    }
}
