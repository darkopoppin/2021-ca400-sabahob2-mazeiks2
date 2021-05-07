describe('Check functionality of the sign in page', () => {
  
  beforeEach(() => {
    cy.intercept('POST', '**/identitytoolkit/**').as('signedIn')
    cy.visit('http://localhost/SignIn')
  });

  it('Should log the user in', () => {
    cy.get('ion-input [type="email"]').type('test@test.com');
    cy.get('ion-input [type="password"]').type('testing');
    cy.get('ion-button').click();
    cy.wait('@signedIn').its('response.statusCode').should('eq', 200)
    cy.get('h3').should('contain', 'Welcome')
  })

  it('should not log the user in', () => {
    cy.get('ion-input [type="email"]').type('wrong@user.com');
    cy.get('ion-input [type="password"]').type('empty');
    cy.get('ion-button').click();
    cy.wait('@signedIn').url().should('eq', 'http://localhost/SignIn')
  })

  it('redirect to forgot password', () => {
    cy.get('a[href*="/ForgotPassword"]').click();
    cy.url().should('eq', 'http://localhost/ForgotPassword')
  })

  it('redirect user to register', () => {
    cy.get('a[href*="/SignUp"]').click();
    cy.url().should('eq', 'http://localhost/SignUp')
  })

  it('checks url authentication protection', () => {
    cy.visit('http://localhost/categorySelection')
    cy.url().should('eq', 'http://localhost/SignIn')
  })
})
