#!/bin/sh

if [ "$#" -ne 1 ]
then
	echo "Require version tag"
	exit 1
fi

exec docker build --target custom-build-image --tag ocjs:"$1" .
