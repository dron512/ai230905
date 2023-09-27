import urllib.request

# def down(url,filename):
#     urllib.request.urlretrieve(url, filename)


def down(url,filename):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
    }
    request = urllib.request.Request(url, headers=headers)
    try:
        response = urllib.request.urlopen(request)

        with open(filename, 'wb') as local_file:
            local_file.write(response.read())

        response.close()
    except Exception as e:
        print(f"Error: {e}")
