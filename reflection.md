# Lab 5: Static Code Analysis — Reflection

## 1. What is static code analysis, and why is it useful?

Static code analysis examines source code without executing it to identify potential bugs, security vulnerabilities, maintainability problems, and style violations. In this lab, Pylint, Bandit, and Flake8 helped identify problems in the support ticket tracker before and after modification. Static analysis improves code quality and helps developers detect issues early.

## 2. What issues did you identify and fix?

The original program had a Pylint score of 5.00/10. Bandit identified the use of `eval()` as a medium-severity finding and silent exception handling as a low-severity finding. Other issues included a mutable default argument, unused imports, an unused variable, missing docstrings, incorrect `None` comparison, non-standard function naming, long lines, and file handling without context managers.

I removed the unsafe `eval()` demonstration, replaced the bare exception handler with targeted exception handling, removed unused code, improved file handling with context managers and UTF-8 encoding, and corrected style and documentation issues.

## 3. What are the differences between Pylint, Bandit, and Flake8?

Pylint evaluates code quality, potential programming errors, naming conventions, documentation, and design practices. Bandit focuses on common security weaknesses in Python source code. Flake8 checks Python style and reports issues such as unused imports, excessive line length, and other linting violations. Using all three provides complementary checks.

## 4. What did you learn about static analysis and its limitations?

This lab demonstrated that static analysis can identify many problems without executing the program. After the fixes, Pylint reported 10.00/10, Bandit reported no issues, and Flake8 produced no findings. However, clean static-analysis reports do not prove that a program is functionally correct. Runtime tests are still necessary to verify normal operations, invalid inputs, and data persistence.