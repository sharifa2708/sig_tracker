# SIG Tracker
_In house application for tracking SIG progress and feedback._<br>
The name of the project is 'sig_tracker' and 'about_sig’ is the name of app. <br>
This app contains the home page housing info what sigs are and links to individual sig progress.<br>
## How to run?
#### Setting up the Development Environment
1.For people using python3 virtual environment:<br>
i.To install python3 virtual environment, refer this:<br>
    
    pip install virtualenv
    virtualenv --python==python3 sig_tracker
    source sig_tracker/bin/activate 
   
ii.	The base directory contains 'requirements.txt' file.<br>
iii. To replicate the same environment:   <br>
    
    pip install -r requirements.txt<br>
    
#### Running for the first time:
1.To migrate databases:<br>
    
    python manage.py makemigrations<br>
    python manage.py migrate<br>
    
2.Start the development server:<br>
     
    python manage.py runserver
     
_Please file an issue if you face any problem while running the app. Improvements are always welcome. Feel free to fork the repository and send in pull requests with proper commit messages.

