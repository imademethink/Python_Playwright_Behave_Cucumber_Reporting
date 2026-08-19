Feature: Home page validation

  @simple
  Scenario: Home Page Menu Item Validation
    Given User is in on home page
    When User validates main menu items
    Then Main menu item validation should be successful

  Scenario: Welcome Section Icon Validation
    Given User is in on home page
    When User validates main menu items
    When User validates welcome section items
    Then Welcome section item validation should be successful

  @CucumberWithBut
  Scenario: Registration Flow Validation
    Given User is in on home page
    When User perform registration
    Then Registration should be successful
    Then Account opening should not be successful

# with filtering using a tag
#  behave -f allure_behave.formatter:AllureFormatter -o allure-report  -f plain  --no-skipped --tags=@simple
#  behave -f allure_behave.formatter:AllureFormatter -o allure-report  -f plain  --no-skipped --tags=@CucumberWithBut
# with allure report and no scenario filtering
# behave -f allure_behave.formatter:AllureFormatter -o allure-report  -f plain  --no-skipped -o allure-results
# allure serve allure-report
# pytest tests/ --alluredir=allure-report

# parallel execution but no allure reporting
# behavex ./features --parallel-processes 4 --parallel-scheme scenario -f allure_behave.formatter:AllureFormatter -o allure-report  -f plain
# behavex ./features --parallel-processes 4 --parallel-scheme feature -f allure_behave.formatter:AllureFormatter -o allure-report  -f plain


