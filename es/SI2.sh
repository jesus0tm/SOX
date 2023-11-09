check=$(who -T | grep -i -m 1 $1 | awk '{print $2}')

if [ "$check" != "+" ]; then

	echo "$1 disable messaging."

	echo "Exit"

	exit

fi
