import discogs_client
d = discogs_client.Client('ExampleApplication/0.1', user_token="xOwsHwGZNYqIsSFLkBMihoGocHATUbRZlAOssQPX")

#results = d.search(type='release', title='Mose in your ear')
results = d.search('mose in your ear')
result1 = results[0]
release = d.master(597268)
#info = results[0]
#print(results.page(1))
#print(results[0])
print(result1)
print(release)
#print(release.genres)