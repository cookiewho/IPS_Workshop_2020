def server_time_check(task_config, task_times):
  conf = [int(y) for y in task_config.split()]
  tasks = [int(x) for x in task_times.split()]
  tot = 0
  count = 0
  for z in tasks:
    if tot + z <= conf[1]:
      tot+=z
      count+=1
    else:
      print(count)
      return count


## Please do not change the code below this line
## These lines are how the tests interact with the code

task_config = input("Please input the number of tasks, and the maximum total execution time:")
task_times = input("Please input the execution times of each task, seperated with a space:")

server_time_check(task_config, task_times)
