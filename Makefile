doc:
	uv run --with rich readme.py
	
update: doc
	git add . 
	git commit -m update 
	git push origin main
