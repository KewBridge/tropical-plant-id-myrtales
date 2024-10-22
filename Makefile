data/cleanbookmarks.html: cleanbookmarks.py resources/bookmarks.html
	mkdir -p data
	python $^ $@

data/families.csv: bookmarks2csv.py data/cleanbookmarks.html
	python $^ $@

csv:  data/families.csv

data/downloadquery_id.txt: families2gbifdownloadquery.py data/families.csv
	python $^ --gbif_user_name ${GBIF_USERNAME} --gbif_email_address ${GBIF_EMAIL} $@

dlreq: data/downloadquery_id.txt

data/images.zip: families2images.py data/families.csv
	python $^ $@

dlimg: data/images.zip
