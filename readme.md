pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/nedzte07-eng/hillel_homework'
            }
        }
        stage('Setup Python venv') {
            steps {
                sh '''
                #!/bin/bash
                apt-get update && apt-get install -y python3-venv
                python3 -m venv venv
                '''
            }
        }
            stage('Install Requirements') {
        steps {
            sh '''
            . venv/bin/activate
            pip install --upgrade pip
            pip install --cache-dir=$WORKSPACE/.pip_cache -r requirements_for_hw31.txt
            '''
        }
        }
        stage('Run tests') {
        steps {
            sh '''#!/bin/bash
                source venv/bin/activate
                echo "API_URL=https://qauto.forstudy.space/" > .env
                echo "EMAIL=nedzelnytskyidev+021123@gmail.com" >> .env
                echo "PASSWORD=GqNeQrjRLaT8dLM" >> .env
                echo "AUTH_BASIC_USER=guest" >> .env
                echo "AUTH_BASIC_PASSWORD=welcome2qauto" >> .env
                pytest tests/api_tests/lesson_30_tests/test_homework_30.py --alluredir=allure-results'''
        }
        }
    }
}