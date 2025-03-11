import json

tasks = {'1':'Djordje',
         '2': 'Nikola',
         '3':'Mare'}
doneTasks = {}
notTasks = {}
inProgress = {}


class TaskTracker():
    
    def add_task(self):
        while True:
            newTask = input('New task y/n: ')
            if newTask == 'y':
                task = input('Enter a new task: ')
                keys = input('Now name your task: ')
                tasks.update({keys:task})
                
            elif newTask == 'n':
                print('Thank you')
                break
            else:
                print('Please try again')   
                
                
     
            
    def done_tasks(self):
        active = Update()
        
        if len(doneTasks) == 0:
            print('Not tasks yet')
        
        else:
            print('Your done tasks')
            for key, value in doneTasks.items():
                print(f'[{key}] {value}')
                            
                            
                            
                
    def schedule_task(self):
            while True:
                print('\n==== Tasks ===== ')
                print('1. Done tasks')
                print('2. Not done tasks')
                print('3. Tasks in progress')
                print('4. Schedule task')
                print('5. Back')
                
                choice = input('Enter number: ')
                if choice == '1':
                    if len(doneTasks) == 0:
                        print('Not tasks yet')
                    
                    else:
                        print('Your done tasks')
                        for key, value in doneTasks.items():
                            print(f'[{key}] {value}')
                elif choice == '2':
                    if len(notTasks) == 0:
                        print('Not tasks yet')
                    
                    else:
                        print('Your done tasks')
                        for key, value in notTasks.items():
                            print(f'[{key}] {value}')
                elif choice == '3':
                    
                    if len(inProgress) == 0:
                        print('Not tasks yet')
                    
                    else:
                        print('Your done tasks')
                        for key, value in inProgress.items():
                            print(f'[{key}] {value}')  
                            
                elif choice == '4': 
                    while True: 
                        for key, value in tasks.items():
                            print(f'[{key}] {value}')     
                        shedule = input('Choice task you want to schedule by name: ')
                        
                        if shedule in tasks.keys():
                            where = int(input('Where do you want to shedule it?:\n 1 ~ Done tasks\n 2 ~ Not done tasks\n 3 ~ Still in progress: '))
                            if where == 1:
                                if shedule in tasks.keys(): 
                                    for k,v in tasks.items():
                                        if k == shedule:
                                            doneTasks.update({k:v})
                                            print(doneTasks)
                                break
                            
                            elif where == 2:
                                if shedule in tasks.keys(): 
                                    for k,v in tasks.items():
                                        if k == shedule:
                                            notTasks.update({k:v})
                                            print(notTasks)
                                break

                            elif where == 3:
                                if shedule in tasks.keys(): 
                                    for k,v in tasks.items():
                                        if k == shedule:
                                            inProgress.update({k:v})
                                            print(inProgress)
                                break
                            else:
                                print("We don't have that option. Please try again.")  
                        else:
                            back = input("We don't have that option. Please try again or get back\n Back ~ 1: ")
                            if back == '1':
                                break
                                             
                elif choice == '5':
                    break  
                
                else:
                    print('Please try again')  
                    
                    
                    
     

    def view(self):
        if len(tasks) == 0:
            print('Not tasks yet')  
        else:
            print('Your tasks:\n ')
            
            for key, value in tasks.items():
                print(f'[{key}] {value}')
                
    def save_tasks(self):
        while True:
            print('\n==== Tasks to Save ===== ')
            print('1. Save all tasks')
            print('2. Save done tasks')
            print('3. Save not done tasks')
            print('4. Save tasks in progress')
            print('5. Back')
            
            save = input('Enter number: ') 
            if save == '1':
                if len(tasks) == 0:
                    print('Not tasks to save')
                else:   
                    with open('tasks.json','w') as file:
                        json.dump(tasks, file)
                        break
                        
            elif save == '2':
                if len(doneTasks) == 0:
                    print('Not tasks to save')
                else:    
                    with open('doneTasks.json','w') as file:
                        json.dump(doneTasks, file)
                        break
                    
            elif save == '3':
                if len(notTasks) == 0:
                    print('Not tasks to save')
                else:    
                    with open('notTasks.json','w') as file:
                        json.dump(notTasks, file)
                        break
                    
            elif save == '4':
                if len(inProgress) == 0:
                    print('Not tasks to save')
                else:    
                    with open('inProgress.json','w') as file:
                        json.dump(inProgress, file)
                        break    
            else:
                break                   
                        
                                    
                
                
    def delete_task(self):
        if len(tasks) == 0:
            print('No task to delete')
            
        else:
            print('Delete your tasks:\n ')
            
            for key, value in tasks.items():
                print(f'[{key}] {value}')
            while True:
                choice = input('Choice task do delete buy name: ')
                if choice in tasks.keys():
                    del tasks[choice]
                    print('Your task is deleted')
                    break
                else:
                    print('Try again')
                                
            
    
    
    
    def main(self):
        active = TaskTracker()
        update = Update(tasks,doneTasks,notTasks,inProgress)
        while True:
            print('\n==== To-Do-List Application ===== ')
            print('1. Add task')
            print('2. View all tasks')
            print('3. Shedule tasks')
            print('4. Update tasks')
            print('5. Save tasks')
            print('6. Delete task')
            
            choice = int(input('Enter your choice: '))
            if choice == 1:
                active.add_task()
            elif choice == 2:
                active.view()  
            elif choice == 3:
                active.schedule_task()
            elif choice == 4:    
                update.update_task()
            elif choice == 5:
                active.save_tasks()     
            elif choice == 6:
                active.delete_task()
     
                        
                
          
