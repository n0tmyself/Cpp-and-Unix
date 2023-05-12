#!/bin/bash
git checkout prd
git merge --commit dev
time_tag=$(date '+%d.%m.%Y.%H.%M.%S')
git tag "$time_tag"
git push origin prd
git push origin "$time_tag"
