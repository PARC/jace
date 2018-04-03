_This is research code in its ugly and glorious form, used just for testing ideas. The complaint dept is located in /dev/null; otherwise, you are welcome to fix anything you have an issue with._

# What is jace?

Jace is Just Another Coaching Engine. HMC's Just Another Coaching Engine project serving NSF, NIH, and other funded projects

##How does it work?

Jace accepts incoming posts via its API and then disseminates that information into a user_model.
The user_model consists of a User, Question, Answer, and Survey. The user_model also contains a rules function, this allows
updates to the User_Model's models, or updates caused by. 

Normaly when a rule is triggered it tells the communication manager to send a message to the application server.
This message is to turn on or off a question set. There is also the ability to send a fully loaded question if needed.


# Installation

1. Make a container for alpine-linux
2. Make a container for redis and postgres
3. Redis should be set to port 36379, postgres to 32768
4. Set docker port in alpine-linux to 8000, and the published port to 8888
5. In alpine-linux general make a new environmental setting called POSTGRES and set it to 32768
6. Also, in general, make a new environmental setting called REDIS and set it to 32769
7. ```$ apk update```
8. ```$ apk add python3, gcc, git```
9. ```$ git clone http://github.com/parc/jace.git``` 
10. ``` sh setup.sh ```

# Making a rule

First create your content, in the example json format. Make sure that there is some variable in the attributes section.
This value controls whether or not a content item will be seen. Note that for some cases it is important to have multiple permutations  

Note the formula is ((2^n)-n+1) where n is the number of conditions. 

The other basic logic formula for determining if a stimulus should fire is 

if (Item.1 or Item.2 or Item.X), then Target

After content creation, go to usermodels/rules.py and write a function, you may find that you need to add in slots in the
user model, if so edit accordingly, and then run.
```$ sh update_all_models.sh```


# Quick start
```
sh run_jace.sh
```
##Normal Start
```
./run_local
./manage.py run_huey
```

# jace
  Just Another Coaching Engine project serving NSF, NIH, and other funded projects
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
   This is where messages are processed at the moment of posting. It works by looking for a signal
   that a item was posted to communications, and then sorts it into the user model's models. It also has 
   the feature of updating the last heard from date for a particular user.
   ## serializer.py
   Serializer for the user models
   ## tasks.py
   MUST be names tasks.py for HUEY to find it, contains the scheduled item(s), and the schudler.
   ## urls.py
   placeholder for future urls, don't delete

# communications
    contains all programs invovled in the API
   ## views.py
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
        
    
## LICENSES

_Source Code, Non-Commercial Use Permitted under the following conditions_

This software is licensed under the [Aladdin Free Public License](https://github.com/PARC/jace/blob/master/LICENSE-AFPL.md). A [quick summary](https://tldrlegal.com/license/aladdin-free-public-license#summary) of this license is that you CAN Modify and Distribute, you CANNOT Hold Liable, Sublicense, Place Warranty, or Use Comercially, and you MUST Include License, Include Original Code, and State Your Changes.

_Content, not code, Non-Commercial Use Permitted under the following conditions_

The non-code content in this repository is licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://github.com/PARC/jace/blob/master/CONTENT_LICENSE-CC-BY-NC-SA-4.md) (CC BY-NC-SA 4.0). A [quick summary](https://creativecommons.org/licenses/by-nc-sa/4.0/) of this license is that you ARE FREE to Share and Adapt PROVIDED that you Provide Attribution, Use Non-Commercially, and Share Alike.

_For those interested in Commercial Use, please contact PARC, Inc. by email at engage@parc.com_
 
