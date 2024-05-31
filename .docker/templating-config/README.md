# Generate configuration from templates files

## Test



```
docker build -t genconf .
docker run --rm -v ./config:/app/config/ -v /var/run/docker.sock:/var/run/docker.sock -it genconf /bin/bash
```
