# dartmouth-acms
Source for Dartmouth's [Applied and Computational Mathematics Seminar (ACMS) webpage](https://math.dartmouth.edu/~acms/). The site is built using [Quarto](https://quarto.org/) and pulls speaker data from a YAML file.

Instructions for updating:
1. After any updates to `seminar_talks.yml`, run `python update_seminar_pages.py`.
2. Preview the site with `quarto preview`.
3. Once ready, do a final `quarto render`.
4. Git push changes.
5. Replace contents of `acms/public_html` on gauss with the contents of `dartmouth-acms/_site` (is there a way to automate this step?).
