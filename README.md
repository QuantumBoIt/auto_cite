## cite.py

from https://github.com/Kildrese/scholarBibTex

https://www.reddit.com/r/LaTeX/comments/tvb5r1/python_script_to_cite_bibtex_directly_from_google/



- usage:
  1. add paper names to `paper_titles`
  2. run the following command(if you need proxy)

```
python cite.py
```























## scholar.py

This is a fork of www.icir.org/christian/scholar.html with some added functionality.

Fetchs google scholar queries and outputs info or citation data

### FAQ

#### I get nothing but ```403 Forbidden```

The default of scholar is to fake a google id. Unfortunately that yields a ```403 Forbidden``` after a while. You can adjust the google id to your actual id by the following steps:

 * export the cookies.txt from your browser (needs an extension, e.g. https://addons.mozilla.org/de/firefox/addon/export-cookies/)
 * find the google-id cookie, its name is GSP=ID=
 * put your google id in line 305 instead of the fake one

#### How to download a paper?

Simply use the power of the shell:

wget $(python2 scholar.py "\<SEARCHTERMS\>" -c 1 | grep "^ *PDF" | sed "s/ *PDF //")
