pipeline {
    // Agregamos el parámetro label para cumplir con la regla de Jenkins
    agent {
        node {
            label '' // <-- Esta es la pieza clave que faltaba
            customWorkspace 'C:\\Users\\Nelson\\Documents\\GitHub\\Reto-2_SauceDemo-Playwright-python-'
        }
    }

    environment {
        PYTHONDONTWRITEBYTECODE = '1'
    }

    stages {
        stage('Setup & Playwright') {
            steps {
                echo "Ejecutando directamente desde el entorno local..."
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate.bat
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                playwright install chromium --with-deps
                '''
            }
        }
        
        stage('Execute Tests') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    echo "Corriendo pruebas BDD de forma local..."
                    bat '''
                    call venv\\Scripts\\activate.bat
                    pytest tests/ --alluredir=allure-results
                    '''
                }
            }
        }
    }

    post {
        always {
            echo "Generando Reporte de Allure..."
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}