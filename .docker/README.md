# Build Docker images

Here are definitions to build Docker images.

Images are published to dockerhub organization named Oclock : https://hub.docker.com/?namespace=oclock

## Contribute

To build or update new Docker image you should work with the bran run/docker-build

Here is the procedure :

```
git fetch origin
git checkout run/docker-build
git merge origin/main
```

Do what you need, then

```
git commit -a -m '<your conventional commit message>'
git push
```

Now image will be rebuilded (see `.github/workflows/*-image.generate`).

New image need to create a new workflow.




