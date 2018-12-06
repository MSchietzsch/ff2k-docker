import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# pretty much from https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#cbc-mode -> 
creds = {
	"username": "Deadwoodpecker",
	"password": "jyhmeyqH9+IR70yw/LshE"
}
data = b"jyhmeyqH9+IR70yw/LshE"

class Store_in_db():
    data = json.dumps(creds)
    key = get_random_bytes(32)
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    result = json.dumps({'iv':iv, 'ciphertext':ct})
    #print(result)
    #'{"iv": "bWRHdzkzVDFJbWNBY0EwSmQ1UXFuQT09", "ciphertext": "VDdxQVo3TFFCbXIzcGpYa1lJbFFZQT09"}'

key = b'G+5J#o\xc0\xf6\x8a!\xa5i\xe2>j.fb\xd2\xe5\xdf\xf5\xc7\x96\xb0\x8e7\xf9H7:\xfb'

class Restore_from_db():
    # We assume that the key was securely shared beforehand
    try:
        b64 = json.loads(result)
        iv = b64decode(b64['iv'])
        ct = b64decode(b64['ciphertext'])
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        print("The message was: ", pt)
    except ValueError, KeyError:
        print("Incorrect decryption")


"""
>>> # This will run on the 'default' database.
>>> Author.objects.all()

>>> # So will this.
>>> Author.objects.using('default').all()

>>> # This will run on the 'other' database.
>>> Author.objects.using('other').all()


>>> my_object.save(using='legacy_users')


"""
