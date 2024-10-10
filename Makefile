data/cleanbookmarks.html: cleanbookmarks.py resources/bookmarks.html
	python $^ $@

data/families.csv: bookmarks2csv.py data/cleanbookmarks.html
	python $^ $@

csv:  data/families.csv