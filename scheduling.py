class Scheduling_Algos(object):

    def __init__(self):
        self.id = []    #Process id\name list
        self.at = []    #Arrival time list
        self.bt = []    #Finish time list
        self.priority = []  #static priority info
        self.wt = []    #calculated wait time list
        self.tat = []   #calculated turn around time list

    #To read input file and store information in the corresponding list
    def read_file(self):
        with open("input.txt","r") as file:
            data = file.readlines()
            for line in data:
                process_info = line.split()
                k = process_info[0].split(',')
                self.id.append(k[0])
                self.at.append(k[1])
                self.bt.append(k[2])
                self.priority.append(k[3])

    def schedule_via_fcfs(self):
