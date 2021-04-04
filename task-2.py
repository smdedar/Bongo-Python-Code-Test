class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father
    
    def test(self):
        value = {
            "first_name":self.first_name,
            "last_name":self.last_name,
            "father":self.father
        }
        return value

    


if __name__ == "__main__":
    person_a = Person("User", "1", None)
    person_b = Person("User", "2", person_a.test())

    print(person_b.test())

    a = {
        "key1": 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": 4,
                "user": person_b.test(),
            }
        },
    }

    def print_depth(data,count = 0):
        for key, value in data.items():
            print(key, count+1)
            if isinstance(value, dict):
                print_depth(value,count+1)

    print_depth(a)