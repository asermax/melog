@app = window.app ? {}

$ ->
    Backbone.Tastypie.csrfToken = $('meta[name="csrf-token"]').attr('content')
    
