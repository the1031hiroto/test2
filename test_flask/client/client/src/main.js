import 'bootstrap/dist/css/bootstrap.css';
import Vue from 'vue';
import App from './App';
import router from './router';

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
});

// bootstrap the demo
var demo = new Vue({
  el: '#demo',
  data: {
    searchQuery: '',
    gridColumns: ['name', 'power', 'hello'],
    gridData: [
      { name: 'Chuck Norris', power: Infinity, hello: 'hello' },
      { name: 'Bruce Lee', power: 9000, hello: 'world' },
      { name: 'Jackie Chan', power: 7000, hello: 'world' },
      { name: 'Jet Li', power: 8000, hello: 'world' },
      { name: 'Jet Li', power: 8000, hello: 'hello' }
    ]
  }
})