# animal crossing new horizons turnip prices api

this is a small api that aims to complement my fork of of the repo [mikebryant/ac-nh-turnip-prices](https://github.com/mikebryant/ac-nh-turnip-prices) so that user data can be stored, retrieved, and updated to allow for easier turnip collaboration.

## requirements
- python 3 (i use 3.7.1 cause it's what i have installed lmao)
  - flask
  - flask restful
- some sorta db in the future (i'm thinking mariadb since that's what i know but idk)

## usage

run `pip install -r requirements.txt` to install any required packages and then just run the main script with `python main.py`. for documentation on api usage please refer to the [api reference](APIReference.md) note that while this is still in testing stages i'll have it in debug mode. if you plan on deploying this, please take it out of debug mode.
