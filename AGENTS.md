# Controlled Super-agent integration test

This fork is an isolated test of DeepSeek Super-agent. It is not an upstream Click bug report.
The seed commit deliberately introduces a truthiness regression in CliRunner's result construction.
The regression contract is tests/test_superagent_return_values.py. Preserve callback return values,
including falsey values, when standalone_mode=False. Preserve normal standalone behavior.

For a task triggered by the superagent-return-values CI failure, diagnose and repair the library,
run the focused tests and inspect the diff. Do not weaken or delete tests, change workflow files,
add dependencies, redesign behavior, or expand into unrelated code. Keep the existing string case.
The shared local test interpreter is available outside the worktree; its path is in the assignment.

All remote writes must stay in BambooGap/click-superagent-test. Use a fresh agent/ branch and open
a pull request explicitly targeting BambooGap/click-superagent-test, base main. Never open anything
against pallets/click, push main, merge, enable auto-merge, force-push, or request external reviews.
Identify automated messages as automated. Report the PR URL, test outcome and any actual limitation.
