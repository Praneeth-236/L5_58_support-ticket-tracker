# Static Code Analysis — Issue Report

**Project:** Support Ticket Tracker  
**Target file:** `support_ticket_tracker.py`  
**Analysis tools:** Pylint, Bandit, Flake8

## Identified Issues

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Unsafe `eval()` usage | Security — Medium | 92 | Bandit B307 flags the use of `eval()`, which can execute arbitrary Python expressions. The unsafe demonstration is unnecessary for the ticket tracker's normal functionality. | Remove the `eval()` call and the associated unsafe demonstration block. |
| Silent exception handling | Error handling — Low | 24–25 | Bandit B110 flags a bare exception handler that silently suppresses errors during ticket assignment. | Catch the expected `KeyError` and return `False` when the ticket ID does not exist. |
| Mutable default argument | Potential bug | 10 | Pylint W0102 flags `audit_log=[]`. A mutable default list can persist across calls and share data unexpectedly. | Use `None` as the default and initialize a new list inside the function. |
| Unused imports | Code quality | 4–5 | Pylint W0611 and Flake8 F401 identify unused imports of `sys` and `random`. | Remove both imports. |
| Unused local variable | Code quality | 84 | Pylint W0612 and Flake8 F841 identify the unused variable `count`. | Remove the unnecessary assignment. |
| File handling without context managers | Resource management | 46, 53 | Pylint R1732 flags file operations that do not use context managers. The files are manually closed, but a `with` statement provides more reliable resource cleanup. | Use `with open(...)` and specify UTF-8 encoding. |
| Incorrect `None` comparison | Style | 37 | Pylint C0121 and Flake8 E711 flag `status != None`. | Replace it with `status is not None`. |
| Excessively long lines | Formatting | 10, 14, 63, 71, 79–80 | Pylint C0301 and Flake8 E501 flag lines that exceed the configured length limits. | Break long expressions and function calls across multiple lines. |
| Missing docstrings | Maintainability | Multiple | Pylint C0114 and C0116 identify the missing module and function docstrings. | Add a module docstring and concise docstrings to functions. |
| Non-standard function naming | Style | 66 | Pylint C0103 flags `closeTicket()` because it does not follow Python's snake_case convention. | Rename it to `close_ticket()` and update its call sites. |
| Unused function parameter | Code quality | 20 | Pylint W0613 identifies the unused `notify` parameter in `assign_ticket()`. | Remove the parameter if notifications are outside the program's intended scope, updating call sites accordingly. |

## Verification Plan

1. Run Pylint, Bandit, and Flake8 on the original source and preserve the baseline reports.
2. Fix the documented issues, prioritizing security and error handling.
3. Rerun all three tools against the modified source.
4. Verify that the unsafe `eval()` call and the silent exception handling have been removed.
5. Target a Pylint score above 9.5 and resolve Flake8 findings.
6. Test the program's normal ticket operations and invalid-ticket behavior.
7. Preserve the before-and-after reports and make the three required Git commits.

**Note:** Line numbers above refer to the original source file. They may change after modifications.