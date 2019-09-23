#!/usr/bin/env bash

gcloud functions deploy wunder-gkeep \
  --entry-point wunder_to_keep \
  --runtime python37 \
  --trigger-http \
  --region europe-west1 \
  --memory 128MB \
  --env-vars-file .env.yaml
