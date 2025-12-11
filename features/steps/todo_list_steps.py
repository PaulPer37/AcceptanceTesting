# -*- coding: utf-8 -*-
from behave import given, when, then, use_step_matcher
from todo_list import TodoList

# Usar regex matcher para mayor flexibilidad
use_step_matcher("re")

# ========== GIVEN STEPS ==========

@given(r'the to-do list is empty')
def step_given_empty_list(context):
    context.todo_list = TodoList()

@given(r'the to-do list contains tasks:?')
def step_given_list_with_tasks(context):
    context.todo_list = TodoList()
    if context.table:
        for row in context.table:
            task_name = row['Task']
            context.todo_list.add_task(task_name)

# ========== WHEN STEPS ==========

@when(r'the user adds a task "([^"]*)"')
def step_when_add_task(context, task):
    context.todo_list.add_task(task)

@when(r'the user lists all tasks')
def step_when_list_tasks(context):
    context.task_list = context.todo_list.list_tasks()

@when(r'the user marks task "([^"]*)" as completed')
def step_when_mark_completed(context, task):
    result = context.todo_list.mark_completed(task)
    assert result, f"Failed to mark task '{task}' as completed"

@when(r'the user clears the to-do list')
def step_when_clear_list(context):
    context.todo_list.clear_all()

@when(r'the user deletes task "([^"]*)"')
def step_when_delete_task(context, task):
    result = context.todo_list.delete_task(task)
    assert result, f"Failed to delete task '{task}'"

# ========== THEN STEPS ==========

@then(r'the to-do list should contain "([^"]*)"')
def step_then_list_contains(context, task):
    tasks = [t.description for t in context.todo_list.list_tasks()]
    assert task in tasks, f"Task '{task}' not found in to-do list. Current tasks: {tasks}"

@then(r'the output should contain "([^"]*)"')
def step_then_output_contains(context, task):
    tasks = [t.description for t in context.task_list]
    assert task in tasks, f"Task '{task}' not found in output. Current tasks: {tasks}"

@then(r'the to-do list should show task "([^"]*)" as completed')
def step_then_task_completed(context, task):
    for t in context.todo_list.list_tasks():
        if t.description == task:
            assert t.status == "Completed", f"Task '{task}' status is '{t.status}', not 'Completed'"
            return
    assert False, f"Task '{task}' not found in to-do list"

@then(r'the to-do list should be empty')
def step_then_list_empty(context):
    assert context.todo_list.is_empty(), f"To-do list is not empty. Contains {len(context.todo_list.tasks)} tasks"

@then(r'the to-do list should not contain "([^"]*)"')
def step_then_list_not_contains(context, task):
    tasks = [t.description for t in context.todo_list.list_tasks()]
    assert task not in tasks, f"Task '{task}' is still in to-do list. Current tasks: {tasks}"