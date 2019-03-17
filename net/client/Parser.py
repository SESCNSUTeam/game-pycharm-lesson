def pars(bytes):
    index = bytes.find(b'\x01e.')
    if index != -1:
        return bytes[:index+3], bytes[index+3:]
    return None, bytes

# b'\x80\x03]q\x00(K\x01K;M0\x0bK K\x00\x87q\x01e.'


# string = b'\x80\x03]q\x00(K\x01K;M0\x0bK K\x00\x87q\x01e.\x80\x03]q\x00(K\x01K;M0\x0bK K\x00\x87q\x01e.'
# packet, string = pars(string)
# print('packet {}'.format(packet))
# print('finally {}'.format(string))
