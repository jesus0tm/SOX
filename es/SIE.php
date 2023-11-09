logged=$(who | awk -v IGNORECASE=1 -v usr=$1 '{ if ($1==usr) { print $1 }exit }')

if [ -z $logged ]; then

	echo "$1 is not logged on."

	echo "Exit"

	exit

fi
