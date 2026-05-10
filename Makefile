push:
	git add .
	git commit -m "$$(date +%Y/%m/%d)$ by $$(whoami)"
	git push
