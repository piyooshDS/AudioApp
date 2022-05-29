""" define encryption python file """
import os
import random
import struct
from Crypto.Cipher import AES
from django.contrib.sites.shortcuts import get_current_site


def encrypt_file(key, in_filename, request, out_filename=None, chunksize=64 * 1024):
    """ Encrypts a file using AES (CBC mode) with the
        given key.

        key:
            The encryption key - a string that must be
            either 16, 24 or 32 bytes long. Longer keys
            are more secure.

        in_filename:
            Name of the input file

        out_filename:
            If None, '<in_filename>.enc' will be used.

        chunksize:
            Sets the size of the chunk which the function
            uses to read and encrypt the file. Larger chunk
            sizes can be faster for some files and machines.
            chunksize must be divisible by 16.
    """
    if not out_filename:
        out_filename = in_filename.path + '.enc'
    four = ''.join(chr(random.randint(65, 91)) for i in range(16)).encode()
    encryptor = AES.new(key[:16], AES.MODE_CBC, four)
    filesize = os.path.getsize(in_filename.path)

    with open(in_filename.path, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(four)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))
                return get_current_site(request).name + "/" + in_filename.name + '.enc'
