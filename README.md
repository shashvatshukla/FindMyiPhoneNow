# Find My iPhone Now

## Problem

I keep losing my iPhone at home and need to open icloud.com to use Find My Iphone to find it. 

It would be great to do it in just one click.

## Solution (Current attempt)

Using the Python library [Selenium](http://selenium-python.readthedocs.org/) to simulate clicks and login so that the process is automated.

Look at the page html to find the xpath of the button to be clicked on and tell selenium that. 

As of first commit, this code was never written to be readable, I am sorry.


## Usage

Add your email and password to [config.ini](config.ini).
Run `python findmyiphonenow.py` with Selenium installed.