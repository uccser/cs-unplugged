from .Error import Error

class TopicHasNoUnitPlansError(Error):
    '''Raised when there are not unit plans listed in a topic's yaml file
    '''
    
    def __init__(self):
    	super().__init__()
