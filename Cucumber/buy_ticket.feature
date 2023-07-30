Feature: Buy Ticket Flow

  Scenario: User can buy a ticket
    Given I am on the login page
    When I enter my credentials with "<email>" and "<password>"
    And I tap the login button
    And I tap the continue CTA
    And I grant location permission
    And I tap the buy ticket CTA
    And I select the beds & bucks option
    And I select the aylesbury plus option
    And I tap the purchase ticket CTA
    And I tap on the adult ticket
    And I add 1 adult day 5
    And I proceed to view the basket
    And I scroll down
    And I select the payment method
    Then I should be able to buy the ticket successfully
