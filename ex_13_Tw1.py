def main():
    import urllib.request, urllib.parse, urllib.error
    import twurl
    import ssl

    TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    while True:
        acct = input('Ingresa la cuenta de Twitter:')
        if (len(acct) <1): break
        url = twurl.augment(TWITTER_URL, {'Screen_name': acct, 'Count': '2'})
        print('Retrieving', url)
        connection = urllib.request.urlopen(url, context=ctx)
        data = connection.read().decode()
        print(data[:250])
        headers = dict(connection.getheaders())
        print('Remaining', headers['x-rate-limit-remaining'])

if __name__ == "__main__":
    main()