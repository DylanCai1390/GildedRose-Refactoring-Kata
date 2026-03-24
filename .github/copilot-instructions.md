# Copilot Instructions

## Project Overview
This is the Gilded Rose Refactoring Kata implemented in Python. The project manages inventory for a fictional inn, where items have quality and sell-in values that change daily according to specific business rules.

## Code Style
- Use Python 3.9+ conventions
- Follow PEP 8 style guidelines
- Use snake_case for functions and variables
- Use PascalCase for class names
- Keep methods short and focused on a single responsibility

## Architecture
- The codebase uses the Strategy design pattern
- Each item type has its own updater class that inherits from ItemUpdater
- New item types should be added by creating a new updater class and registering it in UPDATER_MAP
- Do not modify the Item class

## Testing
- Tests use the built-in unittest framework
- Run tests with python3 test_gilded_rose.py -v
- Approval tests are in tests/test_gilded_rose_approvals.py and require the approvaltests package
- When changing item behavior, update the approved output file accordingly

## Business Rules
- All items have sell_in and quality values
- Quality degrades as the sell date approaches
- Quality is never negative and never exceeds 50 (except Sulfuras at 80)
- Aged Brie increases in quality over time
- Sulfuras never changes
- Backstage passes increase then drop to 0 after the concert
- Conjured items degrade twice as fast as normal items
