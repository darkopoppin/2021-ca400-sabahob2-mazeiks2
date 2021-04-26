// https://docs.cypress.io/api/introduction/api.html

describe('My First Test', () => {
  beforeEach(() => {
    cy.visit('http://localhost')
  });
  it('Visits the app root url', () => {
    cy.get('h3').should('contain', 'Login')
  })
})
