a = {"key1": 1,
     "key2": {"key3": 1, "key4": {"key5": 4
                                  }
              }
     }


def print_depth(data,count = 0):
    for key, value in data.items():
        print(key, count+1)
        if isinstance(value, dict):
            print_depth(value,count+1)
        
print_depth(a)