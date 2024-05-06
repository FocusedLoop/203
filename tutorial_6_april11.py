def relations_4(R):
    # Set comprehension to extract all first elements (a) from the pairs in R
    first_elements = {a for (a, b) in R}
    
    # Set comprehension to extract all first elements (b) from the pairs in R
    second_elements = {b for (a, b) in R}
    
    # combine the two sets using the union operator to remove duplicates and
    # form the underlying set
    underlying_set = first_elements | second_elements
    
    # Return the underlying set of the relation R
    return underlying_set

R = {(1, 2), (2, 3), (3, 4)}

# Get the underlying set of R
print(relations_4(R))

def relations_5(R):
    
    # Check for all pairs (a, b) in R, whether (b, a) is also in R
    symmetric = all((b, a) in R for (a, b) in R)
    
    seen_pairs = set()
    antisymmetric = True
    
    for (a, b) in R:
        if (b, a) in seen_pairs and a != b:
            antisymmetric = False
            break
        seen_pairs.add((a, b))
        
    # Return a tuple indicating whether the relation is symmetric and antisymmetric
    return symmetric, antisymmetric

R = {(1, 2), (2, 1), (2, 3), (3, 2)}
# R = {(1, 2), (2, 3)}

symmetric, antisymmetric = relations_5(R)

print("symmetric: ", symmetric)
print("antisymmetric: ", antisymmetric)

    
    
def relations_6(R):
    # check all pairs (a, b), (b2, c) in R where b == b2.
    # Verify whether the required (a, c) is also present in R.
    for (a, b) in R:
        for (b2, c) in R:
            if b == b2: # Check if the second element of the first pair equals the first element of the second pair.
                # If the condition holds, check if (a, c) is present in R
                if (a, c) not in R:
                    return False
    
    return True

R = {(1, 2), (2, 3), (1, 3)}
# R = {(1, 2), (2, 3)}

print("Transitive: ", relations_6(R))

def functions_2_numimages(R, a):
    # return the size of the set of all b such that (a, b) in in R.
    # This will be 1 for all a in A if R is a function
    return len({b for (a2, b) in R if a2 == a})
    

def functions_2_isfunction(R, A, B):
    # Check if each element in A appears on the left exactly once
    isF = all(functions_2_numimages(R, a) == 1 for a in A)
    
    # Find the inverse relation
    R2 = {(b, a) for (a, b) in R}


    # Check if the inverse relation is a function
    hasInv = all(functions_2_numimages(R2, b) == 1 for b in B)
    
    return isF, hasInv
          
R = {(0, 1), (1, 2), (2, 0)}

# Define sets A and B
A = {0, 1, 2}
B = {1, 2, 0}

is_function, has_inverse = functions_2_isfunction(R, A, B)

# print the results
print("Is function: ", is_function)
print("Has inverse: ", has_inverse)


#------ Sequences Q2 -----#

# Function to create an empty database
def createD():
    return dict()

# Add a student to the database
def addStudent(D, student):
    number, firstname, lastname = student
    D[number] = (firstname, lastname)
    
# Retrieve the student's first name and last name
# from the database by student number
def studentName(D, number):
    return D[number]
    
# Create an empty database
D = createD()

# Add a student to the database
addStudent(D, (98736788, "John", "Smith"))
addStudent(D, (23987423, "Will", "Smith"))
addStudent(D, (34534567, "Cameron", "Diaz"))
addStudent(D, (15674582, "James", "Cordon"))


student_number = 15674582
first_name, last_name = studentName(D, student_number)
print("Student's name: ", first_name, last_name)









          
          
          
          

