import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# pretty much from https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#cbc-mode -> 
creds = {
	"username": "someusername",
	"password": "jyhmeyqH9+IR70yw/LshE"
}

#key = get_random_bytes(32)
key = b'\xcc\xb0\xa5ad\xc59~Od\xde\xcf\x18\xfe\xdd\xf4~\xb2\xa2\x14\x91K\xed\x9b\xfb_\xf6$\xfce9\x89'

json_str = json.dumps(creds)
data = json_str.encode('utf-8')

class Store_in_db():
    data = json.dumps(resp)
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    result = json.dumps({'iv':iv, 'ciphertext':ct})
    #print(result)
# {"iv": "kDbLBbPjWue/nUDLWUZXrg==", "ciphertext": "EitHEbvAvmvcTxnZUuMaq2QUw3BA3DzaYtctvzJNsX0r5vh522YOjuicTVXplHeok6XhMctI/Kd3yyeS0PfAOh9l8ageLxsYgF4jbhP/fpk="}

class Restore_from_db():
    # We assume that the key was securely shared beforehand
    try:
        b64 = json.loads(result)
        iv = b64decode(b64['iv'])
        ct = b64decode(b64['ciphertext'])
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        retr = pt.decode('utf-8')
        print(retr)
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
