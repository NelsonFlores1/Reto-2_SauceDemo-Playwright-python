pipeline {
    agent any

    environment {
        PYTHONDONTWRITEBYTECODE = '1'
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                script {
                    echo "Setting up Python Virtual Environment and Dependencies..."
                    // Cambiamos 'sh' por 'bat' y usamos la ruta de Windows para el entorno virtual
                    bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate.bat
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Install Playwright Browsers') {
            steps {
                script {
                    echo "Installing Playwright Chromium browser..."
                    bat '''
                    call venv\\Scripts\\activate.bat
                    playwright install chromium --with-deps
                    '''
                }
            }
        }

        stage('Execute Tests') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    script {
                        echo "Running BDD Tests..."
                        bat '''
                        call venv\\Scripts\\activate.bat
                        pytest tests/ --alluredir=allure-results
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            echo "Generating Allure Report..."
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            cleanWs() 
        }
    }
}