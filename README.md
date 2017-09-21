# jace
   HMC's Just Another Coaching Engine project serving NSF, NIH, and other funded projects
  ## settings.py
   django settings
  ## config.py
   scheduler settings
  ## urls.py
   main subfields for API links
        

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
   ## urls.py
   placeholder for future urls, don't delete

# communications
    contains all programs invovled in the API
   ##views.py
   creates, and serializes objects when the api is called.
   ## serializer.py
   serializor for the reports objects
   ## models.py
   Contains a catch all store for all incoming messages to jace, stores information about the data and source
   as reports
   ## urls.py
   This is where the api is generated. It uses regex to build, note however all of these are in
   the subdirectory communications. Example  
```
   localhost:8888/communications/reports/
```


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
   try flushing DB
        
          
```        

$ python manage.py flush

```
        
        
        
        
   
   ## server not running
        try ./run_local
        
    
        
 