# SIG Tracker
<<<<<<< HEAD

_In house application for tracking SIG progress and feedback._

The name of the project is 'sig_tracker' and 'about_sig’ is the name of app. 

This app contains the home page housing info what sigs are and links to individual sig progress.

## How to run?

#### Setting up the Development Environment

1.	For people using python3 virtual environment:

To install python3 virtual environment, refer this-

i.	
        
             
        pip install virtualenv
        
        virtualenv --python==python3 sig_tracker
        
        source sig_tracker/bin/activate 
        
     
 
      
ii.	The base directory contains 'requirements.txt' file.

iii.     To replicate the same environment:   

         pip install -r requirements.txt
        
      

#### Running for the first time:

1.	To migrate databases:

             
        python manage.py makemigrations

        python manage.py migrate
        
    
3.	Start the development server:
     
        python manage.py runserver
        
        
      
    
_Please file an issue if you face any problem while running the app. Improvements are always welcome. Feel free to fork the repository and send in pull requests with proper commit messages.

=======
*In house application for tracking SIG progress and feedback.*<br>
The name of the project is 'sig_tracker' and 'about_sig’ is the name of app. <br>
This app contains the home page housing info what sigs are and links to individual sig progress.<br>
## How to run?
#### Setting up the Development Environment
For python3 virtual environment:<br>
1. To install python3 virtual environment, refer this:<br>
   ```bash
   pip install virtualenv
   virtualenv --python==python3 sig_tracker
   source sig_tracker/bin/activate 
   ```
2. The base directory contains 'requirements.txt' file. To replicate the same environment:<br>
   ```bash
   pip install -r requirements.txt<br>
   ```

#### Running for the first time:
1. To migrate databases:<br>
   ```bash
    python manage.py makemigrations [app_name]<br>
    python manage.py migrate<br>
   ```
2. Start the development server:<br>
   ```bash
   python manage.py runserver
   ```
Please file an issue if you face any problem while running the app.<br> 
Improvements are always welcome.<br>
Feel free to fork the repository and send in pull requests with proper commit messages.
>>>>>>> upstream/master
