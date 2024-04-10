# Import Module
from bs4 import BeautifulSoup

# HTML Document
HTML_DOC = """
			<html>
			<head>
				<title> Find Next Siblings </title>
			</head>
			<body>
					<h2 class = "languages">1957: FORTRAN</h2>
					<div>

					<p class = "languages">1972: C</p>

					<p class = "languages">1983: C++</p>

					<p class = "languages">1991: Python</p>

					<p class = "languages">1993: Ruby</p>

					<p class = "languages">1995: Java</p>

					<p class = "languages">1995: PHP</p>

					<p class = "languages">1995: JavaScript</p>
					</div>

			</body>
			</html>
			"""

# Function to find all the next siblings
def findNextSiblings(html):

	# parse html content
	soup = BeautifulSoup(html, "html.parser")

	element = soup.h2

	# Extracting all the next siblings of an element
	nextSiblings = element.find_next_siblings("p")

	# Printing all the next siblings
	for nextSibling in nextSiblings:
		print(nextSibling)


# Function Call
findNextSiblings(HTML_DOC)
