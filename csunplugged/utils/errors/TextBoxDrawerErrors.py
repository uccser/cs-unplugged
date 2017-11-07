class TextBoxDrawerError(Exception):
    pass

class MissingSVGFile(TextBoxDrawerError):
    pass

class TextBoxNotFoundInSVG(TextBoxDrawerError):
    pass

class MissingSVGViewBox(TextBoxDrawerError):
    pass
