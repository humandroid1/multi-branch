node{
   stage('SCM Checkout'){
     git 'https://github.com/vishnu2198/multi-branch.git'
     }
  
  
  stage("Copying files to other instance"){
      sh 'scp -o StrictHostKeyChecking=no /var/lib/jenkins/workspace/airflow_final/*.py  ec2-user@3.85.33.216:/home/ec2-user/vish/'
       }
  stage("Installing Dependencies automatically")
  {
   sh  "ssh -v ec2-user@3.85.33.216 'python /home/ec2-user/vish/autoimport.py"
  }
  //stage("Deploying in airflow"){
  //echo "hiiiiii"
  //}
  //}