class Update():
    
    def __init__(self,dicT,dicD,dicN,dicP):
        self.dicT = dicT
        self.dicD = dicD
        self.dicN = dicN
        self.dicP = dicP

                  
    def update_task(self): 
        while True:
            print('\n==== Update Tasks ===== ')
            print('1. All tasks')
            print('2. Done tasks')
            print('3. Not done tasks')
            print('4. Tasks in progress')
            print('5. Back')
            choice = input('Enter number: ')
            
            if choice == '1':
                self.dicT = tasks 
                if len(self.dicT) == 0:
                    print('No task to update')
                else:   
                    print('All tasks:\n ')    
                    for key, value in self.dicT.items():
                        print(f'[{key}] {value}')
                    ind = input('What task do you want to update? write key: ')
                    if ind in self.dicT.keys():
                        for key, value in self.dicT.items():
                            print(f'Your text is ~ {value}')
                            break
                        rewrite = input('Now rewrite: ')
                        if ind in self.dicT.keys():
                                self.dicT.update({ind:rewrite})
                        else:
                            print('Try again')   
                    else:
                        print("Don't have that task. Try again")        
                        
            elif choice == '2':
                self.dicD = doneTasks
                self.dicT = tasks
                if len(self.dicD) == 0:
                    print('No task to update')
                else:   
                    print('All tasks:\n ')
                            
                    for key, value in self.dicD.items():
                        print(f'[{key}] {value}')
                    ind = input('What task do you want to update? write name: ')
                    if ind in self.dicD.keys():
                        for key, value in self.dicD.items():
                            print(f'Your text is ~ {value}')
                            break
                        rewrite = input('Now rewrite: ')
                        if ind in self.dicD.keys():
                                self.dicD.update({ind:rewrite})
                                self.dicT.update({ind:rewrite})
                        else:
                            print('Try again')   
                    else:
                        print("Don't have that task. Try again")  
                        
            elif choice == '3':
                self.dicN = notTasks
                self.dicT = tasks
                if len(self.dicN) == 0:
                    print('No task to update')
                else:   
                    print('All tasks:\n ')
                            
                    for key, value in self.dicN.items():
                        print(f'[{key}] {value}')
                    ind = input('What task do you want to update? write name: ')
                    if ind in self.dicN.keys():
                        for key, value in self.dicN.items():
                            print(f'Your text is ~ {value}')
                            break
                        rewrite = input('Now rewrite: ')
                        if ind in self.dicN.keys():
                                self.dicN.update({ind:rewrite})
                                self.dicT.update({ind:rewrite})
                        else:
                            print('Try again')   
                    else:
                        print("Don't have that task. Try again")  
            
            elif choice == '4':
                self.dicP = inProgress
                self.dicT = tasks
                if len(self.dicP) == 0:
                    print('No task to update')
                else:   
                    print('All tasks:\n ')
                            
                    for key, value in self.dicP.items():
                        print(f'[{key}] {value}')
                    ind = input('What task do you want to update? write name: ')
                    if ind in self.dicP.keys():
                        for key, value in self.dicP.items():
                            print(f'Your text is ~ {value}')
                            break
                        rewrite = input('Now rewrite: ')
                        if ind in self.dicP.keys():
                                self.dicP.update({ind:rewrite})
                                self.dicT.update({ind:rewrite})
                        else:
                            print('Try again')   
                    else:
                        print("Don't have that task. Try again")  
                        
            elif choice == '5':
                break

                                        
                                        
                                    
                            
                    
                  
                
       
                        
            

if __name__ == '__main__':
    active = TaskTracker()
    work = active.main()