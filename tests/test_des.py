from algorithm import des


def test_des_clear_text2binary():
    clear_text_en = 'hello'
    clear_text_han = '你好'
    en_result = des.clear_text2binary(clear_text_en)
    han_result = des.clear_text2binary(clear_text_han)
    assert en_result == list('0110100001100101011011000110110001101111')
    assert han_result == list('100111101100000101100101111101')


def test_binary2text():
    binary_ex = list('0110100001100101011011000110110001101111001011000111001101100010')
    assert 'hello,sb' == des.binary2text(binary_ex)


def test_des_ip_key_replace():
    bin_res = des.clear_text2binary('hello,sb')
    key_bin = des.clear_text2binary('12345678')
    text_result = des.ip_key_replace(bin_res, des.IP_table)
    key_result = des.ip_key_replace(key_bin, des.compress_table1)
    assert text_result == list('1101111101000000001111100101001000000000111111110011110111010000')
    assert key_result == list('00000000000000001111111111110110011001111000100000001111')


def test_des_generate_subkey():
    minkey = des.generate_subkey('12345678')
    assert minkey[0] == list('010100000010110010101100010101110010101011000010')


def test_des_encrypt():
    assert 'qÐ]DYGs°' == des.des_algorithm('qwertyui', '12345678', 'encrypt')


def test_des():
    assert 'qÐ]DYGs°8ý/rsÜ' == des.des('qwertyui12345', '12345678', 'encrypt')
    assert 'qwertyui12345   ' == des.des('qÐ]DYGs°8ý/rsÜ', '12345678', '')
