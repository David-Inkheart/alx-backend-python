# Unittests and Integration Tests

This repository contains code examples and exercises for understanding and implementing unit tests and integration tests in Python. The tests are written using the `unittest` framework and the `unittest.mock` library.

## Table of Contents

1. **Unittests and Integration Tests**
2. **Tasks**
    - [0. Parameterize a unit test](#0-parameterize-a-unit-test)
    - [1. Parameterize a unit test exception](#1-parameterize-a-unit-test-exception)
    - [2. Mock HTTP calls](#2-mock-http-calls)
    - [3. Parameterize and patch](#3-parameterize-and-patch)
    - [4. Parameterize and patch as decorators](#4-parameterize-and-patch-as-decorators)
    - [5. Mocking a property](#5-mocking-a-property)
    - [6. More patching](#6-more-patching)
    - [7. Parameterize](#7-parameterize)
    - [8. Integration test: fixtures](#8-integration-test-fixtures)
    - [9. Integration tests](#9-integration-tests)

## Tasks

### [0. Parameterize a unit test](./test_utils.py)
Familiarize yourself with the `utils.access_nested_map` function and understand its purpose. In this task, you will write the first unit test for `utils.access_nested_map`.

Create a `TestAccessNestedMap` class that inherits from `unittest.TestCase`. 
Implement the `TestAccessNestedMap.test_access_nested_map` method to test that the method returns the expected result for different inputs.
Decorate the method with `@parameterized.expand` to test the function for specific inputs.
```
nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")
```

### [1. Parameterize a unit test exception](./test_utils.py)
Implement the `TestAccessNestedMap.test_access_nested_map_exception` method to test that a `KeyError` exception is raised for certain inputs. Use the `assertRaises` context manager to check for the exception and verify the exception message.

### [2. Mock HTTP calls](./test_utils.py)
Familiarize yourself with the `utils.get_json` function. Define the `TestGetJson` class and implement the `TestGetJson.test_get_json` method to test that `utils.get_json` returns the expected result. Use `unittest.mock.patch` to mock the `requests.get` function and ensure it returns the desired payload.

### [3. Parameterize and patch](./test_utils.py)
Implement the `TestMemoize` class with a `test_memoize` method. Inside the `test_memoize` method, define a class and use `unittest.mock.patch` to mock a method. Test that the method is only called once when calling a decorated property multiple times.

### [4. Parameterize and patch as decorators](./test_client.py)
Implement the `TestGithubOrgClient` class and the `test_org` method. Use `@patch` as a decorator to mock the `get_json` function and ensure it is called once with the expected argument. Use `@parameterized.expand` as a decorator to parametrize the test with different org examples.

### [5. Mocking a property](./test_client.py)
Implement the `test_public_repos_url` method to unit-test `GithubOrgClient._public_repos_url`. Use `patch` as a context manager to mock `GithubOrgClient.org` and test the result of `_public_repos_url` based on the mocked payload.

### [6. More patching](./test_client.py)
Implement the `TestGithub

OrgClient.test_public_repos` method to unit-test `GithubOrgClient.public_repos`. Use `@patch` as a decorator to mock `get_json` and `GithubOrgClient._public_repos_url`. Test that the list of repos is as expected and that the mocked property and `get_json` are called once.

### [7. Parameterize](./test_client.py)
Implement the `TestGithubOrgClient.test_has_license` method to unit-test `GithubOrgClient.has_license`. Parametrize the test with different inputs and expected return values.

### [8. Integration test: fixtures](./test_client.py)
Create the `TestIntegrationGithubOrgClient` class and implement the `setUpClass` and `tearDownClass` methods. Use `@parameterized_class` to parameterize the class with fixtures found in `fixtures.py`. Mock the `requests.get` function to return example payloads.

### [9. Integration tests](./test_client.py)
Implement the `test_public_repos` method to test `GithubOrgClient.public_repos` and make sure it returns the expected results. Implement `test_public_repos_with_license` to test `public_repos` with the `license` argument and verify the result matches the expected value from the fixtures.
