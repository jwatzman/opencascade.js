#!/bin/sh

if [ "$#" -ne 2 ]
then
	echo "Require version tag and yaml file"
	exit 1
fi

exec docker run --rm -it -v "$(pwd):/src" -u "$(id -u):$(id -g)" ocjs:"$1" "$2"
