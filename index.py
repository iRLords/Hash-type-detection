try:
    hash_ = str(bin(int(input('Enter the hash : '),16))).replace('0b','')
except:
    exit('error : enter a valid hash value')

def Hash_type_detection(value):
    text = 'I guess the hash type is one of these : '
    try:
        return {2:text+'[CRC-16]',4:text+'[joaat | CRC32 | adler32 | crc32b | fnv132 | fnv1a32]','4L':text+'[adler32]',8:text+'[fnv164 | fnv1a64]',16:text+'[MD5 | MD2 | MD4 | ripemd128 | tiger128,3 | tiger128,4 | haval128,3 | haval128,4 | haval128,5]',20:text+'[SHA-1 | ripemd160 | tiger160,3 | tiger160,4 | haval160,3 | haval160,4 | haval160,5]',24:text+'[tiger192,3 | tiger192,4 | haval192,3 | haval192,4 | haval192,5]',28:text+'[Keccak-224 | SHA3-224 | SHA512/224 | SHA224 | haval224,3 | haval224,4 | haval224,5]',32:text+'[gost-crypto | Shake-128 | Keccak-256 | SHA3-256 | SHA512/256 | SHA256 | ripemd256 | snefru | snefru256 | gost | haval256,3 | haval256,4 | haval256,5]',48:text+'[Keccak-384 | SHA3-384 | SHA384 | ripemd320]',64:text+'[Shake-256 | Keccak-512 | SHA3-512 | SHA512 | whirlpool]'}['4L' if value < 4 else value]
    except KeyError:
        return 'unknown hash'

print(Hash_type_detection(len([hash_[x:x+8] for x in range(0,len(hash_),8)])))