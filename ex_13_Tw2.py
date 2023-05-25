def main():
    import urllib.request, urllib.parse, urllib.error
    import twurl
    import json
    import ssl

    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    while True:
        acct = input('Ingresa la cuenta de Twitter:')
        if (len(acct) < 1): break
        url = twurl.augment(TWITTER_URL, {'Screen_name': acct, 'Count': '5'})
        print('Retrieving', url)
        connection = urllib.request.urlopen(url, context=ctx)
        data = connection.read().decode()
        js = json.loads(data)
        headers = dict(connection.getheaders())
        print('Remaining', headers['x-rate-limit-remaining'])
        for u in js['users']:
            print(u['Screen_name'])
            if 'status' not in u:
                print(' *No status found')
                continue
            s = u['status']['text']
            print('', s[:50])
if __name__ == "__main__":
    main()