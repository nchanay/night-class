let app = new Vue({
  el: '#display',
  data: {
    display: null
  },
  mounted: function() {
    let intervalID = setInterval(this.changeTime, 1000)
  },
  methods: {
    changeTime: function() {
      this.display = new Date().toLocaleTimeString()
    }
  }
})

let app2 = new Vue ({
  el: '#display2'.
  data: {
    display2: '00:00:00'
  },
  mounted: function() {

  },
  methods: {

  }
})
