# Build cloud init iso

On mac os you can't use genisoimage, and hdutils have troubles with iso creation. So:

## Use online version:

### Payload as file:

    curl -s -F meta-data=@meta-data -F user-data=@user-data https://build-cloud-init-iso.herokuapp.com/ > seed.iso

### Payload as form-data:

    curl -F user-data="$(cat user-data)" -F meta-data="$(cat meta-data)" https://build-cloud-init-iso.herokuapp.com/ > seed.iso

## Self-hosted solution

### Build:

    docker build . --tag egeneralov/build-cloud-init-iso

### Run:

    docker run -d -p 8080:8080 egeneralov/build-cloud-init-iso

### Use:

    curl -F meta-data=@meta-data -F user-data=@user-data http://127.0.0.1:8080/ > seed.iso

## source code

https://github.com.egeneralov/build-cloud-init-iso
