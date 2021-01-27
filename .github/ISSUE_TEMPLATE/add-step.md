---
name: Add step
about: template for addin a step to course
title: ''
labels: infrastructure, learning
assignees: ''

---

## Step Summary and Purpose

**working branch:** 
### Outline Description
Step|User Actions (to trigger step)| App Actions| Related Event
-----|-----|-----|-----
| | |

### Primary Goal/Outcome


## References
* Solution branch: https://github.com/nanoMFG/python-best-practices-v2-template/tree/solution
* [Response Style guide](https://google.github.io/styleguide/pyguide.html)
* [Available actions](https://lab.github.com/docs/actions/)
* [GitHub webhook Events](https://docs.github.com/en/developers/webhooks-and-events/webhook-events-and-payloads)

### Update procedure
* Use a topic branch to apply updates with a branch name like : `step-<stepnum>`.  
* Merge main into your topic branch occasionally: `topic_branch <- main`
* When ready to test, open a PR to main.  When a PR is created the "course bot" will run checks and validation and if it passes it will create a deployment.
* If the validation fails, look at the message, close the PR (without merging), add some more commits to the branch to fix. Then, re-open the PR to trigger a new deployment. 
 * Use the deployment on the topic branch to test*

\*Note you will need to delete the course repo that was created in your account if it already exists before testing a new deployment.
