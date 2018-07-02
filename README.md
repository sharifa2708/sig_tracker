#SIG Tracker#
_In house application for tracking SIG progress and feedback._

The Project Name is 'sig_tracker'.
'about_sig’ is an app that contains the home page housing info what sigs are and links to individual sig progress.

##How to run?

####Setting up the Development Environment
1.	For people using python3 virtual environment:

i.	To install python3-venv, refer this

ii.	Create a folder 'environments'.

iii.	
        
      mkdir environments

      cd environments   
      
iv.	The base directory contains 'requirements.txt' file. To replicate the same environment:

v.	virtualenv sig_tracker

vi.	source sig_tracker/bin/activate

    pip install -r requirements.txt
    
####Running for the first time:

1.	To migrate databases:

2.	
     
       python manage.py makemigrations

       python manage.py migrate
    
3.	Start the development server:

    
        python manage.py runserver
    
_Raise issues if you face any problems with respect to firing up the app. Improvements are welcome. Just fork the repository, create PRs with meaningful commit messages._



