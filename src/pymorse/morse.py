#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Morse(object):
    """
    支持Unicode的摩斯电码编码解码库
    使用方法：
        from pymorse import Morse
        Morse.encode('你好')
        Morse.decode('--')
    """
    __standard = {
        # Letters
        'A': '01',  # A
        'B': '1000',  # B
        'C': '1010',  # C
        'D': '100',  # D
        'E': '0',  # E
        'F': '0010',  # F
        'G': '110',  # G
        'H': '0000',  # H
        'I': '00',  # I
        'J': '0111',  # J
        'K': '101',  # K
        'L': '0100',  # L
        'M': '11',  # M
        'N': '10',  # N
        'O': '111',  # O
        'P': '0110',  # P
        'Q': '1101',  # Q
        'R': '010',  # R
        'S': '000',  # S
        'T': '1',  # T
        'U': '001',  # U
        'V': '0001',  # V
        'W': '011',  # W
        'X': '1001',  # X
        'Y': '1011',  # Y
        'Z': '1100',  # Z
        # Numbers
        '0': '11111',  # 0
        '1': '01111',  # 1
        '2': '00111',  # 2
        '3': '00011',  # 3
        '4': '00001',  # 4
        '5': '00000',  # 5
        '6': '10000',  # 6
        '7': '11000',  # 7
        '8': '11100',  # 8
        '9': '11110',  # 9
        # Punctuation
        '.': '010101',  # Full stop
        ',': '110011',  # Comma
        '?': '001100',  # Question mark
        '\'': '011110',  # Apostrophe
        '!': '101011',  # Exclamation mark
        '/': '10010',  # Slash
        '(': '10110',  # Left parenthesis
        ')': '101101',  # Right parenthesis
        '&': '01000',  # Ampersand
        ':': '111000',  # Colon
        ';': '101010',  # Semicolon
        '=': '10001',  # Equal sign
        '+': '01010',  # Plus sign
        '-': '100001',  # Hyphen1minus
        '_': '001101',  # Low line
        '"': '010010',  # Quotation mark
        '$': '0001001',  # Dollar sign
        '@': '011010'  # At sign
    }

    # 计算反向词典
    __rstandard = {}
    for key in __standard:
        __rstandard[__standard[key]] = key

    @staticmethod
    def encode(msg, space='/', short='.', long='-'):
        """将字符串编码为摩斯电码"""
        msg = list(''.join(msg.upper().split()))
        trans_msg = [Morse.__standard[ch] if ch in Morse.__standard
                     else bin(ord(ch))[2:] for ch in msg]
        morse = [ch.replace('0', short).replace('1', long) for ch in trans_msg]
        return space.join(morse)

    @staticmethod
    def decode(morse, space='/', short='.', long='-'):
        """将摩斯电码解码为字符串"""
        morse = morse.split(space)
        msg = [code.replace(' ', '').replace(short, '0').replace(long, '1') for code in morse]
        trans_msg = [Morse.__rstandard[ch] if ch in Morse.__rstandard
                     else chr(int(ch, 2)) for ch in msg]
        return ''.join(trans_msg)

