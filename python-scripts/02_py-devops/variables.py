# Assigning a value to a variable
my_variable = 42

# Accessing the value of a variable
print(my_variable)  # Output: 42


# Local Variable
def my_function():
       x = 10  # Local variable
       print(x)
   
my_function()
print(x)  # This will raise an error since 'x' is not defined outside the function.


# Globle Variable
y = 20  # Global variable

def another_function():
    print(y)  # This will access the global variable 'y'

another_function()
print(y)  # This will print 20


# Define configuration variables for a web server
server_name = "my_server"
port = 80
is_https_enabled = True
max_connections = 1000

# Print the configuration
print(f"Server Name: {server_name}")
print(f"Port: {port}")
print(f"HTTPS Enabled: {is_https_enabled}")
print(f"Max Connections: {max_connections}")

# Update configuration values
port = 443
is_https_enabled = False

# Print the updated configuration
print(f"Updated Port: {port}")
print(f"Updated HTTPS Enabled: {is_https_enabled}")