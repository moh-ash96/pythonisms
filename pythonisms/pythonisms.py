import time

from _pytest.compat import _setup_collect_fakemodule

def calculate_time(any_fun):
  
  def wrapper(*args,**kwargs):
    starting_time = time.time()
    result = any_fun(*args,**kwargs)
    ending_time = time.time()
    print (ending_time-starting_time)
    return result
  return wrapper


def debug_code(any_fun):
  def wrapper(*arg, **kwargs):
    x = arg
    y = kwargs
    print(f'inputs are : {x}, {y}')
    output = any_fun(*arg, **kwargs)
    print(f'output is : {output}')
    return output

  return wrapper

def slowdown(x):
    def wrapper(*arg, **kwargs):
        time.sleep(1)
        output = x(*arg, **kwargs)
        return output
    return wrapper

def convert_to_float(x):
    def wrapper(*args, **kwargs):
        output = x(*args, **kwargs)
        return float(output)
    return wrapper

def validate_conditions(x):
    def wrapper(*args, **kwargs):
        conditions = [
            type(args[0]) == str,
            type(args[1]) == int
        ]
        if all(conditions):
            output = x(*args, **kwargs)
            return output
        else:
            return "passed arguments don't match"
    return wrapper
        

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class Linked_list():
    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, value):
        """inserts a node to the biggining of the linked list

        Args:
            value ([any])
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def __str__(self):

        output = ''

        current = self.head

        while current:
            output += f"{ {current.value} } "
            current = current.next
        output += 'None'

        return output

    def append(self, val):
        """adds a node to the end of the linked list

        Args:
            val ([any])
        """
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node


    
    def __iter__(self):
        """Makes the link list iterable

        Yields:
            [any]: [value of node]
        """
        current= self.head
        while current:
            yield current.value
            current = current.next 
    

    def __eq__(self, other):
        """returns True if the nodes in both lists are qual, and False if one 
        or more are not equal

        Args:
            other ([linked list])

        Returns:
            [boolean]
        """
        current1 = self.head
        current2 = other.head
        flag =True
        while current1 and current2:
            if not (current1.value == current2.value):
                flag = False
                break
            current1 = current1.next
            current2 = current2.next
        return flag


    def __bool__(self):
        """Checks if the linked list is empty or not

        Returns:
            [Boolean]: [if liked list is empty, return False and if it contains nodes, return True]
        """
        if self.head:
            return True
        else:
            return False




ll = Linked_list()
ll.append(10)
ll.append(20)
ll.append(50)
ll.append(7)

ll2 = Linked_list()
ll2.append(10)
ll2.append(20)
ll2.append(50)
ll2.append(7)

# @calculate_time
def check_equality(ll1, ll2):
    return ll1 == ll2

check_equality(ll, ll2)

# @debug_code
def factorial(n):
    if n ==1:
        return 1
    else:
        return n * factorial(n-1)

factorial(6)
y = ll.head


# @slowdown
@convert_to_float
def summation(li):
    if len(li) == 0:
        return 0
    else:
        return li[0] + summation(li[1:])

# @validate_conditions
def calc_age(name, YOB):
    return f'Hello {name} you are {2021 - YOB} years old'

starting_time = time.time()
calc_age('Mohammad', 1996)
ending_time = time.time()
print(int(ending_time - starting_time))

@calculate_time
def return_calc_time(name, age):
    calc_age(name, age)

return_calc_time('Mohammad', 1996)


@debug_code
def add(a, b):
    return a + b

add(3,4)