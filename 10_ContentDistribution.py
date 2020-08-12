def distribute_content(cdns, requests):
  image_locataions = []
  for request in requests:
    ip = request["ip"].split(".")[0:2]                                      #get first two nums in ip
    ip = float(ip[0] + "." + ip[1])
    min_distance_index = 0
    val_dist = cdns[min_distance_index].split(".")[0:2]
    for ind in range(len(cdns)):
      if min_distance_index == ind:
        continue
      ip2 = cdns[ind].split(".")[0:2]                                       #get first two nums in ip2
      ip2 = float(ip2[0] + "." + ip2[1])
      if abs(ip - ip2) < abs(ip - float(val_dist[0] + "." + val_dist[1])):  #if distance is less than min_distance
        min_distance_index = ind                                            #set min_distance
        val_dist = cdns[min_distance_index].split(".")[0:2]
    print(ip)
    temp = {"image":request["path"].split(".")[0:1], "server": cdns[min_distance_index]}
    if temp not in image_locataions:
      image_locataions.append(temp)                                         #image_locataion.append the image and ip of min distance
  return image_locataions
  
'''### IF WE WANT ONE SERVER PER IMAGE, DOESNT DEAL WITH OUTLIERS THAT WELL, OTHERWISE WORKS FINE ###'''

content_distribution_network_ips = ["4.2.5.66", "5.8.94.12", "14.9.144.56", "94.94.112.4", "200.8.8.90"]

requests = [
  {
    "path": "image_02309.jpg",
    "ip": "4.4.5.6"
  },
  {
    "path": "image_8899.jpg",
    "ip": "15.9.3.8"
  },
  {
    "path": "image_34095.jpg",
    "ip": "95.14.55.11"
  },
  {
    "path": "image_34095.jpg",
    "ip": "92.11.44.112"
  },
  {
    "path": "image_34095.jpg",
    "ip": "4.2.5.66"
  }
]
print(distribute_content(content_distribution_network_ips, requests))