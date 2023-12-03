-- A set is a unique collection of objects in Python. You can denote a set with a pair of curly brackets {}.
    Python will automatically "remove duplicate" items

-- To Create a set
    set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}

-- We can Convert list to set
    album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", \
                   "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
    album_set = set(album_list)             
    album_set    #{'00:42:19', 10.0, 1982,'30-Nov-82', 46.0,65,'Michael Jackson',None,'Pop, Rock, R&B', 'Thriller'}

-- We can do many operationson sets 
  # Sample set
  A = set(["Thriller", "Back in Black", "AC/DC"])
    1) Adding 
        A.add("NSYNC")
        A        #{'AC/DC', 'Back in Black', 'NSYNC', 'Thriller'}

    2) Removing
        A.remove("NSYNC")
        A        #{'AC/DC', 'Back in Black', 'Thriller'}

    3) Verify if the element is in the set
        "AC/DC" in A    #True

-- Sets logic operations
    # Sample Sets
    album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
    album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

  1) To Print two sets use :
      album_set1, album_set2    #({'AC/DC', 'Back in Black', 'Thriller'}, {'AC/DC', 'Back in Black', 'The Dark Side of the Moon'})

  2) Find the intersections
      intersection = album_set1 & album_set2
      intersection         #{'AC/DC', 'Back in Black'}

  3) Find the difference in set1 but not set2
      album_set1.difference(album_set2)      #{'Thriller'}

  4) Find intersection of album_list1 and album_list2
      album_set1.intersection(album_set2)      #{'AC/DC', 'Back in Black'}

  5) Find the union of two sets
      album_set1.union(album_set2)          #{'AC/DC', 'Back in Black', 'The Dark Side of the Moon', 'Thriller'}

  6) 




        
