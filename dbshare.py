#!/usr/bin/env python

import sys, dropbox, os, json

import imp
tokens = imp.load_source('tokens', os.path.expanduser('~/.dbshare.conf'))

if tokens.OAUTH_TOKEN is None:
	print 'Enter app key:',
	APP_KEY = raw_input().strip()
	print 'Enter app secret:',
	APP_SECRET = raw_input().strip()

	flow = dropbox.client.DropboxOAuth2FlowNoRedirect(APP_KEY, APP_SECRET)
	print 'Please authorize the application at', flow.start()
	print 'Enter the token you are given:',
	token = raw_input().strip()
	access_token, user_id = flow.finish(token)
	print 'Put the following line in ~/.dbshare.conf:'
	print "OATH_TOKEN = '%s'"%(access_token,)
	sys.exit(0)

if len(sys.argv) < 2:
	print 'dbshare.py filename_in_dropbox'
	sys.exit(0)

def get_dropbox_root():
	return os.path.realpath(json.load(open(os.path.expanduser('~/.dropbox/info.json'), 'r'))['personal']['path'])

file_path = os.path.relpath(os.path.realpath(sys.argv[1]), get_dropbox_root())
if file_path[0] == '/' or file_path[0:3] == '../':
	print 'File not in dropbox, unable to share.'
	sys.exit(1)

dbclient = dropbox.client.DropboxClient(tokens.OAUTH_TOKEN)
print dbclient.share('/'+file_path, False)['url']
