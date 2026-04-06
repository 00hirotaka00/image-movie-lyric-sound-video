#!/usr/bin/env python3
"""
デプロイ前に実行するスクリプト。
index.html内の ____DEPLOY_TIME____ を現在の日本時間に書き換えます。

使い方:
  python update_deploy.py
  → index.html を上書き更新してから GitHub にアップしてください。
"""

import re
from datetime import datetime, timezone, timedelta

JST = timezone(timedelta(hours=9))
now = datetime.now(JST).strftime('%Y-%m-%d %H:%M JST')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(
    r'const DEPLOY_TIME = ".*?";',
    f'const DEPLOY_TIME = "{now}";',
    html
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'✅ Deploy time updated: {now}')
