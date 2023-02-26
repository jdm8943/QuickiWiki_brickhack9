# QuikiWiki_brickhack9
Repositroy for Brickhack 9 with our project, QuikiWiki

# Overview
We used NLP and A* search on live-queried wikipedia pages to try and find the shortest path between two pages. We started with a naive uninformed search, and with each improvement to the heuristic we cut the time down by about half. For any depth of links past 2, our implementation was intractable. 
## Heuristic
The heuristic uses NLP and a similarity join to quantify the difference between the titles of the current page and the title of the goal page.

# Usage
Quikiwiki.py is main driver file. Start and goal nodes are hardcoded.

# Resources
Trello link: https://trello.com/invite/b/4xUnIxRD/ATTI22f3091c4eedf118166a3aad4fb74112A5C0FD0E/quikiwiki

# Sources
https://www.analyticsvidhya.com/blog/2021/02/a-simple-guide-to-metrics-for-calculating-string-similarity/
