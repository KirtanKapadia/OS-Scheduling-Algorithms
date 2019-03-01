import statistics

class Scheduling_Algos(object):

    def __init__(self):
        self.id = []    #Process id\name list
        self.at = []    #Arrival time list
        self.bt = []    #Finish time list
        self.priority = []  #static priority info
        self.wt = []    #calculated wait time list
        self.tat = []   #calculated turn around time list
        self.completion_time = [] #completion_time of each process

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
        with open("FCFS.txt","w") as file:
            for i in range(4):

                if i == 0:
                    self.completion_time.append(self.bt[i])
                    self.wt.append("0")
                    self.tat.append(self.bt[i])
                    string = "{},{},{},{}".format(self.id[i],self.wt[i],self.completion_time[i],self.tat[i])
                    file.write(string)
                else:
                    self.completion_time.append(str(int(self.bt[i-1])+int(self.bt[i])))
                    x = str(int(self.completion_time[i]) - int(self.at[i]))
                    self.tat.append(x)
                    y = str(int(self.tat[i]) - int(self.bt[i]))
                    self.wt.append(y)
                    string = "{},{},{},{}".format(self.id[i],self.wt[i],self.completion_time[i],self.tat[i])
                    file.write(string)

            w = [int(x) for x in self.wt]
            avg = statistics.mean(w)
            file.write("mean WT:{}".format(str(avg)))
            w = [int(x) for x in self.tat]
            avg = statistics.mean(w)
            file.write("mean TAT:{}".format(str(avg)))
