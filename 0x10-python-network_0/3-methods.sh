#!/bin/bash
#get accepted methods
curl -sIX OPTIONS  $1| grep Allow|cut -d ' ' -f 2-
