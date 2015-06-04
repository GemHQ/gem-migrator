gem-migrator: A small utility for migrating Gem application wallets.

This tool will re-encrypt your [Gem](https://developers.gem.co) Application wallets using an updating encryption scheme (chosen to eliminate the not-very-portable libsodium).

Prerequisites:

1. A *NIX environment (this migration is in part intended to make the [Gem client library](https://github.com/GemHQ/round-py) easy to install on Windows)

2. Python 2.7 or 3.3+

3. Build tools and pip

    $ sudo apt-get install gcc make libffi-dev python-dev python-pip git


Installation:

1. Install coinop from PyPI:

    $ sudo pip install gem-migrator


Usage:

1. Log into the [Gem Developer Console](https://developers.gem.co). You'll need to copy tokens for use in the next step.

2. Run the utility (replacing the uppercase variables with their values from the console)

    $ gem-migrator -a API_TOKEN -d ADMIN_TOKEN -t TOTP_SECRET

3. Enter your passphrase for each wallet when prompted.

4. Uninstall gem-migrator. You will probably never need it again.

    $ sudo pip uninstall gem-migrator
