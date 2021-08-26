
def qst(arg):
    questions = {}
    questions[1] = "Question1:\nThe following decorator will:\n\ndef decorator(func):\n     @wraps(func):\n     def wrapper(*args,**kwargs):\n          return int(func(*args,**kwargs))\nreturn wrapper"
    questions[2] = "Question2:\nWhat objects can be decorated?"
    questions[3]= "Question3:\nWhat will my_func() return?\n\ndef decorator1(func):\n     @wraps(func)\n     def wrapper(*args,**kwargs):\n               return tuple(func(*args,**kwargs))\n     return wrapper"
    return questions[arg]