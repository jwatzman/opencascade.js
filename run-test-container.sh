#!/bin/sh

set -ex

docker build --target test-image --tag ocjs:tmp .
docker run --rm --name ocjs-tmp --entrypoint /bin/bash -it ocjs:tmp
docker rmi ocjs:tmp
