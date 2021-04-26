// https://docs.cypress.io/api/introduction/api.html
import { mount } from '@vue/test-utils'
import Home from '@/views/Home.vue'

describe('My First Test', () => {
  it('Visits the app root url', () => {
    const wrapper = mount(Home)
    expect(wrapper.find("h3").text()).toMatch('Welcome')
  })
})
