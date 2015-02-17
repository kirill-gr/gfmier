# GFMier
## Fixes pandoc markdown output for use on GitHub

Currently pandoc outputs markdown_github with line breaks as is, which doesn't work for GitHub. This script replaces all in-table line breaks with HTML `<br>`.

##Usage
File, passed as a parameter will be overwritten with fixed version.
