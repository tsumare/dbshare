#!/usr/bin/env python

import sys, dropbox, os, json
import imp

CONF_FILE = os.path.expanduser('~/.dbshare.conf')
try:
	tokens = imp.load_source('tokens', CONF_FILE)
except IOError as e:
	f = open(CONF_FILE, 'w')
	f.write("OAUTH_TOKEN = None")
	f.close()
	del f
	tokens = imp.load_source('tokens', CONF_FILE)

if tokens.OAUTH_TOKEN is None:
	print 'Enter app key:',
	APP_KEY = raw_input().strip()
	print 'Enter app secret:',
	APP_SECRET = raw_input().strip()

	flow = dropbox.client.DropboxOAuth2FlowNoRedirect(APP_KEY, APP_SECRET)
	print 'Please authorize the application at', flow.start().strip()
	print 'Enter the token you are given:',
	token = raw_input().strip()
	access_token, user_id = flow.finish(token)
	print 'Updating ~/.dbshare.conf...'
	f = open(CONF_FILE, 'w')
	f.write("OAUTH_TOKEN = '%s'"%(access_token,))
	f.close()
	tokens.OAUTH_TOKEN = access_token

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
