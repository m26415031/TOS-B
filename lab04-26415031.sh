#!/bin/bash

curl -s http://www.google.com | sed -e 's/<[^>]*>//g'

