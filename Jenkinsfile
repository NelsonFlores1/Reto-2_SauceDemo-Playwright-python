pipeline {
    agent any // En proyectos avanzados, aquí se usa un contenedor de Docker con Playwright

    environment {
        // Establecer variables de entorno para evitar que Python genere archivos .pyc
        PYTHONDONTWRITEBYTECODE = '1'
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Descarga el código desde tu repositorio (GitHub, GitLab, etc.)
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                script {
                    echo "Setting up Python Virtual Environment and Dependencies..."
                    sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Install Playwright Browsers') {
            steps {
                script {
                    echo "Installing Playwright Chromium browser..."
                    sh '''
                    . venv/bin/activate
                    playwright install chromium --with-deps
                    '''
                }
            }
        }

        stage('Execute Tests') {
            steps {
                // Usamos catchError para que, si fallan las pruebas, el pipeline continúe 
                // y pueda generar el reporte de Allure en el siguiente paso.
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    script {
                        echo "Running BDD Tests..."
                        sh '''
                        . venv/bin/activate
                        # Ejecución obligatoria en modo HEADLESS (sin interfaz gráfica)
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
            // Esto toma los JSON generados por pytest y construye el reporte HTML en Jenkins
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            
            // Limpieza del workspace para no acumular archivos pesados
            cleanWs() 
        }
    }
}