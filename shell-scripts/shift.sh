# The shift command is mostly used when arguments are unknown. Arguments are processed in a while loop with a condition of (( $# )).

#!/bin/bash
# if [ "$#" == "0" ]
#   then
#     echo pass atleast one parameter.
#     exit 1
# fi
# while 
#   (( $# ))
#    do
#        echo you gave me $1
#        shift
#     done

---------------------------------------------------------------------------------
# The read command allows a user to provide the runtime input.
echo Enter your name :
read name

