# GBIF_USER_NAME = ${GBIF_USER_NAME}
# GBIF_EMAIL_ADDRESS = ${GBIF_EMAIL_ADDRESS}

data/cleanbookmarks.html: cleanbookmarks.py resources/bookmarks.html
	python $^ $@

data/families.csv: bookmarks2csv.py data/cleanbookmarks.html
	python $^ $@

csv:  data/families.csv

data/query.json: families2gbifdownloadquery.py data/families.csv
	python $^ --gbif_user_name ${GBIF_USER_NAME} --gbif_email_address ${GBIF_EMAIL_ADDRESS} $@

dlreq: data/query.json
