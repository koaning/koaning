update:
	python -m pip install uv 
	uv run --with rich readme.py
	git add . 
	git commit -m update 
	git push origin main
