# trumpbeep
Sound an alarm when new tweets come in from a list of users. For Mac only.

## Setup
1. Open a terminal and make sure you have python and pip installed on your mac by running `sudo easy_install python` and `sudo easy_install pip`.
2. Navigate to your home directory with `cd`, then clone the repo with `git clone https://github.com/wcox13/trumpbeep.git`.
3. Navigate to the repo with `cd trumpbeep`, then install the dependencies with `pip install -r requirements.txt`.

## Usage
From the `trumpbeep` directory, simply run `python main.py` followed by a space separated list of one or more usernames you'd like to follow. For example, `python main.py foxnews realdonaldtrump` would follow Fox News and Donald Trump.
