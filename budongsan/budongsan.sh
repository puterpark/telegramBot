#!/bin/sh

curl --location --request GET '{naver_budongsan_url}' > data/data.txt

/usr/bin/python3 budongsan.py