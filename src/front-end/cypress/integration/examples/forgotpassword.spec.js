describe('Check functionality of the sign in page', () => {

  beforeEach(() => {
    cy.intercept('POST', '**/identitytoolkit/**').as('submitted')
    cy.visit('http://localhost/forgotPassword')
  });

  it('sends reset email', () => {
    cy.get('ion-input [type="email"]').type('test@test.com');
    cy.get('ion-button').click();
    cy.on('window:alert', (str) => {
      expect(str).to.contains('Check your registered email to reset the password!')
    })

    cy.url().should('eq', 'http://localhost/SignIn')
  })

  it('does not find non-registered user', () => {
    cy.get('ion-input [type="email"]').type('nonexistent@not.com');
    cy.get('ion-button').click();


    cy.on('window:alert', (str) => {
      expect(str).to.contains('There is no user record corresponding to this identifier. The user may have been deleted.')
    })

    cy.wait('@submitted').its('response.statusCode').should('eq', 400)
    cy.url().should('eq', 'http://localhost/forgotPassword')
  })


  it('redirect user to sign in', () => {
    cy.get('a[href*="/"]').click();
    cy.url().should('eq', 'http://localhost/SignIn')
  })
})
