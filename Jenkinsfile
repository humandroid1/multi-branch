node{
   stage('SCM Checkout'){
     git 'https://github.com/vishnu2198/multi-branch.git'
     }
 sshagent(['jenkinstom']) { 
  
  stage("Copying files to other instance"){
      sh 'scp -o StrictHostKeyChecking=no /var/lib/jenkins/workspace/autoimport_checkout/*.py  ec2-user@3.85.33.216:/home/ec2-user/vish/'
       }
  stage("Installing Dependencies automatically")
  {
      //sh  "ssh  ec2-user@3.85.33.216 ' cd /home/ec2-user/vish/' "
   sh  "ssh  ec2-user@3.85.33.216 'sudo python autoimport.py' "
  }
  //stage("Deploying in airflow"){
  //echo "hiiiiii"
  //}
 }
  }
