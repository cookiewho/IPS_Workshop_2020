test_data = [
'[WARNING] 403 Forbidden: No token in request parameters',
'[ERROR] 500 Server Error: int is not subscriptable',
'[INFO] 200 OK: Login Successful',
'[INFO] 200 OK: User sent a message',
'[ERROR] 500 Server Error: int is not subscriptable'
]


def log_stats(logs):
  dict = {}
  newlogs = []
  for log in logs:          #format data to easily sort into dict
    log = log.split(":")
    log[1] = log[1].strip()
    log[0] = log[0].replace("[", "").replace("]", "")
    log[0] = log[0].split(" ", 2)
    log[0].append(log[1])
    log = log[0]
    newlogs.append(log)
  for log in newlogs:
    if log[0] not in dict:
      dict[log[0]] = {}
    if log[1] not in dict[log[0]]:
      dict[log[0]][log[1]] = {}
    if log[2] not in dict[log[0]][log[1]]:
      dict[log[0]][log[1]][log[2]] = {}
    if log[3] not in dict[log[0]][log[1]][log[2]]:
      dict[log[0]][log[1]][log[2]][log[3]] = 1
    else:
      dict[log[0]][log[1]][log[2]][log[3]] += 1
  return dict
print(log_stats(test_data))