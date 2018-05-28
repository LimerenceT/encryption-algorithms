# IP置换表
IP_table = [58, 50, 42, 34, 26, 18, 10, 2,
            60, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6,
            64, 56, 48, 40, 32, 24, 16, 8,
            57, 49, 41, 33, 25, 17, 9, 1,
            59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5,
            63, 55, 47, 39, 31, 23, 15, 7
            ]
# 逆IP置换表
IP_table_ = [40, 8, 48, 16, 56, 24, 64, 32,
             39, 7, 47, 15, 55, 23, 63, 31,
             38, 6, 46, 14, 54, 22, 62, 30,
             37, 5, 45, 13, 53, 21, 61, 29,
             36, 4, 44, 12, 52, 20, 60, 28,
             35, 3, 43, 11, 51, 19, 59, 27,
             34, 2, 42, 10, 50, 18, 58, 26,
             33, 1, 41, 9, 49, 17, 57, 25
             ]
# S盒中的S1盒
S1 = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
      0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
      4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
      15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13
      ]
# S盒中的S2盒
S2 = [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
      3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
      0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
      13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9
      ]
# S盒中的S3盒
S3 = [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
      13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
      13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
      1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12
      ]
# S盒中的S4盒
S4 = [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
      13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
      10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
      3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14
      ]
# S盒中的S5盒
S5 = [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
      14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
      4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
      11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3
      ]
# S盒中的S6盒
S6 = [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
      10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
      9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
      4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13
      ]
# S盒中的S7盒
S7 = [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
      13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
      1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
      6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12
      ]
# S盒中的S8盒
S8 = [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
      1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
      7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
      2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11
      ]
# S盒
S = [S1, S2, S3, S4, S5, S6, S7, S8]

# P盒
P_table = [16, 7, 20, 21,
           29, 12, 28, 17,
           1, 15, 23, 26,
           5, 18, 31, 10,
           2, 8, 24, 14,
           32, 27, 3, 9,
           19, 13, 30, 6,
           22, 11, 4, 25
           ]
# 压缩置换表1，不考虑每字节的第8位，将64位密钥减至56位。然后进行一次密钥置换。
compress_table1 = [57, 49, 41, 33, 25, 17, 9,
                   1, 58, 50, 42, 34, 26, 18,
                   10, 2, 59, 51, 43, 35, 27,
                   19, 11, 3, 60, 52, 44, 36,
                   63, 55, 47, 39, 31, 23, 15,
                   7, 62, 54, 46, 38, 30, 22,
                   14, 6, 61, 53, 45, 37, 29,
                   21, 13, 5, 28, 20, 12, 4
                   ]

# 压缩置换表2，用于将循环左移和右移后的56bit密钥压缩为48bit
compress_table2 = [14, 17, 11, 24, 1, 5,
                   3, 28, 15, 6, 21, 10,
                   23, 19, 12, 4, 26, 8,
                   16, 7, 27, 20, 13, 2,
                   41, 52, 31, 37, 47, 55,
                   30, 40, 51, 45, 33, 48,
                   44, 49, 39, 56, 34, 53,
                   46, 42, 50, 36, 29, 32
                   ]

# 用于对数据进行扩展置换，将32bit数据扩展为48bit
extend_table = [32, 1, 2, 3, 4, 5,
                4, 5, 6, 7, 8, 9,
                8, 9, 10, 11, 12, 13,
                12, 13, 14, 15, 16, 17,
                16, 17, 18, 19, 20, 21,
                20, 21, 22, 23, 24, 25,
                24, 25, 26, 27, 28, 29,
                28, 29, 30, 31, 32, 1
                ]


def clear_text2binary(clear_text) -> list:
    """明文转2进制"""
    bin_result = []
    for c in clear_text:
        res_bin = format((ord(c)), 'b').rjust(8, '0')
        bin_result.append(res_bin)
    return list(''.join(bin_result))


def binary2text(binary_list: list) -> str:
    """二进制转明文"""
    encrypt_result = []
    for i in range(8):
        byte = slice(8*i, 8*(i+1))
        c = chr(int(''.join(binary_list[byte]), 2))
        encrypt_result.append(c)
    return ''.join(encrypt_result)


def ip_key_replace(bin_text: list, table: list) -> list:
    """二进制数组根据table置换、压缩置换、扩展置换."""
    return [bin_text[num - 1] for num in table]


def generate_subkey(key: str) -> list:
    """根据密钥生成16个子密钥数组，返回一个数组包含16个子密钥数组"""
    move_step = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    key = ip_key_replace(clear_text2binary(key), compress_table1)
    sub_keys = []
    for step in move_step:
        left_key, right_key = key[:28], key[28:]
        left_key = left_key[step:] + left_key[:step]
        right_key = right_key[step:] + right_key[:step]
        key = left_key + right_key
        sub_keys.append(ip_key_replace(key, compress_table2))
    return sub_keys


def des_algorithm(text, key, en_or_de):
    # 生成sub_keys
    key_list = generate_subkey(key)
    key_list if en_or_de is 'encrypt' else key_list.reverse()
    # ip置换
    binary_result = clear_text2binary(text)
    replace_result = ip_key_replace(binary_result, IP_table)
    result = replace_result
    # 进行16轮的循环操作
    for subkey in key_list:
        left_32, right_32 = result[:32], result[32:]
        right_48_extend = ip_key_replace(right_32, extend_table)
        xor_result = (bin(int(''.join(right_48_extend), 2) ^ int(''.join(subkey), 2))[2:]).rjust(48, '0')
        s_box_result = []
        # s盒代替
        for j in range(8):
            bit_6 = slice(j*6, (j+1)*6)
            s_box_in_6 = str(xor_result)[bit_6]
            row, col = int(s_box_in_6[0]+s_box_in_6[-1], 2), int(s_box_in_6[1:-1], 2)
            index = row * 16 + col
            s_box_out_4 = format(S[j][index], 'b').rjust(4, '0')
            s_box_result.append(s_box_out_4)
        # p盒置换
        p_box_out = ip_key_replace(list(''.join(s_box_result)), P_table)
        xor_ = format(int(''.join(p_box_out), 2) ^ int(''.join(left_32), 2), 'b').rjust(32, '0')
        left_32, right_32 = right_32, xor_
        result = left_32 + list(right_32)

    result = result[32:]+result[:32]
    # ip末置换
    result_replace = ip_key_replace(result, IP_table_)
    return binary2text(result_replace)


def des(text, key, en_or_de):
    length = len(text) % 8
    if not length:
        pass
    else:
        text = text + (8-length)*' '
    result = []
    for i in range(len(text)//8):
        byte = slice(i*8, (i+1)*8)
        i_res = des_algorithm(text[byte], key, en_or_de)
        result.append(i_res)
    return ''.join(result)
