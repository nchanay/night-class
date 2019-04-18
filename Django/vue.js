let app = new Vue({
  el: '#app',
  data: {
    message: "Hello World!"
  }
})

let app2 = new Vue ({
  el: '#app-2',
  data: {
    message: 'You loaded this page on ' + new Date().toLocaleString()
  }
})

let app3 = new Vue ({
  el: '#app-3',
  data: {
    seen: false
  }
})

let app4 = new Vue ({
  el: '#app-4',
  data: {
    todos: [
    { text: 'Learn JavaScript' },
    { text: 'Learn Vue' },
    { text: 'Build something awesome' }
    ]
  },
  method: {
    remove: function (evt, key) {
      this.todos.splice(1, key)
    }
  }
})
