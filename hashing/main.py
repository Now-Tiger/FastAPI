#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import random
import string
import hashlib
import itertools
from string import ascii_letters, digits, punctuation, hexdigits

__version__ = "0.1.0"


class HashMaster(object):
    def __init__(self, password: str) -> None:
        self._password = password

    def __repr__(self) -> str:
        return f"User password: {self._password}"

    def hash_password(self) -> hexdigits:
        password_bytes = self._password.encode('utf-8')
        hash_object = hashlib.sha256(password_bytes)
        password_hashed = hash_object.hexdigest()
        return password_hashed

    def generate_random_password(self, length: int = 5) -> str:
        all_chars = ascii_letters + digits + punctuation
        password = ''.join(random.choice(all_chars) for i in range(length))
        return password

    def validate_password(self) -> bool:
        if len(self._password) < 5:
            return False
        if not any(a.isupper() for a in self._password):
            return False
        if not any(a.islower() for a in self._password):
            return False
        if not any(a.isdigit() for a in self._password):
            return False
        if not re.search(r'[!@#$%&]', self._password):
            return False
        return True

    def get_password_variants(self) -> str:
        pass_variants = []
        substitutions = {
            'a': ['@', '4', 'A'],
            'e': ['3', 'E',],
            'i': ['1', '!', 'I'],
            'o': ['0', 'O'],
            's': ['$', '5', 'S'],
            't': ['7', 'T'],
            'z': ['2', 'Z'],
        }
        for i in range(len(self._password)):
            if self._password[i] in substitutions:
                for sub in substitutions[self._password[i]]:
                    pass_variant = self._password[:i] + \
                        sub + self._password[i + 1:]
                    pass_variants.append(pass_variant)

        pass_variants.append(self._password + '!')
        pass_variants.append(self._password + '123')
        pass_variants.append(self._password + '@')
        pass_variants.append(self._password + '#')
        pass_variants.append(self._password + '$')
        pass_variants.append(self._password + '%')
        pass_variants.append(self._password + '&')
        pass_variants.append(self._password + '*')
        pass_variants.append(self._password + '-')
        pass_variants.append(self._password + '_')
        pass_variants.append(self._password + '=')
        pass_variants.append(self._password + '+')

        return pass_variants

    def brutforce_attack(self) -> None:
        attempts = 0
        chars = string.printable.strip()
        for length in range(1, len(self._password) + 1):
            for guess in itertools.product(chars, repeat=length):
                attempts += 1
                guess = ''.join(guess)
                if guess == self._password:
                    return (attempts, guess)
        return (attempts, None)


def main() -> None:
    password = str(input('Enter your password: '))
    instance = HashMaster(password)
    hashed_password = instance.hash_password()
    print(f'Your password is: {hashed_password}')
    print('-'*80)
    print('--- Generate random password ---')
    password_length = int(input("Input the desired length of your password: "))
    random_password = instance.generate_random_password(password_length)
    print(f"Generated password: {random_password}")
    is_valid = instance.validate()
    print(is_valid)
    result_variants = instance.get_password_variants()
    attempts, guess = instance.brutforce_attack()
    if guess:
        print(
            f"Password cracked in: {attempts} attempts. The password is {guess}")
    else:
        print(f"Password not cracked after {attempts} attempts")
    # print(result_variants)
    return


if __name__ == '__main__':
    main()
