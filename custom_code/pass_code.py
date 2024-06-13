
#password encryption 

def pass_argument(password_):
    try:
        refactoring = password_ * 100000000 // -300000000
        
        next_phase = refactoring * 2.10 // -3 
        next_new_phase = next_phase * 214793
       
        return int(next_new_phase)
    
    except SyntaxError as e:
        print('There was a error {}'.format(e))
