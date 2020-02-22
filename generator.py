#!/usr/bin/env python

import json
import os
import uuid
from subprocess import Popen, PIPE
from authlib.jose import JsonWebKey, JWK_ALGORITHMS


class KeyGenerator:
    jwks = {}
    jwks_file_name = '/keys/jwks.json'

    def __init__(self, keys_amount=1):
        print('Starting.')
        for i in range(keys_amount):
            try:
                os.mkdir(f'/keys/{i}')
            except FileExistsError:
                pass
            self.create_key_pair(i)
        self._write_jwks()
        print('Finishing.')

    @classmethod
    def _write_jwks(cls):
        with open(cls.jwks_file_name, 'w+') as file:
            print('Writing to jwks.json file...')
            json.dump(cls.jwks, file)

    @classmethod
    def _read_jwks(cls):
        try:
            with open(cls.jwks_file_name, 'r') as file:
                cls.jwks = json.load(file)
                print('Reading from existing file...')
        except FileNotFoundError:
            print('File: jwks.json does not exist.')
            pass

    @classmethod
    def _create_private_key(cls, kid, i):
        command = f'openssl genrsa -out /keys/{i}/priv.pem {os.getenv("RSA_SIZE")}'
        res = Popen(command.split(), stderr=PIPE, stdout=PIPE)
        res.communicate()
        jwk = JsonWebKey(
            algorithms=JWK_ALGORITHMS
        ).dumps(open(f'/keys/{i}/priv.pem').read(), kty='RSA', kid=kid)
        return jwk

    @classmethod
    def _create_public_key(cls, kid, i):
        command = f'openssl rsa -in /keys/{i}/priv.pem -outform PEM -pubout -out /keys/{i}/pub.pem'
        res = Popen(command.split(), stderr=PIPE, stdout=PIPE)
        res.communicate()
        jwk = JsonWebKey(
            algorithms=JWK_ALGORITHMS
        ).dumps(open(f'/keys/{i}/pub.pem').read(), kty='RSA', kid=kid)
        return jwk

    def create_key_pair(self, i):
        kid = str(uuid.uuid4())[:8]
        jwk_private = self._create_private_key(kid, i)
        jwk_public = self._create_public_key(kid, i)
        self.jwks[kid] = {'public': jwk_public, 'private': jwk_private}
        print(f'Creating keys with kid: {kid}')


if __name__ == '__main__':
    handler = KeyGenerator(int(os.getenv('KEY_NUMBER')))
