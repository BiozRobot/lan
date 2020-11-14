import shodan

SHODAN_API_KEY = "UNmOjxeFS2mPA3kmzm1sZwC0XjaTTksy"

api = shodan.Shodan(SHODAN_API_KEY)

f = open('ipprinter.txt', 'w')

try:
	results = api.search('port:9100 pjl')

	for result in results['matches']:

		print('IP: {}'.format(result['ip_str']))
		ip = result['ip_str']
		f.write("{} \n".format(ip))

except shodan.APIError, e:
        print('Error: {}'.format(e))


f.close()
