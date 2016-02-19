# Find My iPhone Now

## Problem

I keep losing my iPhone at home and need to open icloud.com to use Find My Iphone to find it. 

It would be great to do it in just one click.

## Solution (Current attempt)

Using the Python library Selenium to simulate clicks and login so that the process is automated.

Look at the page html to find the id of the button to be clicked on and tell selenium that. 

As of first commit, this code was never written to be readable, I am sorry.

## Problems faced

- icloud.com changes the id of the elements so the code becomes unusable after some time, it would be great to have a way of keeping to date with them.

- Seems like selenium can't find some elements

## Usage

Run findmyiphonenow.py using Python35 with selenium installed