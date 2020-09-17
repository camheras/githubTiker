GithubTiker
=================

> An interactive Markdown template based on
> [markdown-it](https://github.com/markdown-it/markdown-it).

Usage
-----

Edit `index.txt` in a text editor.

Open `index.html` in a browser to see the result.

Implementation
--------------

The code reads the contents of `index.txt` by using a hidden `iframe`.
Locally, this works very well in Firefox. Chrome, however, imposes
restrictions on local file access. A workaround is to host the files
on a local HTTP server, for example
[http-server](https://www.npmjs.com/package/http-server):

    $ npm install -g http-server
    $ http-server -a localhost -p 80

Run these commands in the directory containing `index.html` and
`index.txt`. The template is now available from <http://localhost/>.

The following implementations are available:

### `loadIframe()` (default)

-   Loads the
    [.contents()](http://stackoverflow.com/questions/1796619/how-to-access-the-content-of-an-iframe-with-jquery)
    of a hidden `iframe`
-   Requires the loaded file to have a file extension of `.txt`
-   Locally:
    -   Works in Firefox and Internet Explorer
-   On a server:
    -   Works in Firefox, Chrome, Safari and Internet Explorer

### `loadAjax()`

-   Loads the file with [$.get()](https://api.jquery.com/jquery.get/)
-   The file can have any extension (e.g., `.md`)
-   Locally:
    -   Works in Firefox
    -   The file extension `.txt` is recommended because otherwise,
        Firefox tends to store partial files in its download directory
-   On a server:
    -   Works in Firefox, Chrome, Safari and Internet Explorer
    -   Can use any file extension

Similar methods: ~~[$.load()](http://api.jquery.com/load/)~~,
    ~~[XMLHttpRequest](http://stackoverflow.com/questions/14446447/javascript-read-local-text-file)~~.

Miscellaneous
-------------

The example text is the article
[General Parser Combinators in Racket](https://epsil.github.io/gll/).

A somewhat similar project is
[Markdeep](https://casual-effects.com/markdeep/) by Morgan McGuire.
There, both the document and the parser is stored in a single file
with the extension `.md.html`, which behaves appropriately whether it
is opened in a text editor or a browser.

License
-------

[![License][license-image]][license-url]

Released under the MIT License. See the [LICENSE](LICENSE) file
for details.

[license-image]: https://img.shields.io/npm/l/markdownlint.svg
[license-url]: http://opensource.org/licenses/MIT
