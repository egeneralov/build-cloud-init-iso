# Build cloud init iso

On mac os you can't use genisoimage, and hdutils have troubles with iso creation. So:

## Build:

    docker build . --tag egeneralov/build-cloud-init-iso

## Run:

    docker run -d -p 8080:8080 egeneralov/build-cloud-init-iso

## Use:

    curl -F meta-data=@meta-data -F user-data=@user-data http://127.0.0.1:8080/ > seed.iso
