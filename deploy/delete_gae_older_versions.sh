VERSIONS=(`gcloud app versions list --service "$1" --sort-by '~version' --format 'value(version.id)' | sort -r`)
DEL_VERSIONS=("${VERSIONS[@]:$2}")
if [ ${#DEL_VERSIONS[@]} -gt 0 ]
then
  gcloud app versions delete "${DEL_VERSIONS[@]}" --service "$1" -q
fi
