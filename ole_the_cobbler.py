import threading
from collections import deque
job_queue = deque()

def list_update(job,job_queue):

   arrival_time,job_length = job
   if job_length < 5:
     job_queue.appendleft((arrival_time, job_length))
   else:
     job_queue.append((arrival_time, job_length))
   print(job_queue)

def insert_job(job, job_queue):
    # Find the position in the queue where the new job should be inserted
    for i, existing_job in enumerate(job_queue):
        if existing_job[0] > job[0]:
            list_update(i,job_queue)
            return
    # If the new job should be added at the end of the queue
    job_queue.append(job)

def delay(job_queue):

    for job in job_queue:
        arrival_time, job_length = job
        while time < arrival_time:
            if job_queue:
                start_time, length = job_queue.popleft()
                total_delay += time - start_time
                num_jobs += 1
                time += length
            else:
                time += 1
        if job_queue:
            start_time, length = job_queue.popleft()
            total_delay += time - start_time
            num_jobs += 1
            time += length







from tkinter import *
root = Tk()

root.geometry('1000x800')
root.title('Average Delay Time Calculator')
root.config(bg='light blue')

logopic = PhotoImage(file='pic.png')
logopiclabel = Label(root, image=logopic, bg='light blue')
logopiclabel.pack(padx = 20,pady=20)



def give_job():
    def calculate_delay():

        arrival_time = job_entry.get()
        job_length = job_entry1.get()
        job = (int(arrival_time), int(job_length))
        list_update(job,job_queue)

        info_label.config(text='Your Job is booked!\n please wait for '+ str(total_delay/len(job_queue)) +'mins')
        quit_button = Button(new, text="Quit", command=quit)
        quit_button.pack()
        delay(job_queue)


    def quit():
        new.destroy()





    new = Toplevel()
    new.title('Give Job')
    new.geometry('500x500')
    info_label = Label(new)
    info_label.pack()
    info_label.config(text="Jobs: \nReplacing Heel Tip : 7 mins\nResoling shoes : 30 mins\nReplacing shoe laces: 3 mins\nStretching shoes: 20 mins\nRepairing shoe stitching:10 mins\nAdding protective soles:40 mins\nRepairing shoe straps or buckles: 25 mins\nReplacing zippers: 15 mins\npolishing shoe:4 mins")
    job_label = Label(new, text="Enter Arrival Time ")
    job_entry = Entry(new, width=50)
    job_label.pack()
    job_entry.pack()
    job_label1 = Label(new, text="Enter job length from the above list ")
    job_entry1 = Entry(new, width=50)
    job_label1.pack()
    job_entry1.pack()
    calculate_button = Button(new, text="submit", command=calculate_delay)
    calculate_button.pack()

    info_label = Label(new)
    info_label.pack()



def collect_job():
    def work():
        arrival_time = job_entry.get()
        job_length = job_entry1.get()
        job = (int(arrival_time), int(job_length))
        info_label = Label(new1)
        info_label.pack()
        if job in job_queue:
            info_label.config(text='Your Job is in queue \n please wait for 5 mins')
        else:
            info_label.config(text='Your Job is Done \n Thank You and Please visit again')
        quit_button = Button(new1, text="Quit", command=quit)
        quit_button.pack()
    def quit():
        new1.destroy()



    new1 = Toplevel()
    new1.title('Collect  Job')
    new1.geometry('500x500')
    job_label = Label(new1, text="Enter your registered Arrival Time ")
    job_entry = Entry(new1, width=50)
    job_label.pack()
    job_entry.pack()
    job_label1 = Label(new1, text="Enter registered job length")
    job_entry1 = Entry(new1, width=50)
    job_label1.pack()
    job_entry1.pack()
    calculate_button = Button(new1, text="submit", command=work)
    calculate_button.pack()






calculate_button=Button(root, text="Give Job",height=5,width=30,command = give_job)
calculate_button.pack(side=LEFT,padx=200)

calculate_button1=Button(root, text="Collect Job",height=5,width=30,command = collect_job)
calculate_button1.pack(side=RIGHT,padx=100)

def run_delay(job_queue):
    while True:
        delay(job_queue)

thread = threading.Thread(target=run_delay, args=(job_queue,))
thread.daemon = True
thread.start()



root.mainloop()