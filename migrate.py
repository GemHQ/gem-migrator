#! /usr/bin/env python

from round import client
from gem_migrator.nacl_passphrasebox import NaclPassphraseBox
from coinop.passphrasebox import PassphraseBox
from sys import argv
from argparse import ArgumentParser
from getpass import getpass


parser = ArgumentParser(
    description=("A simple utility for migrating Gem application wallets. You "
                 "can find the required parameters in the Gem web console at: "
                 "https://developers.gem.co"))
parser.add_argument('api_token', help="Your api_token")
parser.add_argument('admin_token', help="Your admin_token")
parser.add_argument('totp_secret', help="Your totp_secret")

if __name__ == '__main__':
    args = parser.parse_args()

    cli = client()

    app = cli.authenticate_application(api_token=args.api_token,
                                       admin_token=args.admin_token)
    app.set_totp(args.totp_secret)

    for w in app.wallets:
        if w.primary_private_seed['iv']:
            continue
        print("Enter your passphrase for {}: ".format(w.name))
        try:
            passphrase = getpass()
            seed = NaclPassphraseBox.decrypt(passphrase, w.primary_private_seed)
            encrypted_seed = PassphraseBox.encrypt(passphrase, seed)
            w.with_mfa(app.get_mfa()).update(
                {'name': w.name,
                 'primary_private_seed': encrypted_seed})
            print("{} updated successfully!".format(w.name))
        except Exception as e:
            print(e.message)
            print("Looks like something went wrong. Check your passphrase and "
                  "try running this utility again.")
            break

    print "Done!"
