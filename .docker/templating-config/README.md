# Generate configuration from templates files

## Test



```
docker build -t genconf .
docker run --rm -v ./configs:/app/configs/ -v /var/run/docker.sock:/var/run/docker.sock -it genconf /bin/bash
```
