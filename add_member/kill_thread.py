import os                                                                       
from multiprocessing import Pool
import keyboard

def run():                                                                                                                             
                                                                                                                                                    
    processes = ('process1.py', 'process2.py', 'process3.py')                                                                              
                                                                                
    def run_process(process):              # fix                                               
        os.system('python {}'.format(process))                                       
                                                                                
                                                                                
    pool = Pool(processes=3)                                                        
    pool.map(run_process, processes)

def kill(all_processes):
    for process in all_processes:
        
        process.terminate()

def press_key(all_processes):
    while True:  # making a loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                print('You Pressed A Key!')
                for i in range(3):
                    os.kill(pool._pool[0].pid,signal.SIGTERM)
                kill(all_processes)
                break  # finishing the loop
        except:
            break  # if user pressed a key other than the given key the loop will break


if __name__ == "__main__":
    run()
    all_processes = ('process1.py', 'process2.py', 'process3.py')
    press_key(all_processes)
    
