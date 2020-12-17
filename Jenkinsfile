pipeline{
  agent any
  stages {
  	stage('Build docker image'){
  		steps{
  			script{
  				if (env.BRANCH_ENV != 'master') {
		    		sh 'docker build -t app .'
		  		}
				}
    	}
    }
    
    stage('Run containerized application'){
      steps{
  			script{
  				if (env.BRANCH_ENV != 'master' ) {
		    		bat 'docker run -p 5000:5000 app'
		  		}
				}
    	}
    }
		/*
    stage('Integration and Unit tests '){
     		steps{
     			script{
     				if (env.BRANCH_NAME == 'feature' ) {
							bat 'python test_unit.py'
              bat 'python test_integration.py'
		    	}
				}
			}
		}
		 stage('stress_test'){
				steps{
					script{
    				if (env.BRANCH_NAME == 'develop') {
      				bat 'python test_stress.py'
					}
				}
				
		  }
		}
	
    
		
		
		*/
		
	
		stage('push to release'){
				steps{
					script{
    				if (env.BRANCH_NAME == 'develop') {
    					bat 'git checkout -b release || git checkout release'	
    					bat 'git fetch'	
    					bat 'git pull'
    					bat 'git merge origin/develop'
    					bat 'git commit --allow-empty -m "release the application"'
    					bat 'git push -f https://Kimpouni:Codelyoko_93@github.com/AnasE17/Project-Data-Engineering-2.git'
					}
				}
				
		  }
		}
		
		stage('Release phase'){
     		steps{
     			script{
     				if (env.BRANCH_NAME == 'release') {
							echo '"deploying"' 
		    	}
				}
			}
		}
		
		stage('User acceptance'){
     		steps{
     			script{
     				if (env.BRANCH_NAME == 'release') {
							input 'Accept merge to master ??'
		    	}
				}
			}
		}
		
		stage('Final merging'){
     		steps{
     			script{
     				if (env.BRANCH_NAME == 'release') {
							bat 'git checkout -b main || git checkout main'
							bat 'git merge origin/release'
							bat 'git push -f https://Kimpouni:Codelyoko_93@github.com/AnasE17/Project-Data-Engineering-2.git'
		    	}
				}
			}
		}
				
				
		stage('Delete container'){
     		steps{
     			script{
     				if (env.BRANCH_NAME != 'master') {
							bat 'docker rmi -f app'
		    	}
				}
			}
		}
		
		
	}
}
