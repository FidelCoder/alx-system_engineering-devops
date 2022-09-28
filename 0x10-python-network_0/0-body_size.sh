#!/bin/bash
#display size of body of response
curl -s $1| wc -c
