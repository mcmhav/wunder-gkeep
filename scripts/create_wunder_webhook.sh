#!/usr/bin/env bash

curl "https://a.wunderlist.com/api/v1/webhooks" \
  -X POST \
  -H "X-Access-Token: $WUNDER_ACCESS_TOKEN" \
  -H "X-Client-ID: $WUNDER_CLIENT_ID" \
  -d "list_id=$WUNDER_DAGLIG" \
  -d "url=$CLOUD_URL" \
  -d "processor_type=generic" \
  -d "configuration=''"

get_hooks() {
  curl "https://a.wunderlist.com/api/v1/webhooks?list_id=$WUNDER_DAGLIG" \
    -H "X-Access-Token: $WUNDER_ACCESS_TOKEN" \
    -H "X-Client-ID: $WUNDER_CLIENT_ID"
}

delete_hook() {
  REVISION=""
  curl "https://a.wunderlist.com/api/v1/webhooks/$REVISION?revision=0" \
    -X DELETE \
    -H "X-Access-Token: $WUNDER_ACCESS_TOKEN" \
    -H "X-Client-ID: $WUNDER_CLIENT_ID"
}
