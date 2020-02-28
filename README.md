# jwk-rsa-key-generator
[![Build Status](https://travis-ci.org/HallBregg/jwk-rsa-key-generator.svg?branch=master)](https://travis-ci.org/HallBregg/jwk-rsa-key-generator)

With jwk-rsa-key-generator you can generate rsa private and public keys + jwks.json file.

```sh
$ docker run --rm -v $PWD:/keys hallbregg/jwk-generator
Starting.
Creating keys with kid: d7bb9bfc
Creating keys with kid: 0f95b2e7
Writing to jwks.json file...
Finishing.

$ ls -la $PWD
total 24
drwxr-xr-x  4 root root 4096 lut 22 13:33 .
drwxrwxrwt 19 root root 4096 lut 22 13:33 ..
drwxr-xr-x  2 root root 4096 lut 22 13:33 0
drwxr-xr-x  2 root root 4096 lut 22 13:33 1
-rw-r--r--  1 root root 4174 lut 22 13:33 jwks.json
```

You can also specify two ENVs:
* ENV KEY_NUMBER=2
* ENV RSA_SIZE=2048
