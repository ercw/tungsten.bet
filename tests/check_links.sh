#!/bin/sh
# Prints the HTTP status of every source URL in the dataset (follows redirects).
# openai.com answers 403 to non-browser clients; confirm those in a browser.
cd "$(dirname "$0")/.." || exit 1
python3 -I -c "
import json
for e in json.load(open('data/items.json', encoding='utf-8')): print(e['id'], e['url'])
for b in json.load(open('data/bets.json', encoding='utf-8')):
    for s in b['sources']: print(b['id'], s['url'])
" | while read -r id url; do
  code=$(curl -s -o /dev/null -L --max-time 20 -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36" -w "%{http_code}" "$url")
  echo "$id $code $url"
done
