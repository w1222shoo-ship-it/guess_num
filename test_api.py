import json
import time
import urllib.request

def post_json(path, data):
    url = 'http://127.0.0.1:5000' + path
    b = json.dumps(data).encode()
    req = urllib.request.Request(url, data=b, headers={'Content-Type':'application/json'})
    with urllib.request.urlopen(req, timeout=5) as r:
        return json.loads(r.read().decode())

def main():
    # wait a bit for server
    for i in range(10):
        try:
            gid = post_json('/start', {})['game_id']
            break
        except Exception:
            time.sleep(0.3)
    else:
        print('Cannot connect to server')
        return

    print('game_id', gid)

    for g in [50, 25, 75, 12, 37]:
        res = post_json('/guess', {'game_id': gid, 'guess': g})
        print('guess', g, '->', res)
        if res.get('result') == 'correct':
            break

if __name__ == '__main__':
    main()
