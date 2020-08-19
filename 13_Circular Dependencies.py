dependencies = {
  "name": "my_cool_software",
  "version": "1.0.0",
  "dependencies": {
    "xmllib": { 
      "version": "0.2.3",
      "name": "xmllib",
      "dependencies" : {
          "parser": {
            "name": "parser",
            "version": "1.2.1"
          },
          
        }
      },
      "parser": {
        "name": "parser",
        "version": "1.4.6"
       }
    }
}

def flatten_dependencies(dependencies):
  flattend_dict = {}
  def check(dictionary, key):
    if key in flattend_dict:
      str1 = key + "@" + flattend_dict[key]
      flattend_dict[str1] = flattend_dict[key]
      str2 = key + "@" + dictionary["version"]
      flattend_dict[str2] = dictionary["version"]
      del  flattend_dict[key]
    else:
      flattend_dict[key] = dictionary["version"]
  for key, values in dependencies["dependencies"].items():
    if "dependencies" in values:
      check(values, key)
      for key, values in values["dependencies"].items():
        check(values, key)
    else:
      check(values, key)
  return flattend_dict
    
print(flatten_dependencies(dependencies))