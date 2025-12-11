Feature: To-Do List Manager
  As a user
  I want to manage my tasks
  So that I can organize my daily activities

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | Task          |
      | Buy groceries |
      | Pay bills     |
    When the user lists all tasks
    Then the output should contain "Buy groceries"
    And the output should contain "Pay bills"

  Scenario: Mark a task as completed
    Given the to-do list contains tasks:
      | Task          | Status  |
      | Buy groceries | Pending |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | Task          |
      | Buy groceries |
      | Pay bills     |
    When the user clears the to-do list
    Then the to-do list should be empty

  Scenario: Delete a specific task
    Given the to-do list contains tasks:
      | Task          |
      | Buy groceries |
      | Pay bills     |
      | Call mom      |
    When the user deletes task "Pay bills"
    Then the to-do list should not contain "Pay bills"
    And the to-do list should contain "Buy groceries"
    And the to-do list should contain "Call mom"