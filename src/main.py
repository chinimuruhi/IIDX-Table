import requests
import urllib.request
import gzip

with open('./dist/sp12.iidx.app.json', mode='w') as f:
    r = requests.get('https://sp12.iidx.app/api/v1/sheets')
    f.write(r.text)

with open('./dist/bpim.msqkn310.workers.dev.json', mode='w') as f:
    r = requests.get('https://bpim.msqkn310.workers.dev/release')
    f.write(r.text)

with open('./dist/cpi.makecir.com.json', mode='w') as f:
    r = requests.get('https://cpi.makecir.com/scores')
    f.write(r.text)

with open('./dist/textage.cc.json', mode='w') as f:
    r = requests.get('https://textage.cc/score/titletbl.js')
    f.write(r.text)

with open('./dist/bm2dx.com.json', mode='w') as f:
    with urllib.request.urlopen('https://bm2dx.com/IIDX/notes_radar/notes_radar.json.gz') as res:
        dec = gzip.GzipFile(fileobj=res)
        f.write(dec.read().decode("utf-8"))

with open('./dist/zasa.sakura.ne.jp.json', mode='w') as f:
    r = requests.get('https://zasa.sakura.ne.jp/dp/run.php')
    f.write(r.text)