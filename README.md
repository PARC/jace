# jace
    HMC's Just Another Coaching Engine project serving NSF, NIH, and other funded projects
  ## settings.py
    django settings
  ## config.py
    scheduler settings
  ## urls.py
    top level API links
        

# user_model
    contains Infromation on the user,questions, answers
    
   ## rules.py
    rules for updatings users
   ## models.py
    locattion of django models
   ## signal.py
        this is where messages are processed at the moment of posting. It works by looking for a signal
        that a item was posted to communications, and then sorts it into the user model's models. It also has 
        the feature of updating the last heard from date for a particular user.
   ## serializer.py
    serialized the user models
   ## tasks.py
        MUST be names tasks for HUEY to find it, contains the scheduled item, and the schudler.

# communications
    contains all programs invovled in the API
   ##views.py
      API GENERATION ENGINE
   ##URLS.PY
        REGEX URL LINKS FOR API
   ## models.py
    location of reports models for django


# Transactions

    checks to see if there are any missing datas

# commands
 
 ## Update the day and check all rules (run update) for external scheduler!!!
 python manage.py runscript updates 
 ## Run the server
 $ ./run_local
 ## run setup
 $ sh setup.sh
 
 
# issues
   ## typeError message in server readout, 
        try flushing DB  $ python manage.py flush
   
   ## server not running
        try ./run_local
        
    
        
 