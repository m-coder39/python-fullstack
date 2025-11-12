

def add_task(task):
    'Add task'
    f=open('tasks.txt','a')
    s=task+'-pending'
    f.write(s+"\n")
    f.close()
def view_all_tasks():
    'View all tasks'
    f=open('tasks.txt','r')
    print(f.read())
    f.close()
def mark_completed(comp_task):
    'mark as completed'
    f=open('tasks.txt','r')
    lines = f.readlines()
    f.close()

    f=open('tasks.txt','w')
    for line in lines:
       if(comp_task in line and 'Pending' in line):
           line=line.replace('Pending','completed')
       elif (comp_task in line and 'pending' in line):
           line = line.replace('pending', 'completed')
       f.write(line)
    f.close()
    print("task marked as completed")
def delete(task):
    f=open('tasks.txt','r')
    lines=f.readlines()
    f.close()
    found=False
    f = open('tasks.txt', 'w')
    for line in lines:
        if(task not in line):
            f.write(line)
        else:
            found=True
    if found:
        print("deleted successfully")
    else:
        print("not found")


def func():
    print("Menu")
    print("1.Add a new task\n2.View all tasks\n3.Mark a task as completed\n4.Delete a task\n5.Exit the program")
    ch=int(input("enter your choice:"))
    if(ch==1):
        new_task=input("enter the new task")
        add_task(new_task)
    elif(ch==2):
        view_all_tasks()
    elif(ch==3):
        comp_task=input("enter the task name")
        mark_completed(comp_task)
    elif(ch==4):
        del_task=input("enter the task name:")
        delete(del_task)
    elif(ch==5):
        exit()
    else:
        print("invalid choice :( try again")
        func()

func()
