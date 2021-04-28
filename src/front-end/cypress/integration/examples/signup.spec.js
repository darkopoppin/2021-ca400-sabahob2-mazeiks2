describe('Check functionality of the sign in page', () => {
  
  beforeEach(() => {
    cy.intercept('POST', '**/identitytoolkit/**').as('signedUp')
    cy.visit('http://localhost/SignUp')
  });

  it('registers user and redirect to preferences', () => {
    cy.get('ion-input [type="text"]').type('cypress');
    cy.get('ion-input [type="email"]').type('cypress@test.com');
    cy.get('ion-input [type="password"]').type('cypressor');
    cy.get('ion-button').click();
    
    cy.wait('@signedUp').url().should('eq', 'http://localhost/categorySelection')
  })

  it('does not register already created user', () => {
    cy.get('ion-input [type="text"]').type('test');
    cy.get('ion-input [type="email"]').type('test@test.com');
    cy.get('ion-input [type="password"]').type('testing');
    cy.get('ion-button').click();
    
    cy.url().should('eq', 'http://localhost/SignUp')
  })

  it('redirect user to sign in', () => {
    cy.get('a[href*="/"]').click();
    cy.url().should('eq', 'http://localhost/SignIn')
  })
})
