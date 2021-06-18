#
# Example file for retrieving data from the internet
#

def main():
    import urllib.request
    url = "http://www.baidu.com"
    handle = urllib.request.urlopen(url)
    print(handle.getcode())
    print(handle.read())


if __name__ == "__main__":
    main()
