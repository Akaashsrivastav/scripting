# Example 1 without argument:

#!/bin/bash
while getopts ":abc" option;
do
 case $option in
 a)
  echo recieved -a
  ;;
 b)
  echo recieved -b
  ;;
 c)
  echo recieved -c
  ;;
  *)
   echo "envalid option $OPTARG"
   ;;
 esac
done 
  

# Example 2 with argument:
while getopts ":ab:c" option;
do
 case $option in
 a)
  echo recieved -a
  ;;
 b)
  echo recieved -b with $OPTARG
  ;;
 c)
  echo recieved -c
  ;;
  *)
   echo "envalid option $OPTARG"
   ;;
 esac
done 