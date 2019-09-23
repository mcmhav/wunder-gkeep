#!/usr/bin/env bash

curl "https://a.wunderlist.com/api/v1/webhooks" \
  -X POST \
  -H "X-Access-Token: $WUNDER_ACCESS_TOKEN" \
  -H "X-Client-ID: $WUNDER_CLIENT_ID" \
  -d "list_id=$WUNDER_DAGLIG" \
  -d "url=$CLOUD_URL" \
  -d "processor_type=generic" \
  -d "configuration=''"
