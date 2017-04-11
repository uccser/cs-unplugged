from .Error import Error

class UnitPlanHasNoLessonsError(Error):
    '''Raised when there are not lessons given for a unit plan
    '''
    
    def __init__(self):
    	super().__init__()
