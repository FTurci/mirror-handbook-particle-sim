stripout:
	nbstripout --keep-output contents/*.ipynb
book:
	jupyter-book build ../handbook
