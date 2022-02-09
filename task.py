import sys
import os

k = sys.argv

if len(k)<=1 or k[1].lower() == 'help':
    print("Usage :-\n$ ./task add 2 hello world    # Add a new item with priority 2 and text \"hello world\" to the list\n$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order\n$ ./task del INDEX            # Delete the incomplete item with the given index\n$ ./task done INDEX           # Mark the incomplete item with the given index as complete\n$ ./task help                 # Show usage\n$ ./task report               # Statistics")



elif k[1].lower()=='add':
    if len(k)<4:
        print("Error: Missing tasks string. Nothing added!")
    else:
        d = open("task.txt" , "a")

        d.write("{} {}\n".format(k[2],k[3]))
        d.close()
        print("Added task: \"{}\" with priority {}".format(k[3],k[2]))



elif k[1].lower() == 'ls':
    if not os.path.exists('task.txt'):
        print("There are no pending tasks!")
    else:
        x = open("task.txt" , 'r')
        i=1
        for line in sorted(x):
            val = line.split()  # [0 , the, thing, i, need, to, do]
            s = " ".join(val[1:]) # the thing i need to do
            print("{}. {} [{}]".format(i,s,val[0]))
            i+=1
        x.close()

elif k[1].lower()=="del":
    if len(k)<3:
        print("Error: Missing NUMBER for deleting tasks.")
    else:
        with open("task.txt", "r+") as f:
            d = f.readlines()
            n = len(d)
            if int(k[2])<1 or int(k[2])>n:
                print("Error: task with index #{} does not exist. Nothing deleted.".format(int(k[2])))
            else:
                f.seek(0)
                for i in d:
                    if i != int(k[2]):
                        f.write(i)
                f.truncate()
                print("Deleted task #{}".format(k[2]))

elif k[1].lower()=="done":
    if len(k)<3:
        print("Error: Missing NUMBER for marking tasks as done.")
    else:
        c = open("completed.txt" , "a")


        with open("task.txt", "r+") as f:
                d = f.readlines()
                n = len(d)
                if int(k[2])<1 or int(k[2])>n:
                    print("Error: no incomplete item with index #{} exists.".format(str(k[2])))
                else:
                    f.seek(0)
                    w=1
                    for i in sorted(d):
                        print(i)

                        if w != int(k[2]):
                            f.write(i)
                        else:
                            c.write(i)
                        w+=1
                    f.truncate()
                    print("Marked item as done.")

        c.close()

elif k[1].lower()=="report":
    f = open("task.txt","r")
    n = len(f.readlines())
    f.close()
    print("Pending : {}".format(n))
    x = open("task.txt" , 'r')
    i=1
    for line in sorted(x):
        val = line.split()  
        s = " ".join(val[1:]) 
        print("{}. {} [{}]".format(i,s,val[0]))
        i+=1
    x.close()
    
    f = open("Completed.txt","r")
    n = len(f.readlines())
    f.close()
    print("\nCompleted : {}".format(n))
    x = open("Completed.txt" , 'r')
    i=1
    for line in sorted(x):
        val = line.split()  
        s = " ".join(val[1:]) 
        print("{}. {}".format(i,s))
        i+=1
    x.close()
    
    
    