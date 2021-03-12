Step|App Prep Actions (done at end of previous step)|User Actions| Event | App Check Actions
-----|-----|-----|-----|-----
1| <ul><li>Protect main branch</li> <li>Create first issue</li><li>respond with first activity</li></ul>|open first pull request, commit LICENSE file | `pull_request.opened`|<ul><li>check if LICENSE exists at top-level</li></ul>
2|<ul><li>respond--ask user to commit .gitignore</li></ul> |user commits .gitignore|`pull_request.synchronize` | <ul><li>Check that it is the right file for Python?</li></ul>
3|<ul><li>respond: ask user to merge PR</li></ul>|Users merges PR| `pull_request.closed`| <ul><li>gate: Check if PR was actually merged </li></ul>
4|<ul><li>close first issue</li><li>create second issue</li><li>responds in closed PR with link to new issue for next</li><li>Introduce topic: Python packages and modules (issue body)</li></ul>|User commits __init__.py's and opens PR|`pull_request.synchronize`|<ul><li>gate: check for correct files/locations</li></ul>  |
5 |<ul><li>respond with next activity: Create Python Module</li></ul> | User commits code with "working" module | `pull_request.synchronize` | gate: check if module is correct 