#!/bin/bash
git checkout stg
git merge --commit dev
time_tag=$(date '+%d.%m.%Y.%H.%M.%S')
git tag "$time_tag"
git push origin stg
git push origin "$time_tag"
