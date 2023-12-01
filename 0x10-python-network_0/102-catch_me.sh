#!/bin/bash
# Sending a POST request with a custom header to cause the server to respond with the desired message
curl -s -X POST -H "Referer: You got me!" 0.0.0.0:5000/catch_me
