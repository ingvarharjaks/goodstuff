#!/usr/bin/env python

# Client for HTTP based SOAP services. No-nonsense.
#
# License: BSD
# (c) 2012 Ingvar Harjaks <ingvarharjaks@gmail.com>

import urllib2

class SOAP_Client():
	def __init__(self, endpoint, payload):
		self.req = urllib2.Request(endpoint, payload)
		self.req.add_header('Content-Type', 'text/xml')
		# put other headers here e.g. SOAPAction, Authorization etc

	def make_request(self):
		try:
			self.resp = urllib2.urlopen(self.req)
		except (urllib2.URLError, urllib2.HTTPError):
			raise Exception, "Unable to get response from SOAP service: %s" % \
				self.req.get_full_url()

	def read_response(self):
		resp = self.resp.read()
		if len(resp) == 0:
			raise Exception, "SOAP service returned empty response: %s" % \
				self.req.get_full_url()
		return resp

	# save response into file instead of memory. useful for services where
	# response is huuuuge. only chunks are kept in memory.
	def save_response(self, tofile):
		f = open(tofile, 'w')
		chunk_size = 16 * 1024
		while True:
			chunk = self.resp.read(chunk_size)
			if not chunk: break
			f.write(chunk)
