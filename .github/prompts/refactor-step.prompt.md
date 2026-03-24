---
mode: 'agent'
description: 'Refactor a specific item type in the Gilded Rose codebase'
---

# Refactor Step

Given an item type name, review the corresponding updater class in gilded_rose.py and suggest improvements.

## Steps
1. Identify the updater class for the given item type
2. Check that the business rules match the requirements in GildedRoseRequirements.md
3. Suggest any code improvements for readability or maintainability
4. Verify that existing tests cover the item type behavior
5. If tests are missing, suggest new test cases

## Context
- The project uses the Strategy pattern with an ItemUpdater base class
- Each item type has its own updater subclass
- Tests are in test_gilded_rose.py using unittest

## Input
The user will provide an item type name such as Aged Brie, Sulfuras, Backstage passes, Conjured, or normal.
