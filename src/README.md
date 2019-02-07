# Source of Pages and Pagelets
This folder contains the source files required by the devserver

# Directory Structure
```
| - src / pagelets
| - src / pages
```

# src / pagelets
- Pagelets are used to build the container HTML layout / aka templating
- Pagelets are suggested to be numbered so that the loading order is guaranteed
- eg.
-- 01.header.html
-- 02.nav.html
-- 03.CONTENT.html
-- 04.footer.html
- It's mandatory to have a blank file ending in CONTENT.html 

# src / pages
- Any page inside this folder is identified as navigation path
- The content inside this folder is replaced while generating the file
- eg. if a page filename is "home.html", and considering pagelets as above
-- 01.header and 02.nav files are loaded from src/pagelets
-- home.html is loaded from src/pages
-- 04.footer is loaded from src/pagelets


