def func1(): 
  return "True" 
  
def func2(): 
  return "False"
def _if(bool, func1, func2):
    if bool: return func1()
    else: return func2()
