#The code will receive times of runners running 100[m], calculate the average and
#the amount of runers under average time

#This function will count how many runners are under the average time
#by checking all the times in the list and checking if it's under the average time
#if it is it will advance an index.
#the function receives the list 'times' and the average time. 
#The function returns the ammount of runers under time
def run_un_avg(times,avg):
    j=0
    for i in range(len(times)):
        if(times[i]<avg):
            j+=1
    return j

#This function will calculate the average time by adding all the times and dividing by
#the amount of runners
#the function receives the list 'times' and the amount of runers and returns the averag time
def my_avg(times,runer):
    avg = 0
    for i in range(runer):
        avg+=times[i]
    avg = (avg/runer)
    return avg

#This function will receive the times of each runer from the user and store it
#in a list the size of the amount of runners
#the function receives the amount of runers and returns the list 'time'
def runner_times(n):
    time = [0]*n
    for i in range(n):
        time[i] = float(input("Enter time: "))
    return time


#this main function will print the average time and the ammount of runners under average
#by calling all the functions above
#The function reveives the amount of runners and returns nothings
def main(runners):
    times = runner_times(runners)
    avg_time = my_avg(times,runners)
    print("Avarge time is: %.3f" %avg_time)
    under =  run_un_avg(times,avg_time)
    print("The number of runners, running below average time is: ", under)
    return 0

main(runners = int(input("Enter number of runners: ")))#Asking for amount of runners and sending it to 'main'