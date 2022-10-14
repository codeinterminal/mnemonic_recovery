import os
import sys

from common import find_address

def next_password_fn(try_paswords, passwords):
    if try_passwords == False:
        def pwdfn():
            yield ''
            return
        return pwdfn
    if passwords is not None:
        def pwdfn():
            for pwd in passwords:
                yield pwd.strip()
        return pwdfn
    def pwdfn():
        try:
            while True:
                pwd = input("Introduce password: ")
                pwd = pwd.strip()
                yield pwd
        except KeyboardInterrupt:
            return
    return pwdfn

if __name__ == "__main__":
    usage = """
    Try to find the target address from pass phrase file.

    usage:
        python cmd.py [mnemonic_file] [target_address] [-i|passwords_file]

    The mnemonic_file and target_address are required parameters.

    The -i option is used to be asked for a passwords interactively. Otherwise
    a password file can be provided.
    """

    if len(sys.argv) < 3:
        print(usage)
        exit(-1)

    mnemonic_file = sys.argv[1].strip()
    target_address = sys.argv[2].strip()
    print(f"PASS PHRASE FILE: {mnemonic_file}")
    print(f"TARGET ADDR: {target_address}")

    try_passwords = False
    passwords = None
    if len(sys.argv) > 3:
        try_passwords = True
        if sys.argv[3].strip() != "-i":
            passwords_file = sys.argv[3].strip()
            try:
                with open(passwords_file, 'r') as f:
                    passwords = ' '.join(f.read().split('\n')).rstrip().lstrip()
            except FileNotFoundError:
                print(f"cannot open passwords file: {passwords_file}")
                exit(-1)

    pwdfn = next_password_fn(try_passwords, passwords)

    mnemonic = ""
    try:
        with open(mnemonic_file, 'r') as f:
            mnemonic = ' '.join(f.read().split('\n')).rstrip().lstrip()
    except FileNotFoundError:
        print(f"cannot open phrase file: {mnemonic_file}")
        exit(-2)

    num_addresses = 5
    derivation_paths = [
        "m/44'/60'/0'/0/{acc_idx}",
        "m/44'/60'/0'/{acc_idx}",
        "m/44'/60'/{acc_idx}'/0",
        "m/44'/60'/{acc_idx}",
    ]

    for pwd in pwdfn():
        for der_path in derivation_paths:
            for acc_idx in range(num_addresses):
                dp = der_path.format(acc_idx=acc_idx)
                addr, info = find_address(mnemonic, target_address, pwd, dp)
                if addr is not None:
                    print(f"-> addr: {addr} - der_path: {dp}")
                if addr.lower().startswith(target_address.lower()):
                    print("****************************************")
                    print("FOUND MATCH")
                    print(f"-> addr: {addr} - der_path: {dp}")
                    print("****************************************")
                    exit(0)
