1. Use `Wappalyzer` to identify an application that's using react.

2. Open des Devs tools and navigate to whatever tal loads the client side javascript files (Sources)

3. Look at a folder labeled `src` and check the if the `React` statement is imported

When you've identified a target application that doesn't have the obfuscate the react code, the next is to download  that using `JS Miner` extension on Burp Suite

4. Navigate to the sitemap under the target tab, rightclick on the root of the target app, `Extensions` -> `JS Miner` -> `Scans` -> `JS sources mapper (active)`

5. Scan the react files from any static code analysis tool using [Semgrep](https://github.com/semgrep/semgrep)

6. Onse Semgrep is install, Navigate to the folder source code and run

```sh
semgrep scan
```

