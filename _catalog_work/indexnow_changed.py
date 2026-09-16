"""Submit blog URLs changed since a given commit to IndexNow (quota-free).

Usage: python indexnow_changed.py [since_commit]   (default: 3 commits back)
"""
import json
import subprocess
import sys
import urllib.error
import urllib.request

REPO = r'C:\Users\Saladin\Desktop\yominelectric-main'
KEY = '3672105a741b4228a5c276221f1dd067'
HOST = 'www.yominelectric.com'
SITE = 'https://www.yominelectric.com'


def git(*a):
    r = subprocess.run(['git'] + list(a), cwd=REPO, capture_output=True)
    return r.stdout.decode('utf-8', 'ignore')


since = sys.argv[1] if len(sys.argv) > 1 else 'HEAD~3'
files = [l.strip() for l in git('diff', '--name-only', '%s..HEAD' % since).splitlines() if l.strip()]
# git paths already include the blog/ prefix - do not add it again
blog = sorted({f[:-5] for f in files if f.startswith('blog/') and f.endswith('.html')})

urls = ['%s/%s' % (SITE, s) for s in blog]
print('commits since %s: %d files, %d blog pages' % (since, len(files), len(blog)))
if not urls:
    print('nothing to submit')
    raise SystemExit(0)

# Post-deploy guard: never announce a URL that is not live yet. On 2026-09-14 a batch
# announced blog URLs before they were deployed, so Bing/Yandex crawled them early and
# logged avoidable 404s. Only submit URLs that answer 200 right now.
def is_live(u):
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=25) as r:
            return r.status == 200
    except Exception:
        return False


live, not_live = [], []
for u in urls:
    (live if is_live(u) else not_live).append(u)

if not_live:
    print('SKIPPED (not live yet - deploy first, then re-run):')
    for u in not_live:
        print('   %s' % u)
if not live:
    print('nothing live to submit')
    raise SystemExit(0)

urls = live
print('submitting %d live URLs (first 5): %s' % (len(urls), urls[:5]))

payload = json.dumps({'host': HOST, 'key': KEY,
                      'keyLocation': '%s/%s.txt' % (SITE, KEY), 'urlList': urls}).encode('utf-8')
for ep in ['https://api.indexnow.org/indexnow', 'https://www.bing.com/indexnow']:
    req = urllib.request.Request(ep, data=payload,
                                 headers={'Content-Type': 'application/json; charset=utf-8'})
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            print('%-38s HTTP %s' % (ep, r.status))
    except urllib.error.HTTPError as e:
        print('%-38s HTTP %s %s' % (ep, e.code, e.read().decode('utf-8', 'ignore')[:160]))
    except Exception as e:
        print('%-38s ERR %s' % (ep, e))
