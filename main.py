#############################################################################################
# Creating a function which will sort an array of elements which could be an array also
#
def sort_array_integers(in_array):

    print("Input Data is ", in_array)
    out_array = []

    # Page through array elements
    for element in in_array:

        # Page through any nested array
        if type(element) == list:
           for i in element:            # If it is an array, append each item in array
                out_array.append(i)
        else:
            out_array.append(element)

    return sorted(out_array)            # Sort and return the flattened array


print("Sorted, flattened arrays: ",sort_array_integers([45,2,[4,9],1, 34, 8]))

'''
Q&A:

How does this solution ensure data immutability?
ANSWER:  No inputs or global data is changed.  

Is this solution a pure function? Why or why not?
ANSWER:  Yes, it takes the input (array) and returns a var (array sorted)

Is this solution a higher order function? Why or why not?
ANSWER:  No, there is no function passing (as arguments)

Would it have been easier to solve this problem using a different programming style?
ANSWER:  No, it is suited for functional program.  No object/class needs to be created

Why in particular is functional programming a helpful paradigm when solving this problem?
ANSWER:  OOP is unnecessary to solve this problem.  
'''
#############################################################################################
# OOP ASSIGNMENT
#
#

class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed  = max_speed
        self.condition  = condition
        self.price      = price

    def repair(self):
        self.condition = "repaired"

    def show_values(self):
        print("Max Speed =", self.max_speed, " Condition =", self.condition, " Price =", self.price)

class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def boost(self):
        self.max_speed *= 2

class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def flame_jet(self):
        self.condition = "thrashed"

print("")
print("======================= OOP RESULTS ==============================")
pod = Podracer(50, "Awesome", 1000)
pod.show_values()
pod.repair()
pod.show_values()

print("")
new_pod = AnakinsPod(2, "Great", 5000)
new_pod.show_values()
new_pod.boost()
new_pod.show_values()

print("")
third_pod = SebulbasPod(100, "Bad", 5)
third_pod.show_values()
third_pod.flame_jet()
third_pod.show_values()

'''
Q&A:
How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
    - Encapsulation - It provides an external interface perform actions on the object
    - Abstraction - It contains internal data/characteristics not accessible to the outside
    - Inheritance - classes AnakinsPod and SebulbasPod are derivations of the parent Podracer class
    - Polymorphism - does not exist in this model as no methods are overwritten
Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
    No, because there is code reusability for each of the derived child classes/objects
How in particular did Object Oriented Programming assist in the solving of this problem?
    It objectifies the solution making the design easier to understand by formating it in an object-style
    It provides code reusability and makes it easy to add additional derivation of the parent class
'''