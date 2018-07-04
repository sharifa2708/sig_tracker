# SIG Tracker

_In house application for tracking SIG progress and feedback._

The name of the project is 'sig_tracker' and 'about_sig’ is the name of app. 

This app contains the home page housing info what sigs are and links to individual sig progress.

## How to run?

#### Setting up the Development Environment

1.	For people using python3 virtual environment:

To install python3 virtual environment, refer this-

i.	
        
        '''bash
        
        pip install virtualenv
        
        '''
        
        '''bash
        
        virtualenv --python==python3 sig_tracker
        
        '''

        '''bash
        
        source sig_tracker/bin/activate 
        
        '''
 
      
ii.	The base directory contains 'requirements.txt' file.

iii.     To replicate the same environment:   

        '''bash

        pip install -r requirements.txt
        
        '''

#### Running for the first time:

1.	To migrate databases:

        '''bash
        
        python manage.py makemigrations

        '''
        
        '''bash
        
        python manage.py migrate
        
        '''
 
    
3.	Start the development server:
     
        '''bash
        
        python manage.py runserver
        
        '''
      
    
_Please file an issue if you face any problem while running the app. Improvements are always welcome. Feel free to fork the repository and send in pull requests with proper commit messages.

