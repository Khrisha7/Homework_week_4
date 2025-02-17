
names_tuple = 'Red', 'Jane', 'Freddy'

# This is an error handling technique which is used to indicate the success/failure of manipulation
# Try block of code is what we are aiming to test
try:
    print('######## TRY ########')
    print("The TRY block attempts to run")
# prints our original tuple
    print(f"Original Tuple: {names_tuple}")
# uses the sort function and returns a list of the tuple
    name_sorted_as_list = sorted(names_tuple)
    print(name_sorted_as_list)
# As our tuple is now a list, we use the method append to add an extra item to the list
    name_sorted_as_list.append("Bungle")
    print("Added Bungle:", name_sorted_as_list)
    print("Attempt to manipulate the tuple...")
# As tuple are immutable, meaning we can not change its element, this will flag as error
    names_tuple[0] = 'Zippy'
# Error handling - should any of the code raise an exception
# We have specified an exception list
# Raised when a file is not found
except FileNotFoundError as error:
    print('######## EXCEPT: FileNotFoundError ########')
    print("The EXCEPT / CATCH block only runs if this error happens")
    print(f"The following file can not be found: {error.filename}. Please try another file")
# Raised when two different types are combined in the case of line 17
except TypeError as error:
    print('######## EXCEPT: TypeError ########')
    # As the code on line 17 will flag up as a type error
    print("oh dear, that is not allowed on that type")
    print(error)
except Exception as error:
    print('######## EXCEPT: EXCEPTION ########')
    print("Generic catch-all expect / catch block")
    print(error)
# this is always executed
finally:
    #Always close file handle after use
    print('The FINALLY block ALWAYS runs')
    print("The Finally block is used to tidy up")
    if names_tuple:
        names_tuple = None

print("After exception handling is finished... the program can continue")

