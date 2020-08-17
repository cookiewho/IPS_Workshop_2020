class FileDescriptor:
  def __init__(self, filename, contents=None, isFolder=False):
    self.filename = filename
    self.parent = None
    self.isFolder = isFolder
    if self.isFolder:
      self.fileDescriptors = []
    else:
      self.contents = contents
    
  def add_file(self,filename,contents):
    if self.isFolder:
      new_file = FileDescriptor(filename,contents,False)
      self.fileDescriptors.append(new_file)
      new_file.parent = self
      return new_file
    
  def add_folder(self,foldername):
    if self.isFolder:
      new_folder = FileDescriptor(foldername,None,True)
      self.fileDescriptors.append(new_folder)
      new_folder.parent = self
      return new_folder
      
  
  def output_file_path(self):
    # Implement this method:
    # when called on a file or folder, print out a directory path from the root node:
    # eg /Documents/Pictures
    path = []
    path2 = ""
    def get_to_root(self):
      if self.parent == None:
        return
      else:
        path.append(self.filename)
        get_to_root(self.parent)
    get_to_root(self)
    for directory in path[::-1]:
      path2 += "/" + directory
    return path2
    
  
  def find(self, path):
    # Implement this method:
    # Path will be a file path, like /Documents/Pictures/img.jpg
    # Output the contents of the file if it is a file,
    # Output all the file names contained within if it is a folder
    path = path[1:].split("/")
    def finding(curr):
      if len(path) > 0:
        for file in curr.fileDescriptors:
          if file.filename == path[0]:
            curr = file
            path.pop(0)
            finding(curr)
            break
          else:
            continue
      else:
        cont = ""
        if curr.isFolder:
          for file in curr.fileDescriptors:
            cont += file.filename + " "
        else:
          cont += curr.contents
        path.append(cont)
        return
    finding(self)
    return path[0]
    
  def search(self, filename):
    # Implement this method:
    # filename will be a name like "img.jpg"
    # Output all directories under the directory this was called on containing a file with the given filename
    directorypath = []
    def finding(curr):
      if curr.filename == filename:
        directorypath.append(filename)
        return True
      elif curr.isFolder:
        # path.append()
        for file in curr.fileDescriptors:
          if finding(file):
            directorypath.append(curr.filename)
            return True
      else:
        return
    finding(self)
    string = ""
    for x in directorypath[::-1]:
       if x:
         string += "/" + x
    return string
  
  def grep(self, search_string):
    # Implement this method:
    # search_string will be a string of text
    # When called on a folder, output all complete file paths that have the search string within their contents
    path = []
    def recur(curr):
      if curr.isFolder == False:
        string = "file = "
        for x in range(len(curr.contents)-len(search_string)):
          if curr.contents[x:x+len(search_string)] == search_string:
            print("we did it")
            print("".join(path)+ "/"+curr.filename)
      else:
        path.append("/" + curr.filename)
        for file in curr.fileDescriptors:
          recur(file)
        path.pop(-1)
    recur(self)
    return
    """
    ### ITERATIVE APPROACH ###
    DOESN'T WORK BECAUSE WE ADD THE LEFT AND RIGHT TO THE STACK AT THE SAME TIME
    WHEN WE NEED TO GO THROUGH THEM SEPERATELY:
    # curr = self
    # stack = [curr]
    # while len(stack) > 0:
    #   if curr.isFolder:
        
    #     for file in curr.fileDescriptors:
    #       stack.append(file)
    #     # string = "folder = "
    #     # for x in stack:
    #     #   string += "/" + x.filename
    #     # print(string)
    #     curr = stack.pop(-1)
    #   else:
    #     string = "file = "
    #     for x in range(len(curr.contents)-len(search_string)):
    #       if file.contents[x:x+len(search_string)] == search_string:
    #         for x in stack:
    #           string += "/" + x.filename
    #         print (string)
    #     curr = stack.pop(-1)
    """
    
  
root = FileDescriptor("",None,True)
docs = root.add_folder("Documents")
root.add_folder("System")
root.add_folder("bin")

pix = root.fileDescriptors[0].add_folder("Pictures")
musix = root.fileDescriptors[0].add_folder("Music")
src = root.fileDescriptors[0].add_folder("source")

img1 = pix.add_file("img.jpg", "contents are cool")
img2 = pix.add_file("img.png", "pretend these are images")
musix.add_file("song.mp3", "this is a song, for reals")
musix.add_file("another_song.ogg", "it's an ogg vorbis, remember these")
musix.add_file("ima_deejay.ogg", "it's deejay time")
project_1 = src.add_folder("Project_1")
project_1.add_file("main.py", "print('this is python')")
img_path = img1.output_file_path()
print(img_path)
print(root.find(img_path))
project_1_path = project_1.output_file_path()
print(project_1_path)
print(root.find(project_1_path))
print(docs.search("img.png"))
print(root.search("song.mp3"))
print()
print(docs.grep("on"))