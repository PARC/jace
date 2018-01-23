from user_model.rules import upkeep


# call this to update manualy

def run():
    for x in range(14):
        upkeep()
